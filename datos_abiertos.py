from sodapy import Socrata
import datetime
import pandas as pd


def get_meta_from_item(ds_item):
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

def get_metadata(type:str=None):
    ## get datasets
    with Socrata("www.datos.gov.co", None) as client:
        data = client.datasets(limit=0, offset=0)
    ## get meta
    meta = [get_meta_from_item(x) for x in data]
    metadata = pd.DataFrame(meta)
    metadata['getdata_datetime'] = datetime.datetime.now()
    if type!=None:
        metadata = metadata[metadata['type']==type].reset_index(drop=True)
    return metadata



## main
metadata = get_metadata()
