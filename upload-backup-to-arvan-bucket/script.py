import boto3
import logging
import sys
from datetime import datetime
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)

# Variables
backup_file_path = sys.argv[1]
backup_file_name = sys.argv[2]
bucket_name = 'BUCKET_NAME'
bucket_endpoint_url = 'https://s3.ir-thr-at1.arvanstorage.ir'
bucket_access_key = 'ACCESS_KEY'
bucket_secret_key = 'SECRET_KEY'
remove_files_older_than = 40

# Functions
def upload_bak():
    try:
       s3_resource = boto3.resource(
           's3',
           endpoint_url = bucket_endpoint_url,
           aws_access_key_id = bucket_access_key,
           aws_secret_access_key = bucket_secret_key
       )
    
    except Exception as exc:
       logging.error(exc)
    else:
       try:
           bucket = s3_resource.Bucket(bucket_name)
           file_path = backup_file_path
           object_name = backup_file_name
    
           with open(file_path, "rb") as file:
               bucket.put_object(
                   ACL='private',
                   Body=file,
                   Key=object_name
               )
       except ClientError as e:
           logging.error(e)

def remove_old_files():
    try:
       client = boto3.client(
           's3',
           endpoint_url = bucket_endpoint_url,
           aws_access_key_id = bucket_access_key,
           aws_secret_access_key = bucket_secret_key,
       )    

       response = client.list_objects(Bucket=bucket_name)

       today_date_time = datetime.now().replace(tzinfo=None)

       for file in response.get("Contents"):
           file_name = file.get("Key")
           modified_time = file.get("LastModified").replace(tzinfo=None)
                
           difference_days_delta = today_date_time - modified_time
           difference_days = difference_days_delta.days
           if difference_days > remove_files_older_than:
               client.delete_object(Bucket=bucket_name,Key=file_name)

    except Exception as exc:
       logging.error(exc)


# Main
upload_bak()
remove_old_files()
