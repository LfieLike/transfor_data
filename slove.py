import scipy.io as scio
import os
from shutil import copy
def mycopy(is_test,src,type_name,dst='./'):
    print(is_test)
    if not os.path.exists(dst+'val/'):
        os.mkdir(dst+'val/')
    if not os.path.exists(dst+'train/'):
        os.mkdir(dst+'train/')
    if is_test == '1':
        if not os.path.exists(dst+'val/'+type_name):
            os.mkdir(dst+'val/'+type_name)
        copy('car_ims/'+src,dst+'val/'+type_name+'/'+src)
    else:
        if not os.path.exists(dst+'train/'+type_name):
            os.mkdir(dst+'train/'+type_name)
        copy('car_ims/'+src,dst+'train/'+type_name+'/'+src)
def transform_to_imagenet(srclable,srcdata):
    data_mat = scio.loadmat(srclable)
    key = list(data_mat.keys())[-2]
    datas = data_mat[key]
    for data in datas:
        for line in data:
            src = line[0][0][-10:]
            is_test = line[-1][0][0]
            type_name = line[-2][0][0]
            mycopy(str(is_test),str(src),str(type_name))

transform_to_imagenet('cars_annos.mat','.')