import cv2
import numpy as np
from matplotlib import pyplot as plt

result={}
des_temp={}

def im_read(img1,img2):
	query=cv2.imread(img1+'.png')
	comp=cv2.imread(img2+'.png')
	return query,comp

def save_des(im1,des_1,im2,des_2):
	des_temp[im1]=des_1
	des_temp[im2]=des_2
	np.save('des_file',des_temp)
	print("saved!")


def bfmatch_func(img1,img2):
	query_img,train_img=im_read(img1,img2)

	orb=cv2.ORB_create()
	_,des_q=orb.detectAndCompute(query_img,None)
	_,des_t=orb.detectAndCompute(train_img,None)
	save_des(img1,des_q,img2,des_t)

	bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)	
	matches=bf.match(des_q,des_t)
	dis= [m.distance for m in matches]
	result[img2+'.png'] = sum(dis)/len(dis)
	return result
	

if __name__=='__main__':
	print("main")
	query=input('*Plese input query filename\n')
	print(bfmatch_func('{}'.format(query),'test'))
	print(np.load('des_file.npy'))

	#img3=cv2.drawMatches(query_img,kp_q,train_img,kp_t,matches[:10],None,flags=2)
	#plt.imshow(img3)
	#plt.show()


