#coding:utf-8
# License: BSD
# Original author: Sasank Chilamkurthy
# Modified by Fanyang Meng, nkliuyifang

from __future__ import print_function, division
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
from torchvision import datasets, models, transforms
import numpy as np
from torch.utils.data import TensorDataset,DataLoader
from model import FullCNN
import torch.nn.functional as FUN
import time
import os
import argparse

#os.environ["CUDA_VISIBLE_DEVICES"] = "3"

parser = argparse.ArgumentParser()
#######################################   

parser.add_argument("data_dir", type=str, default = 'type1/NTU_cross_setup')
parser.add_argument("save_dir", type=str, default = 'type1/NTU_cross_setup/model')
parser.add_argument("batch_size", type=int, default = 64)

args = parser.parse_args()

#matlab data dir  
data_dir = args.data_dir
save_dir = args.save_dir
batch_size = args.batch_size

######################################################################
modelft_file = save_dir + "/best.pth"

def reloaddata():
    data_transforms = {
        'train': transforms.Compose([
            #transforms.RandomSizedCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'test': transforms.Compose([
            #transforms.Scale(256),
            #transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }
    image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                          data_transforms[x])
                  for x in ['test']}
    dset_loaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size,
                                             shuffle=False, num_workers=1)
                  for x in ['test']}    
    dset_sizes = len(image_datasets['test'])
#    image_datasets =  datasets.ImageFolder(os.path.join(data_dir, 'train'), data_transforms['train'])
#    dset_loaders = torch.utils.data.DataLoader(image_datasets, batch_size=batch_size,shuffle=True, num_workers=1)    
#
#    dset_sizes = len(image_datasets)
    return dset_loaders, dset_sizes

use_gpu = torch.cuda.is_available()
######################################################################
def test_model(model,criterion):
    model.eval()
    running_loss = 0.0
    running_corrects = 0
    cont = 0
    outPre = []
    outLabel = []
    dset_loaders, dset_sizes = reloaddata()
    # Iterate over data.
    for data in dset_loaders['test']:
        # get the inputs
        inputs, labels = data
        labels = torch.squeeze(labels.type(torch.LongTensor))
        inputs, labels = Variable(inputs.cuda()), \
                Variable(labels.cuda())
        # forward
        outputs =  model(inputs)
        _, preds = torch.max(outputs.data, 1)
        loss = criterion(outputs, labels)   
        if cont==0:
            outPre = outputs.data.cpu()
            outLabel = labels.data.cpu()
        else:
            outPre = torch.cat((outPre,outputs.data.cpu()),0)
            outLabel = torch.cat((outLabel,labels.data.cpu()),0)
        # statistics
        running_loss += loss.data[0]
        running_corrects += torch.sum(preds == labels.data)
        print('Num:',cont)
        cont +=1

    print('Loss: {:.4f} Acc: {:.4f}'.format(running_loss/dset_sizes,
                    running_corrects/dset_sizes))
       
    return FUN.softmax(Variable(outPre)).data.numpy(), outLabel.numpy()
    
######################################################################
#torch.cuda.set_device(2)
model_ft = torch.load(modelft_file).cuda()
criterion = nn.CrossEntropyLoss().cuda()
######################################################################
outPre, outLabel = test_model(model_ft,criterion)

np.save(save_dir + '/Pre',outPre)
np.save(save_dir + '/Label',outLabel)

