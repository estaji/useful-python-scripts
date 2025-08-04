from minio import Minio
from minio.error import S3Error

client = Minio("storage.myminio.com",
    access_key="MyAccessKey",
    secret_key="MyStr0ng$ecreT",
)

bucket_name = "mybucket"

try:
    threshold_size = 17000000 #17MB

    for obj in client.list_objects(bucket_name, recursive=False):
        try:
            if obj.size > threshold_size:
                print(obj)
                print(obj.object_name)
                print(obj.last_modified)
                print(obj.size)
                print("==============================")
        except TypeError:
            print("An error skipped...")
            pass


except S3Error as e:
    print("An error occurred:", e)
