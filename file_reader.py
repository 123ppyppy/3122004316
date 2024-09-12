def read_file(file_path):
    """读取文件内容并返回字符串"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()#返回读取的内容后面做预处理
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return None#如果该文件不存在，应抛出异常