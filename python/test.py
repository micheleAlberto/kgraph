import numpy as np
import pykgraph
import time
import os
datasetPath='dataset/'
indexPath='index/'
query_size= 4000
dataset_size=query_size*16
bin_bytes=32
sift_bins=128

def load_float():
    name='float'
    index = pykgraph.KGraph()
    dataset = np.load(datasetPath+name+'.npy')
    index.load(indexPath+name)
    return index,dataset

def load_bin():
    name='bin'
    index = pykgraph.KGraph()
    dataset = np.load(datasetPath+name+'npy')
    index.load(indexPath+name)
    return index,dataset

def gen_float(n=dataset_size,K=10,L=128,S=30,prune=0):
    name='float'
    dataset = np.random.rand(n, sift_bins)
    print 'dataset {0} generato'.format(name)
    np.save(datasetPath+name,dataset)
    print 'dataset {0} salvato'.format(name)
    index = pykgraph.KGraph()
    index.build(dataset)
    index.save(indexPath+name)
    print 'indice {0} salvato'.format(name)
    return index,dataset

def gen_bin(n=dataset_size):
    name='bin'
    dataset = np.random.randint(256,size=(n,bin_bytes)).astype(np.uint8)
    print 'dataset {0} generato'.format(name)
    np.save(datasetPath+name,dataset)
    print 'dataset {0} salvato'.format(name)
    index = pykgraph.KGraph()
    index.build(dataset)
    index.save(indexPath+name)
    print 'indice {0} salvato'.format(name)
    return index,dataset

def gen_query_float(n=query_size):
    return np.random.rand(n, sift_bins)

def gen_query_bin(n=query_size):
    return np.random.randint(256,size=(n,bin_bytes)).astype(np.uint8)

def do():
    f_index , f_dataset= gen_float()
    f_query=gen_query_float()
    f_index.search(f_dataset,f_query)

def bin_test(n_q=[query_size],n_dts=dataset_size,K=10,L=128,S=30,prune=0):
    name='bin'
    d = np.random.randint(256,size=(n_dts,bin_bytes)).astype(np.uint8)
    i = pykgraph.KGraph()
    start= time.time()
        
    end= time.time()
    buildTime=end-start
    i.save('tempIndex')
    stat = os.stat('tempIndex')
    indexSize=stat.st_size
    q=gen_query_bin(n_q)
    start= time.time()
    i.search(d,q,K=K)
    end= time.time()
    searchTime=end-start
    req={}
    req['querySize']=n_q
    req['datasetSize']=n_dts
    req['K']=K
    req['L']=L
    req['S']=S
    req['prune']=prune
    res={}
    res['buildTime']=buildTime
    res['unitBuildTime']=buildTime/n_dts
    res['searchTime']=searchTime
    res['unitSearchTime']=searchTime/n_q
    res['indexSize']=indexSize
    res['unitIndexSize']=indexSize/n_dts
    return {'request': req , 'response': res}

def tests():
    qqs=[4000,4000]
    dtsSzs=[4*4000,8*4000,16*4000,32*4000]
    Ks=[20,40]
    Ls=[128,160]
    Ss=[20,30,40]
    Ps=[0,1,2]
    results=[]
    for q in qqs:
        for dts in dtsSzs:
            for k in Ks:
                for l in Ls:
                    for s in Ss:
                        for p in Ps:
                            x=bin_test(n_q=q,n_dts=dts,K=k,L=l,S=s,prune=p)
                            results.append(x)
                            np.save('partialResults',results)
                            print x
    return results


def do_tests():
    np.save('testResult',tests())



    dtsSzs=4*4000
    Ks=20
    L=128
    S=30
    prune level=2

    
    
    

