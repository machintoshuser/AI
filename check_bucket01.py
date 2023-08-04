from botocore.client import ClientError

try:
    s3.meta.client.head_bucket(Bucket=bucket.name)
except ClientError:
    print('bucket does not exists')