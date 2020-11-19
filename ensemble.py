import os


filename1 = '/project/jmhan/AerialDetection/work_dirs/faster_rcnn_RoITrans_er50_fpn_1x_dota_inv_/Task1_results/'
filename2 = '/project/jmhan/AerialDetection/work_dirs/faster_rcnn_RoITrans_r50_fpn_1x_dota_/Task1_results/'
# filename1 = '/project/jmhan/AerialDetection/work_dirs/test1/Task1_results/'
# filename2 = '/project/jmhan/AerialDetection/work_dirs/test2/Task1_results/'
des_filename = '/project/jmhan/AerialDetection/work_dirs/ensemble_test/Task1_results/'

list1 = os.listdir(filename1)
list2 = os.listdir(filename2)

for i in range(len(list1)):
    txt_file1 = open(filename1 + list1[i])
    context1 = txt_file1.read()
    txt_file2 = open(filename2 + list1[i])
    context2 = txt_file2.read()
    txt_file_des = open(des_filename + list2[i], 'w')
    
    #import ipdb
    #ipdb.set_trace()
    
    txt_file_des.write(context1)
    txt_file_des.write('\n')
    txt_file_des.write(context2)
    
    txt_file_des.close()