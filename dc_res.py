import os
import subprocess

"""
通过apktool_2.6.0.jar 反编译，获取apk中资resource、manifest、smali汇编码
生成的文件比较大
"""
def run_apktool(jar_path, apk_file, output_dir):
    print("start decompile res and smali")
    # 构建命令
    cmd = [
        "java",
        "-jar",
        jar_path,
        "d",  # "d" 表示解包
        "-f",
        apk_file,
        "-o",
        output_dir
    ]
    
    subprocess.call(cmd)
    print("complete decompile res and smali")


def find_apk_file(directory):
    files = os.listdir(directory)
    for file in files:
        if file.endswith('.apk'):
            return os.path.join(directory, file)
    return None


def decompile_res_smali():
    current_dir = os.getcwd()
    apk_file = find_apk_file(current_dir)
    print(f"apk path: {apk_file}")
    if apk_file:
        jar_path = os.path.join(current_dir, "tools", "apktool_2.6.0.jar")

        out_dir_base = os.path.join(current_dir, 'out')
        if not os.path.exists(out_dir_base):
            os.makedirs(out_dir_base)

        apk_name = os.path.splitext(os.path.basename(apk_file))[0]
        out_dir = os.path.join(out_dir_base, apk_name)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        
        run_apktool(jar_path, apk_file, out_dir)


if __name__ == "__main__":
    decompile_res_smali()