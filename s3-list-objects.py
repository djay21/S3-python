import boto3
import json
# from pprint import pprint
import logging
from botocore.exceptions import NoCredentialsError, ClientError

def list_objects(bucket_name):
    """
        * Function Objective: Function to find the details of all the objects present in a specified bucket in S3.
        * Parameter bucket_name: Name of the Bucket whose objects list is to be fetched.
        * Return: Function returns a dictionary containing details of all the objects present in a specified bucket in S3.
    """
    ACCESS_KEY="EF849BDKGO395RFW"
    SECRET_KEY="DWEJR340FJM340IGVMLWF"
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, endpoint_url="https://aws.io")  
    try:
        print("\nFetching List of Objects present in a specific Bucket...")
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        if response['KeyCount'] > 0:
            objects = [object['Key'] for object in response['Contents']]
            print("List of Objects: ", objects)
        return response
    except NoCredentialsError:
        print("Credentials not available.")
        return
    except ClientError as e:
        print("Error: ", e)
        return

bucket_name="mybucket"
objects = list_objects(bucket_name)
# pprint(objects)
d=objects['Contents']
print(d)
for obj in d:
    s=str(obj['Key']) + "    " + str(obj['Size']/float(1000000)) + " MB"
    print(s)# print(objects)
# if objects['KeyCount'] != 0:
#     print("List of objects and the response is: \n", objects)
# else:
#     print("There is no object present in the bucket. The response is: \n", objects)
