import os
from google.cloud import storage
from google.cloud import secretmanager

#project_id = "os.environ["GCP_PROJECT"]"

def get_secret(name):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{name}/versions/latest"
    response = client.access_secret_version(name=name)
    my_secret_value = response.payload.data.decode("UTF-8")
    return my_secret_value




def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

def secret_hello(request):
    secret = get_secret("brey")
    username = get_secret("pg_pass")
    password = get_secret("tname")
    print("helskjcbjhbwbkjxbkjwed",secret, username, password)
    dd=upload_blob("redis-bucket","requirements.txt","dheeru.txt")
    print(dd)
    return "helloworl"

