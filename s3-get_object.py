import boto3
import logging
from botocore.exceptions import NoCredentialsError, ClientError


def get_object(bucket_name, object_name):
    """
        * Function Objective: Function to fetch the contents of a particular object present in the specified bucket.
        * Parameter bucket_name: Name of the Bucket in which the object to be fetched is present.
        * Parameter object_name: Name of the object to be fetched from the specified bucket.
        * Return: Function returns the object present in the specified bucket (if present), else None
    """
    ACCESS_KEY="EF849BDKGO395RFW"
    SECRET_KEY="DWEJR340FJM340IGVMLWF"
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, endpoint_url="https://aws.io") 
    try:
        print("\nFetching the specified Object present in the specified Bucket...")
        response = s3_client.get_object(Bucket=bucket_name, Key=object_name)
        print("Response: \n", response)
        return response
    except NoCredentialsError:
        print("Credentials not available.")
        return
    except ClientError as e:
        print("Error: ", e)
        return
object_name="ChromeSetup.exe"
bucket_name="mybucket"
object = get_object(bucket_name, object_name)
# if object is None:
#     print("Cannot fetch the object from the given bucket due to some error.")
# else:
#     print("The contents of the object present in the specified bucket: \n", object)
