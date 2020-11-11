import boto3
import logging
from botocore.exceptions import NoCredentialsError, ClientError
from credentials import Credentials




def list_buckets():
    """
        * Function Objective: Function to find the details of all the buckets owned by the authenticated sender of the request present in S3.
        * Return: Function returns a dictionary containing details of all the buckets.
    """
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
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


def upload_file(local_file, bucket_name, object_name):
    """
        * Function Objective: Upload an object to a particular S3 bucket.
        * Parameter local_file: Path of the Local file to be uploaded in the specified bucket.
        * Parameter bucket_name: Name of the Bucket in which the file needs to be uploaded.
        * Parameter object_name: Name of the object which is going to be created in the bucket.
        * Return: Function returns True if the file is uploaded successfully, else False.
    """
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        print("\nUploading a local file as a new object to S3...")
        s3_client.upload_file(local_file, bucket_name, object_name)
        return True
    except FileNotFoundError:
        print("The file was not found.")
        return False
    except NoCredentialsError:
        print("Credentials not available.")
        return False
    except ClientError as e:
        print("Error: ", e)
        return False


def list_objects(bucket_name):
    """
        * Function Objective: Function to find the details of all the objects present in a specified bucket in S3.
        * Parameter bucket_name: Name of the Bucket whose objects list is to be fetched.
        * Return: Function returns a dictionary containing details of all the objects present in a specified bucket in S3.
    """
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
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


def get_object(bucket_name, object_name):
    """
        * Function Objective: Function to fetch the contents of a particular object present in the specified bucket.
        * Parameter bucket_name: Name of the Bucket in which the object to be fetched is present.
        * Parameter object_name: Name of the object to be fetched from the specified bucket.
        * Return: Function returns the object present in the specified bucket (if present), else None
    """
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
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


def download_file(local_file, bucket_name, object_name):
    """
        * Function Objective: Download an object from a particular S3 bucket.
        * Parameter local_file: Name of the Local file to be created to store the contents of the downloaded object
        * Parameter bucket_name: Name of the Bucket in which the object to be downloaded is present.
        * Parameter object_name: Name of the object which needs to be downloaded from the bucket
        * Return: Function returns True if the object is downloaded successfully, else False
    """

    if local_file is None:
        local_file = object_name

    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        print("\nDownloading an object from S3...")
        s3.Bucket(bucket_name).download_file(object_name, local_file)
        return True
    except NoCredentialsError:
        print("Credentials not available.")
        return False
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            print("Error: ", e)
        return False


def delete_object(bucket_name, object_name):
    """
        * Function Objective: Function to delete a particular object present in the specified bucket.
        * Parameter bucket_name: Name of the Bucket in which the object to be deleted is present.
        * Parameter object_name: Name of the object to be deleted from the specified bucket.
        * Return: Function returns True if object is deleted successfully, else False
    """
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        print("\nDeleting the specified Object from the given Bucket...")
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except ClientError as e:
        print("Error: ", e)
        return False


def delete_objects(bucket_name, object_names):
    """
        * Function Objective: Function to delete a list of objects present in the specified bucket.
        * Parameter bucket_name: Name of the Bucket in which the objects to be deleted are present.
        * Parameter object_names: List of the objects to be deleted from the specified bucket.
        * Return: Function returns True if all the objects are deleted successfully, else False
    """
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    objlist = [{'Key': obj} for obj in object_names]
    try:
        print("\nDeleting the list of Objects specified from the given Bucket...")
        s3_client.delete_objects(Bucket=bucket_name, Delete={'Objects': objlist})
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except ClientError as e:
        print("Error: ", e)
        return False


def delete_bucket(bucket_name):
    """
        * Function Objective: Delete a specific bucket present in S3 bucket.
        * Parameter bucket_name: Name of the Bucket to be deleted.
        * Return: Function returns True if the bucket is deleted successfully, else False
    """
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        print("\nDeleting the specified Bucket from S3...")
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if response['KeyCount'] > 0:
            print("The bucket you tried to delete is not empty.")
            return False
        s3_client.delete_bucket(Bucket=bucket_name)
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except ClientError as e:
        logging.error(e)
        return False


if __name__ == "__main__":

    bucket_name = "random-named"
    object_name = "my-first-object"
    object_names = ["my-first-object", "my-second-object"]
    local_file = "./cloud_computing.png"
    region = "us-west-2"

    cred = Credentials("<ACCESS_KEY_HERE>", "<SECRET_KEY_HERE>")
    ACCESS_KEY, SECRET_KEY = cred.get_credentials()


    # Creating Bucket

    if create_bucket(bucket_name):
        print("Bucket has been created successfully.")
    else:
        print("Bucket wasn't created due to some error.")

    if create_bucket(bucket_name, region):
        print("Bucket has been created successfully.")
    else:
        print("Bucket wasn't created due to some error.")


    # Listing Buckets

    buckets = list_buckets()
    if len(buckets['Buckets']) != 0:
        print("List of buckets and the response is: \n", buckets)
    else:
        print("There is no Bucket present in S3. The response is: \n", buckets)


    # Uploading a file to a specific Bucket

    if upload_file(local_file, bucket_name, object_name):
        print("File has been uploaded successfully.")
    else:
        print("File wasn't uploaded.")


    # Listing Objects present in a specific Bucket

    objects = list_objects(bucket_name)
    if objects['KeyCount'] != 0:
        print("List of objects and the response is: \n", objects)
    else:
        print("There is no object present in the bucket. The response is: \n", objects)

    # Fetching an object present in a specific Bucket

    object = get_object(bucket_name, object_name)
    if object is None:
        print("Cannot fetch the object from the given bucket due to some error.")
    else:
        print("The contents of the object present in the specified bucket: \n", object)


    # # Downloading a file from a specific Bucket
    #
    # if download_file(None, bucket_name, object_name):
    #     print("Object has been downloaded successfully.")
    # else:
    #     print("Object wasn't downloaded.")


    # # Deleting an object present in the bucket
    #
    # if delete_object(bucket_name, object_name):
    #     print("Object has been deleted successfully.")
    # else:
    #     print("Object can't be deleted due to some error.")


    # # Deleting a list of objects present in the bucket
    #
    # if delete_objects(bucket_name, object_names):
    #     print("All the objects have been deleted successfully.")
    # else:
    #     print("Objects can't be deleted due to some error.")


    # # Deleting a Bucket
    #
    # if delete_bucket(bucket_name):
    #     print("Bucket has been deleted successfully.")
    # else:
    #     print("Bucket can't be deleted due to some error.")
