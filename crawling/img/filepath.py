import os

path_folder_outwear = 'D:\\Jblyoutwear\\'
path_folder_top = 'D:\\Jblytop\\'
path_folder_bottom = 'D:\\Jblybottom\\'
path_folder_acc = 'D:\\Jblyacc\\'
path_folder_shoes = 'D:\\Jblyshoes\\'

os.chmod('D:\\Jblyoutwear\\', 0o777)
os.chmod('D:\\Jblytop\\', 0o777)
os.chmod('D:\\Jblybottom\\', 0o777)
os.chmod('D:\\Jblyacc\\', 0o777)
os.chmod('D:\\Jblyshoes\\', 0o777)

stat_outwear = os.stat('D:\\Jblyoutwear\\')
stat_top = os.stat('D:\\Jblytop\\')
stat_bottom = os.stat('D:\\Jblybottom\\')
stat_acc = os.stat('D:\\Jblyacc\\')
stat_shoes = os.stat('D:\\Jblyshoes\\')

print(oct(stat_outwear.st_mode)[-3:])
print(oct(stat_top.st_mode)[-3:])
print(oct(stat_bottom.st_mode)[-3:])
print(oct(stat_acc.st_mode)[-3:])
print(oct(stat_shoes.st_mode)[-3:])