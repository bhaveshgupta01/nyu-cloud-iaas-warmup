import boto3
import os

# 1. Configuration
BUCKET_NAME = 'nyu-cloud-warmup-bg2896-2025' 
FILE_NAME = 'assignment_data.txt'

# 2. Create a dummy file locally
with open(FILE_NAME, 'w') as f:
    f.write("Hello NYU! This file was created on EC2 and uploaded to S3.")

# 3. Initialize S3 Client
s3 = boto3.client('s3')

try:
    print(f"Uploading {FILE_NAME} to bucket {BUCKET_NAME}...")
    s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
    print("Upload Successful!")

    print("\nVerifying by listing bucket contents:")
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f"- {obj['Key']} (Size: {obj['Size']} bytes)")
    else:
        print("Bucket is empty.")

except Exception as e:
    print(f"Error: {e}")
