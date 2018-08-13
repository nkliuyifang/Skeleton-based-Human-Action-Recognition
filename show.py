#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np

for type in range(1,5):
  total = 0.0
  for seed in range(1,11):
  	labels_name = 'UTD-MHAD_img_type_'+str(type)+'/model_'+str(seed)+'/Label.npy'
  	labels  = np.load(labels_name)
  
  	predict_name = 'UTD-MHAD_img_type_'+str(type)+'/model_'+str(seed)+'/Pre.npy'
  	predict = np.load(predict_name)
  
  	preds = predict.argmax(axis=1)  
  	correct = np.sum(preds==labels)/(preds.size*1.0)
  	print(correct)
  	total += correct
  total /= 10.0 
  print('type: {}, correct: {}'.format(type,total))
