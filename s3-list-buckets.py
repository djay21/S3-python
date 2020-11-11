import boto3
import logging
from botocore.exceptions import NoCredentialsError, ClientError



def list_buckets():
    """
        * Function Objective: Function to find the details of all the buckets owned by the authenticated sender of the request present in S3.
        * Return: Function returns a dictionary containing details of all the buckets.
    """
    ACCESS_KEY="EF849BDKGO395RFW"
    SECRET_KEY="DWEJR340FJM340IGVMLWF"
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, endpoint_url="https://aws.io")
    try:
        print("\nFetching list of buckets present in S3...")
        response = s3_client.list_buckets()

        buckets = [bucket['Name'] for bucket in response['Buckets']]
        print("List of Buckets: ", buckets)
        return response

        # return response
    except NoCredentialsError:
        print("Credentials not available.")
        return
    except ClientError as e:
        print("Error: ", e)
        return


buckets = list_buckets()
if len(buckets['Buckets']) != 0:
    print("List of buckets and the response is: \n", buckets)
else:
    print("There is no Bucket present in S3. The response is: \n", buckets)

