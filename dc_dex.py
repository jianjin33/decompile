import os
import subprocess
import shutil
import zipfile

"""
1. 解压apk
2. 获取dex
3. dex转jar
"""

def find_apk_file(directory):
    files = os.listdir(directory)
    for file in files:
        if file.endswith('.apk'):
            return os.path.join(directory, file)
    return None

def copy_and_rename_apk(apk_path):
    file_dir, file_name = os.path.split(apk_path)
    base_name, _ = os.path.splitext(file_name)
    
    new_file_path = os.path.join(file_dir, f"{base_name}.zip")
    
    shutil.copyfile(apk_path, new_file_path)
    return new_file_path

def extract_zip_file(zip_path, extract_to):
    # 解压缩 .zip 文件
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def move_dex_files(extracted_dir, dex2jar_dir):
    for root, dirs, files in os.walk(extracted_dir):
        for file in files:
            if file.endswith('.dex'):
                dex_file_path = os.path.join(root, file)
                shutil.move(dex_file_path, dex2jar_dir)
                print(f"Moved {file} to {dex2jar_dir}")


def run_dex2jar():
    dex_files = [f for f in os.listdir() if f.endswith('.dex')]
    for file in dex_files:
        print("start dex2jar " + file + "------------------------")
        subprocess.call('d2j-dex2jar.bat ' + file)
        os.remove(file)
        print("end dex2jar " + file + "------------------------")

    # 删除生成的错误文件
    error_files = [f for f in os.listdir() if f.endswith('error.zip')]
    for file in error_files:
        os.remove(file)
        print(f"remove file {file}")

def move_jar_files(dex2jar_dir, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历 dex2jar 目录中的 .jar 文件
    for file in os.listdir(dex2jar_dir):
        if file.endswith('.jar'):
            jar_file_path = os.path.join(dex2jar_dir, file)
            shutil.move(jar_file_path, output_dir)
            print(f"Moved {file} to {output_dir}")

def copy_jd_gui(tools_directory, output_directory):
     for file in os.listdir(tools_directory):
         if file.startswith('jd-gui'):
            jd_gui_path = os.path.join(tools_directory, file)
            shutil.copy(jd_gui_path, output_directory)
            break

def decompile_dex():
    current_directory = os.getcwd()
    apk_file = find_apk_file(current_directory)
    print(f"apk path: {apk_file}")

    if apk_file:
        # 复制并重命名 .apk 文件为 .zip
        zip_file = copy_and_rename_apk(apk_file)
        print(f"Copied and renamed to: {zip_file}")
        
        # 解压缩 .zip 文件
        extract_directory = os.path.join(current_directory, 'temp_extracted')
        extract_zip_file(zip_file, extract_directory)
        os.remove(zip_file)

        # 移动 .dex 文件到 dex2jar 目录
        tools_directory = os.path.join(current_directory, "tools")
        dex2jar_directory = os.path.join(tools_directory, "dex2jar-2.0")
        move_dex_files(extract_directory, dex2jar_directory)

        shutil.rmtree(extract_directory)

        # 进入 /tools/dex2jar-2.0 文件夹 并执行dex2jar 命令
        os.chdir(dex2jar_directory)
        run_dex2jar()
        
        # 返回根目录
        os.chdir(current_directory)

        output_directory = os.path.join(current_directory, "out", "jar")
    
         # 移动 .jar 文件
        move_jar_files(dex2jar_directory, output_directory)

        # jd-gui工具copy一份
        copy_jd_gui(tools_directory, output_directory)

if __name__ == "__main__":
    decompile_dex()