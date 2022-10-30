from nie.ss.minio import MinioClient
from loguru import logger


client = MinioClient(
    end_point='192.168.31.245:9000',
    access_key='ponponon',
    secret_key='ponponon',
    bucket_name='nie',
)

if not client.status.conn.bucket_exists(bucket_name='nie'):
    client.status.conn.make_bucket(bucket_name='nie')

if client.os.path.exists('test/001.txt'):
    with client.open('test/001.txt', 'r', encoding='utf-8') as file:
        logger.debug(file.read())
else:
    with client.open('test/001.txt', 'w', encoding='utf-8') as file:
        file.write('nie project is good')
