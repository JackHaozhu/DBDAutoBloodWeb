import os

def list_files(startpath, relpath=''):
    file_dict = {}
    for root, dirs, files in os.walk(startpath):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), startpath)
            file_name, file_extension = os.path.splitext(file)
            # 寻找文件名中的两条下划线
            first_underscore_index = file_name.find('_')
            second_underscore_index = file_name.find('_', first_underscore_index + 1)
            # 提取两条下划线之间的部分作为键
            if first_underscore_index != -1 and second_underscore_index != -1:
                key = file_name[first_underscore_index + 1:second_underscore_index]
                file_dict[key] = file_path
    return file_dict

# 指定文件夹路径
folder_path = r'D:\SteamLibrary\steamapps\common\Dead by Daylight\DeadByDaylight\Content\UI\Icons\CharPortraits'

# 获取文件夹内所有文件的地址
file_dict = list_files(folder_path)

# 将结果写入文件
with open('filedir.txt', 'w') as file:
    for file_name, file_path in file_dict.items():
        file.write(f"'{file_name}': '{file_path}',\n")
