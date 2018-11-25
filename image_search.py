import cv2
import numpy as np
import pickle
import os
from matplotlib import pyplot as plt

result={}
des_temp={}
#des_data={}

with open('des_file.pickle',mode='rb+') as file:
	des_data=pickle.load(file)

def im_read(img1,img2):
	query=cv2.imread(img1,0)
	comp=cv2.imread('./dataset/'+img2,0)
	cv2.imshow('query',query)
	return query,comp

def save_des(imt,des_t):
	des_temp[imt]=des_t
	with open('des_file.pickle',mode='wb+') as file:
		pickle.dump(des_temp,file)
	print("saved!")


def bfmatch_func(img1,img2):
	query_img,train_img=im_read(img1,img2)
	orb=cv2.ORB_create()
	_,des_q=orb.detectAndCompute(query_img,None)
	if(img2 in des_data): #dataset中のdesを保存したい
		des_t=des_data[img2]
		print("aleady data")
	else:
		_,des_t=orb.detectAndCompute(train_img,None)
		save_des(img2,des_t)

	bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)	
	matches=bf.match(des_q,des_t)
	dis= [m.distance for m in matches]
	result[img2] = sum(dis)/len(dis)
	

if __name__=='__main__':
	query=input('*Plese input query filename\n')
	files=os.listdir('./dataset')
	for f in files:	
		print(f)
		bfmatch_func('{}'.format(query),f)
	shortest_img=min(result,key=result.get)
	result=sorted(result.items(), key=lambda x:x[1])
	result_img=cv2.imread('./dataset/'+shortest_img)
	print("result for {}: {}".format(query,shortest_img))
	print("shortest list:{}\n{}\n{}".format(result[0],result[1],result[2]))
	cv2.imshow(shortest_img,result_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
