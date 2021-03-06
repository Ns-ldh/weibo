import os
from hashlib import md5, sha256


def make_password(password):
    '''产生一个安全密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')

    # 计算哈希值
    hash_value = sha256(password).hexdigest()

    # 产生随机盐, 长度 32 字节
    salt = os.urandom(16).hex()

    # 加盐，产生安全密码
    safe_password = salt + hash_value

    return safe_password


def check_password(password, safe_password):
    '''检查密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')

    # 计算哈希值
    hash_value = sha256(password).hexdigest()

    return hash_value == safe_password[32:]


def save_avatar(avatar_file):
    '''保存头像文件'''
    # 读取文件的二进制数据
    file_bin_data = avatar_file.stream.read()

    # 文件指针归零
    avatar_file.stream.seek(0)

    # 计算文件的 md5 值
    filename = md5(file_bin_data).hexdigest()

    # 获取项目文件夹的绝对路径
    base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

    # 文件绝对路径
    filepath = f'{base_dir}/static/upload/{filename}'

    # 保存文件
    avatar_file.save(filepath)

    # 文件的 URL
    avatar_url = f'/static/upload/{filename}'

    return avatar_url
