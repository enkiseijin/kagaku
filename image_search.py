import cv2
import numpy as np
import pickle
import os
from matplotlib import pyplot as plt

result={}
des_temp={}
des_data={}

#with open('des_file.pickle',mode='rb+') as file:
#	des_data=pickle.load(file)

def im_read(img2):
	#query=cv2.imread(img1,0)
	comp=cv2.imread('./dataset/'+img2,0)
	#cv2.imshow('query',query)
	return comp

def save_des(imt,des_t):
	des_temp[imt]=des_t
	with open('des_file.pickle',mode='wb+') as file:
		pickle.dump(des_temp,file)
	print("saved!")


def bfmatch_func(img1):
	query_img=cv2.imread(img1,0)

	orb=cv2.ORB_create()
	kp_q,des_q=orb.detectAndCompute(query_img,None)

	mini=1000
	files=os.listdir('./dataset')

	for f in files:	
		train_img=im_read(f)
		kp_t,des_t=orb.detectAndCompute(train_img,None)


		bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)	
		matches=bf.match(des_q,des_t)
		dis= [m.distance for m in matches]
		result[f] = sum(dis)/len(dis) #database画像ごとの距離平均
		if(result[f]<mini):
			mini=result[f]
			mini_kp=kp_t
			mini_img=train_img
			mini_match=matches
	return cv2.drawMatches(query_img,kp_q,mini_img,mini_kp,mini_match[:10],None,flags=2)


if __name__=='__main__':
	query=input('*Plese input query filename\n')
	match_kp_img=bfmatch_func(query)

	shortest_img=min(result,key=result.get)
	result=sorted(result.items(), key=lambda x:x[1])
	result_img=cv2.imread('./dataset/'+shortest_img)
	print("result for {}: {}".format(query,shortest_img))
	print("shortest list:{}\n{}\n{}".format(result[0],result[1],result[2]))
	cv2.imshow('near_img',result_img)
	cv2.imshow('key point matching',match_kp_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
