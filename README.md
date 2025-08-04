# About
It is a group of **useful python scripts** for DevOps engineers, System administrators, and developers.

# How
Each directory has a different purpose and scripts are not related to each other.
Find a useful one from this readme file then use it.

# List
+ upload-backup-to-S3-bucket
+ get-report-from-MInIO

### upload-backup-to-S3-bucket
Easily upload a file to an S3 bucket like Arvan cloud bucket using script.py script.

```
python script.py FULL_FILE_PATH FILE_NAME
```

### get-report-from-MInIO
This is a group of readily scripts to get report and search in a MinIO cluster.

Includes:
+ check-file-existence
+ list-files-to-csv (list all objects info into a csv file)
+ total-size-reporter (read a list of objects from a file and sum their sizes)
+ find-large-objects (Find all objects larger than a threshold_size)
+ find-average-size-of-files (in a bucket)