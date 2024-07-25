import os
import shutil


def clean():
    root_dir = os.getcwd()

    # 根目录的临时文件
    extract_dir = os.path.join('temp_extracted')
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)

    # out 文件
    out_dir = os.path.join('out')
    if os.path.exists(out_dir):
         shutil.rmtree(out_dir)
    
    # dex2jar 下文件
    dex2jar_dir = os.path.join("tools", "dex2jar-2.0")
    os.chdir(dex2jar_dir)

    jar_files = [f for f in os.listdir() if f.endswith('.jar')]
    for file in jar_files:
        os.remove(file)
        print(f"remove file {file}")

    dex_files = [f for f in os.listdir() if f.endswith('.dex')]
    for file in dex_files:
        os.remove(file)
        print(f"remove file {file}")

    error_files = [f for f in os.listdir() if f.endswith('error.zip')]
    for file in error_files:
        os.remove(file)
        print(f"remove file {file}")

    os.chdir(root_dir)  
    print('clean finished')


if __name__ == "__main__":
    clean()