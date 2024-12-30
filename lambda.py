import json
import logging

# Set up CloudWatch logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # Log the received event
    logger.info(f"Received event: {json.dumps(event)}")

    # Your function logic here
    message = "Hello from Lambda!"

    # Log the result
    logger.info(f"Function result: {message}")

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }