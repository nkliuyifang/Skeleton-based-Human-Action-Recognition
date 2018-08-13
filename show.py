#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np

for type in range(1,5):
	labels_name = 'Northwestern-UCLA_img_type_'+str(type)+'/model/Label.npy'
	labels  = np.load(labels_name)

	predict_name = 'Northwestern-UCLA_img_type_'+str(type)+'/model/Pre.npy'
	predict = np.load(predict_name)

	preds = predict.argmax(axis=1)  
	correct = np.sum(preds==labels)/(preds.size*1.0)
	print('type: {}, correct: {}'.format(type,correct))
