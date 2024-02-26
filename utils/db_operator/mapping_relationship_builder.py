import os
import sys
import sqlacodegen.main
from loguru import logger

from utils import config

# 生成models文件到models文件夹下
if __name__ == '__main__':

    username = config.get('mysql', 'MYSQL_USERNAME')
    password = config.get('mysql', 'MYSQL_PASSWORD')
    host = config.get('mysql', 'MYSQL_HOST')
    port = config.get('mysql', 'MYSQL_PORT')
    database = config.get('mysql', 'MYSQL_DATABASE')

    output_file_path = "../../models/models.py"
    # 检查文件是否存在，如果不存在则创建
    if not os.path.exists(output_file_path):
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w'):  # 创建空文件
            pass

    # 构造命令字符串
    command = 'sqlacodegen --outfile {} mysql+pymysql://{}:{}@{}:{}/{}'.format(
        output_file_path, username, password, host, port, database
    )

    # order = 'sqlacodegen --noviews --outfile ../../models/models.py mysql+pymysql://{}:{}@{}:{}/{}' \
    #     .format(username, password, host, port, database)

    # 字符处理
    temp = command.split(' ')[1:]
    # genarr = []
    # for a_temp in temp:
    #     if not a_temp == '':
    #         genarr.append(a_temp)
    genarr = [arg for arg in temp if arg]  # 使用列表推导简化
    sys.argv.extend(genarr)
    # 执行创建
    sqlacodegen.main.main()
    # 日志输出
    logger.info(f'映射文件创建完成，地址：models/models.py')
