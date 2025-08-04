from minio import Minio
from minio.error import S3Error
import humanize

# === Configuration ===
BUCKET_NAME = "mybucket"
TEXT_FILE_PATH = "myfile.txt"  # each line = file name (object name)

minio_client = Minio(
    "storage.myminio.com",      # without http:// or https://
    access_key="MyAccessKey",
    secret_key="MyStr0ng$ecreT",
    secure=True                # Use HTTPS
)

# === Main logic ===
def main():
    total_size = 0
    counter = 0

    with open(TEXT_FILE_PATH, 'r') as file:
        for line in file:
            object_name = line.strip()
            if not object_name:
                continue

            counter += 1
            try:
                stat = minio_client.stat_object(BUCKET_NAME, object_name)
                size = stat.size
                total_size += size
                print(f"{counter:>3}. {object_name} - {humanize.naturalsize(size)}")
            except S3Error as e:
                print(e)
                print(f"{counter:>3}. {object_name} - NOT FOUND")

    print("\nTotal files processed:", counter)
    print("Total size:", humanize.naturalsize(total_size))

if __name__ == "__main__":
    main()
