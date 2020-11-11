import boto3
import logging
from botocore.exceptions import NoCredentialsError, ClientError


def download_to_aws(local_file_name, bucket_name, s3_file_name, ACCESS_KEY, SECRET_KEY):
    # If local file name was not specified, use S3 object_name
    if local_file_name is None:
        local_file_name = s3_file_name

    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, endpoint_url="https://aws.io")

    try:
        s3.Bucket(bucket_name).download_file(s3_file_name, local_file_name)
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            logging.error(e)
        return False


downloaded = download_to_aws(None, "mybucket", "ChromeSetup.exe", "EF849BDKGO395RFW", "DWEJR340FJM340IGVMLWF")


# # Alternate Method:

# s3 = boto3.client('s3')
# with open('FILE_NAME', 'wb') as f:
#     s3.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)
