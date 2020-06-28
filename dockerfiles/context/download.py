from os import environ
import boto3

sqs = boto3.client('sqs')

queue_url = f"https://sqs.us-east-1.amazonaws.com/%s/%s-src" % (environ["USER_ID"], environ["RUN_ID"])

if __name__ == "__main__":
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )
    msg = response["Messages"][0]
    with open(environ["SRC_FILE"], "w") as src:
        src.write(msg["Body"])
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=msg["ReceiptHandle"]
    )
