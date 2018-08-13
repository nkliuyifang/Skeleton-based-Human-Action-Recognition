import os

os.system("mkdir Northwestern-UCLA_img_type_4/model")
os.system("python train.py 'Northwestern-UCLA_img_type_4' 'Northwestern-UCLA_img_type_4/model' 16 0.001 10")
os.system("python test.py 'Northwestern-UCLA_img_type_4' 'Northwestern-UCLA_img_type_4/model' 16")

os.system("mkdir Northwestern-UCLA_img_type_3/model")
os.system("python train.py 'Northwestern-UCLA_img_type_3' 'Northwestern-UCLA_img_type_3/model' 16 0.001 10")
os.system("python test.py 'Northwestern-UCLA_img_type_3' 'Northwestern-UCLA_img_type_3/model' 16")

os.system("mkdir Northwestern-UCLA_img_type_2/model")
os.system("python train.py 'Northwestern-UCLA_img_type_2' 'Northwestern-UCLA_img_type_2/model' 16 0.001 10")
os.system("python test.py 'Northwestern-UCLA_img_type_2' 'Northwestern-UCLA_img_type_2/model' 16")

os.system("mkdir Northwestern-UCLA_img_type_1/model")
os.system("python train.py 'Northwestern-UCLA_img_type_1' 'Northwestern-UCLA_img_type_1/model' 16 0.001 10")
os.system("python test.py 'Northwestern-UCLA_img_type_1' 'Northwestern-UCLA_img_type_1/model' 16")



#os.system("mkdir NTU_img_type_4/model")
#os.system("python train.py 'NTU_img_type_4' 'NTU_img_type_4/model' 192 0.01 60")
#os.system("python test.py 'NTU_img_type_4' 'NTU_img_type_4/model' 16")
#
#os.system("mkdir NTU_img_type_3/model")
#os.system("python train.py 'NTU_img_type_3' 'NTU_img_type_3/model' 192 0.01 60")
#os.system("python test.py 'NTU_img_type_3' 'NTU_img_type_3/model' 16")
#
#os.system("mkdir NTU_img_type_2/model")
#os.system("python train.py 'NTU_img_type_2' 'NTU_img_type_2/model' 192 0.01 60")
#os.system("python test.py 'NTU_img_type_2' 'NTU_img_type_2/model' 16")
#
#os.system("mkdir NTU_img_type_1/model")
#os.system("python train.py 'NTU_img_type_1' 'NTU_img_type_1/model' 192 0.01 60")
#os.system("python test.py 'NTU_img_type_1' 'NTU_img_type_1/model' 16")
