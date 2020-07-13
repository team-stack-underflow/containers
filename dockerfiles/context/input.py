from os import environ
import boto3

sqs = boto3.client('sqs')

queue_url = f"https://sqs.us-east-1.amazonaws.com/%s/%s-%s-input.fifo" % (environ["USER_ID"], environ["CLIENT_ID"], environ["RUN_ID"])

if __name__ == "__main__":
    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            WaitTimeSeconds=5
        )
        if "Messages" in response:
            messages = response["Messages"]
            for msg in messages:
                print(msg["Body"], flush=True)
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=msg["ReceiptHandle"]
                )


