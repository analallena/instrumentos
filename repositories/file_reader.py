import boto3
from io import StringIO
import pandas as pd

s3_client = boto3.client('s3')


def read_file(bucket_name, file_name):
    try:
        object_file = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        body = object_file['Body']
        csv_string = body.read().decode('utf-8')
        dataframe = pd.read_csv(StringIO(csv_string))

        return dataframe

    except Exception as err:
        print(err)

        # TODO implement
