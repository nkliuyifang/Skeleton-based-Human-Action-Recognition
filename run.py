import os

for type in range(1,5):
  for seed in range(1,11):
    os.system("mkdir UTD-MHAD_img_type_"+str(type)+"/model_"+str(seed))
    os.system("python train.py 'UTD-MHAD_img_type_"+str(type)+"' 'UTD-MHAD_img_type_"+str(type)+"/model_"+str(seed)+"' 16 0.001 27 "+str(seed))
    os.system("python test.py 'UTD-MHAD_img_type_"+str(type)+"' 'UTD-MHAD_img_type_"+str(type)+"/model_"+str(seed)+"' 16")

for type in range(1,5):
  for seed in range(1,11):
    os.system("mkdir Northwestern-UCLA_img_type_"+str(type)+"/model_"+str(seed))
    os.system("python train.py 'Northwestern-UCLA_img_type_"+str(type)+"' 'Northwestern-UCLA_img_type_"+str(type)+"/model_"+str(seed)+"' 16 0.001 10 "+str(seed))
    os.system("python test.py 'Northwestern-UCLA_img_type_"+str(type)+"' 'Northwestern-UCLA_img_type_"+str(type)+"/model_"+str(seed)+"' 16")
