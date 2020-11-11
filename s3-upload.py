import boto3
import logging
from botocore.exceptions import NoCredentialsError, ClientError


def upload_to_aws(local_file_name, bucket_name, s3_file_name, ACCESS_KEY, SECRET_KEY):
    # If S3 object_name was not specified, use file_name
    if s3_file_name is None:
        s3_file_name = local_file_name

    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, endpoint_url="https://aws.io")

    try:
        response = s3_client.upload_file(local_file_name, bucket_name, s3_file_name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except ClientError as e:
        logging.error(e)
        return False


uploaded = upload_to_aws("package.json", "mybucket", "sample.txt", "EF849BDKGO395RFW", "DWEJR340FJM340IGVMLWF")


# # Alternate Method:


# s3 = boto3.client('s3')
# with open("cloud_computing.png", "rb") as f:
#     s3.upload_fileobj(f, "bucket-permissions-test", "test-file")


# # Alternate Method:


# ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX'
# SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# client = boto3.client(
#     's3',
#     aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY,
#     aws_session_token=SESSION_TOKEN,
# )

# # Or via the Session
# session = boto3.Session(
#     aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY,
#     aws_session_token=SESSION_TOKEN,
# )

