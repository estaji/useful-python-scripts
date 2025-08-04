from minio import Minio
from minio.error import S3Error

client = Minio("storage.myminio.com",
    access_key="MyAccessKey",
    secret_key="MyStr0ng$ecreT",
)

bucket_name = "mybucket"

try:
    total_size = 0
    file_count = 0

    objects = client.list_objects(bucket_name, recursive=False)

    for obj in objects:
        try:
            total_size += obj.size
            file_count += 1
        except TypeError:
            print("An error skipped...")
            pass

    if file_count > 0:
        average_size = total_size / file_count
        print(f"Average file size: {average_size:.2f} bytes in {bucket_name}")
    else:
        print("No files found in the bucket.")

except S3Error as e:
    print("An error occurred:", e)