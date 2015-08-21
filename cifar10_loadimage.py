import random
import os
import sys
import math
import numpy as np
import copy

from PIL import Image



filename100 = "D://python2.7.6//MachineLearning//cifar-CNN3//cifar-100-python//train"
filename10 = "D://python2.7.6//MachineLearning//cifar-CNN3//cifar-10-batches-py"
datafile="D://python2.7.6//MachineLearning//cifar-CNN3//dataVec.txt"
labelfile="D://python2.7.6//MachineLearning//cifar-CNN3//dataLabel.txt"


train_batch=['data_batch_1','data_batch_2','data_batch_3','data_batch_4']
test_batch='test_batch'
valid_batch='data_batch_5'

global dataDic;dataDic={}

def unpickle():
    global train_set_x,train_set_y,valid_set_x,valid_set_y,test_set_x,test_set_y
    train_set_x=np.zeros((40000,3072));train_set_y=np.zeros((40000,))
    import cPickle
    for fn in train_batch:
        fo = open(filename10+'//'+fn, 'rb')
        index=train_batch.index(fn)
        dataDic=cPickle.load(fo)#dataDic={data labels batch_lable,file_name}
        train_set_x[index*10000:(index+1)*10000,:] = dataDic['data']
        train_set_y[index*10000:(index+1)*10000,]=np.array(dataDic['labels'])
        fo.close()

    #####
    fo = open(filename10+'//'+test_batch, 'rb')
    dataDic=cPickle.load(fo)#dataDic={data labels batch_lable,file_name}
    test_set_x=dataDic['data']#[1w,3072]
    test_set_y=np.array(dataDic['labels'])#[1w,]
    fo.close()

    ####
    fo = open(filename10+'//'+valid_batch, 'rb')
    dataDic=cPickle.load(fo)#dataDic={data labels batch_lable,file_name}
    valid_set_x=dataDic['data']
    valid_set_y=np.array(dataDic['labels'])
    fo.close()

    datasets=[(train_set_x,train_set_y),(test_set_x,test_set_y),(valid_set_x,valid_set_y)]
    return datasets
    #print train_set_x[39999,3071],test_set_x[9999,3071]
     



########
'''
dataDic=unpickle(filename10)
for k,v in dataDic.items():
    print type(v),len(v),np.shape(v)
    
print dataDic.keys()
print set(dataDic['labels']),set(dataDic['batch_label'])
print dataDic['labels'][:10],dataDic['filenames'][:20]
dataDic={data:[1w,3072],labels:[10000,],batch_label:21string,file-name:[1w,]}
'''
if __name__='__main__':
    unpickle()





 
 

 
    
         
    
    
    

'''
<type 'str'> <type 'numpy.ndarray'> 4 10000
<type 'str'> <type 'list'> 6 10000
<type 'str'> <type 'str'> 11 21
<type 'str'> <type 'list'> 9 10000
keys['data', 'labels', 'batch_label', 'filenames']
values array(10000, 3072),list 10000,str 21,list 10000
'''






    
    
