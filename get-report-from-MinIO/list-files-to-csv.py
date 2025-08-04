from minio import Minio
from minio.error import S3Error
import csv

client = Minio("storage.myminio.com",
    access_key="MyAccessKey",
    secret_key="MyStr0ng$ecreT",
)

bucket_name = "mybucket"
file_path = 'myobjects.csv'

try:
    for obj in client.list_objects(bucket_name, recursive=True):
        try:
                # print(obj.object_name)
                # print(obj.last_modified)
                # print(obj.size)
                # print("==============================")

                new_data = [
                    [obj.object_name, obj.last_modified, obj.size],
                ]

                with open(file_path, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(new_data)

        except TypeError:
            print("An error skipped...")
            pass

except S3Error as e:
    print("An error occurred:", e)
