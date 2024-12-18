import os
import subprocess
from datetime import datetime
import sys

def compress_folder(source_path, target_path, folder_name):
    """
    压缩指定文件夹为7z格式
    
    参数:
    source_path: 源文件夹路径
    target_path: 压缩文件保存路径
    folder_name: 文件夹名称
    """
    try:
        # 获取当前时间，格式化为字符串
        current_time = datetime.now().strftime('%Y%m%d_%H%M')
        
        # 构建压缩文件的完整路径（文件名+时间戳）
        zip_name = f"{folder_name}_{current_time}.7z"
        zip_path = os.path.join(target_path, zip_name)
        
        # 检查7z是否已安装
        if sys.platform == 'win32':
            seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"
            if not os.path.exists(seven_zip_path):
                print("错误：请先安装7-Zip软件！")
                return False
        else:
            # Linux/Mac下检查7z命令
            if subprocess.call(['which', '7z'], stdout=subprocess.PIPE) != 0:
                print("错误：请先安装7z压缩软件！")
                return False
        
        # 创建保存压缩文件的目录（如果不存在）
        os.makedirs(target_path, exist_ok=True)
        
        # 构建7z命令
        if sys.platform == 'win32':
            cmd = [seven_zip_path, 'a', '-t7z', zip_path, source_path]
        else:
            cmd = ['7z', 'a', '-t7z', zip_path, source_path]
        
        # 执行压缩命令
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            print(f"完成：{zip_path}")
            return True
        else:
            print(f"失败：{stderr}")
            return False
            
    except Exception as e:
        print(f"出错：{str(e)}")
        return False

def main():
    """
    主函数，支持命令行参数
    """
    if len(sys.argv) != 4:
        print("用法: python auto_compress.py <源文件夹路径> <目标保存路径> <文件夹名称>")
        sys.exit(1)
        
    source_folder = sys.argv[1]
    target_folder = sys.argv[2]
    folder_name = sys.argv[3]
    
    # 执行压缩
    compress_folder(source_folder, target_folder, folder_name)

if __name__ == "__main__":
    main() 