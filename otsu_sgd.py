'''
Otsu method and simple stochastic gradient descent
'''


import time
import os
import h5py
import hdf5storage
import numpy as np
import math
from scipy import signal as spsig
import struct
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
import gc
import cv2
import torch



def testfun(x):
    return x[0]**2+(x[1]-2)**2


def try_sgd(x1=10.,x2=10.):

    x = torch.tensor([x1,x2], requires_grad = True)
    optimizer = torch.optim.SGD([x], lr=1, momentum=0.25)

    for it in range(100):
        optimizer.zero_grad()
        y = testfun(x)
        y.backward()
        optimizer.step()
        print(it,y.item(),x.detach().numpy())
        if y.item()<1e-6:
            break
    
    print(x.detach().numpy())
    return y.item()	




def otsu_var(im,th):

    temp=np.zeros(im.shape)
    temp[im>th] = 1

    npx = im.size
    npx1 = np.count_nonzero(temp)
    w1 = npx1/npx
    w0 = 1-w1

    if w0>0 and w1>0:
        vp0=im[temp==0]
        vp1=im[temp==1]
        var0 = np.var(vp0) if len(vp0)>0 else 0	 	
        var1 = np.var(vp1) if len(vp1)>0 else 0
        return w0*var0 + w1*var1
    else:
        return np.inf	


def arr_otsu_trans(arr):

    thrange = np.arange(np.max(arr)+1)
    vval = [otsu_var(arr,th) for th in thrange]
    rval = thrange[np.argmin(vval)]    
    res = np.zeros(arr.shape)
    res[arr>rval] = 1

    return(res)    




def main():
    print(" ")
	
    n = 50000

#    print("Initialize Preprocessor")
#    preprocess = Preprocessor()

    #print("Trying openfile")
    #files = preprocess.openfile()
    files = ['']
	
    fname = 'test2'

    im = cv2.imread(fname+'.png')
    print(type(im),np.shape(im))

    grim = 0.299 * im[:,:,0] + 0.587 * im[:,:,1] + 0.114 * im[:,:,2] 
#    rim = arr_otsu_trans(grim)
	
#    plt.imshow(grim)
#    plt.title('grayscale before')
#    plt.savefig(fname + '_' + str(time.time())[12:] + '_grayscale_before_' + '.png', dpi = 400)
#    plt.cla()

#    plt.imshow(rim)
#    plt.title('grayscale after')
#    plt.savefig(fname + '_'  + str(time.time())[12:] + '_grayscale_after_' + '.png', dpi = 400)
#    plt.cla()


    u = try_sgd()
    print(u)
	

    #for i in range(0,10):
    
#    status = preprocess.process_full(0)

			
#    if status:
#        print("Processing failed")
#    else:
#        print("Processing is successfully complected")
		
    print(" ")

	
	

if __name__ == "__main__":
    main()
