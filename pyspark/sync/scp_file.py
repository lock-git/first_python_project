"""
@Time: 2021/3/11 13:49

@Author: dukeqiang
"""

import paramiko
from scp import SCPClient
import datetime

# 将指定目录的图片文件上传到服务器指定目录
# host 服务器ip地址
# remote_path远程服务器目录
# file_path本地文件夹路径
# model_name是file_path本地文件夹路径下面的文件名称
def upload_img(model_name, remote_path="/data01/go_project/src/lgb_model",host = "10.101.34.227",
               file_path="/home/jdduser/wangben/lightgbm_model_train"):
    # img_name示例：07670ff76fc14ab496b0dd411a33ac95-6.webp
    host = "10.101.34.227"  # 服务器ip地址
    port = 62222  # 端口号
    username = "root"  # ssh 用户名
    password = "QianDuoDuoJddH201~~~"  # 密码

    date = datetime.datetime.now().strftime('%Y-%m-%d')

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(host, port, username, password)
    scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)
    local_path = file_path + "/" + date + "/" + model_name
    try:
        scpclient.put(local_path, remote_path)
    except FileNotFoundError as e:
        print(e)
        print("系统找不到指定文件" + local_path)
    else:
        print("文件上传成功")
    ssh_client.close()

if __name__ == '__main__':
    upload_img("lightgbm_model_20210311.txt")
