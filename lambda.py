import logging
import json
import boto3

from repositories.instruments_repo import InstrumentsRepository

# Set up CloudWatch logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    try:
        repository = InstrumentsRepository()
        instruments = repository.get()

        logger.info(instruments)

    except Exception as err:
        print(err)

        # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
