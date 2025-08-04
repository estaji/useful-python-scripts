from minio import Minio

client = Minio("storage.myminio.com",
    access_key="MyAccessKey",
    secret_key="MyStr0ng$ecreT",
)

try:
    response = client.get_object("mybucket", "object_name")
    print(response.data)
finally:
    response.close()
    response.release_conn()