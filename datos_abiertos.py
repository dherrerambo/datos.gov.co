from sodapy import Socrata

def get_inventory()->dict:
    """
        the inventory can be parse as DataFrame with:
            pd.DataFrame.from_dict(inventory, orient='index')
    """
    def get_meta_from_item(ds_item:dict)->dict:
        """
            get metadata from dataset
        """
        cols = ['id','name','description']
        meta = dict((k,v) for k,v in ds_item['resource'].items() if k in cols)
        try:
            t = ds_item['classification'].copy()
            t.update(dict(list(a.values()) for a in t['domain_metadata']))
            del t['domain_metadata']
        except:
            print(meta['id'])
            pass
            raise Exception('there is no [classification][domain_metadata]')
        meta.update( t )
        meta.update( dict((k,v) for k,v in ds_item['resource'].items() if k not in cols) )
        return meta
    
    ## get data available
    with Socrata("www.datos.gov.co", None) as client:
        dataAvailable = client.datasets(limit=0, offset=0)
    ## get meta
    inventory = [get_meta_from_item(x) for x in dataAvailable]
    inventory = dict((x['id'], dict((k,v) for k,v in x.items() if k!='id')) for x in inventory)
    return inventory
