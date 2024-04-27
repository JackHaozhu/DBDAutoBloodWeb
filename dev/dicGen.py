import os

def list_files(root_dir):
    files_dict = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_extension = os.path.splitext(file)
            after_underscore = file_name.split("_")[1] if "_" in file_name else file_name
            relative_path = os.path.relpath(file_path, root_dir)
            files_dict[after_underscore] = relative_path
    return files_dict

def write_to_file(file_dict, output_file):
    with open(output_file, "w") as f:
        for key, value in file_dict.items():
            f.write(f"'{key}': '{value}',\n")

# 定义文件夹路径
folder_path = r'D:\SteamLibrary\steamapps\common\Dead by Daylight\DeadByDaylight\Content\UI\Icons\Favors'

# 获取文件信息
files_info = list_files(folder_path)

# 将文件信息写入文件
output_file_path = "filedir.txt"
write_to_file(files_info, output_file_path)
