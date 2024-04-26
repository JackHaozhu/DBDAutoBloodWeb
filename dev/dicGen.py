import os

def list_files_to_file(directory, output_file):
    # 打开输出文件以写入模式
    with open(output_file, 'w') as f:
        # 遍历指定目录及其子目录中的所有文件
        for root, dirs, files in os.walk(directory):
            for file in files:
                # 获取文件的相对地址
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                # 加上单引号
                relative_path_quoted = "'" + relative_path + "',"
                # 将相对地址写入文件
                f.write(relative_path_quoted + '\n')

# 指定要遍历的文件夹路径
folder_path = r'D:\SteamLibrary\steamapps\common\Dead by Daylight\DeadByDaylight\Content\UI\Icons\Favors'

# 指定输出文件路径
output_file = "filedir.txt"

# 调用函数将文件相对地址写入到文件中
list_files_to_file(folder_path, output_file)

print("文件相对地址已写入到", output_file)
