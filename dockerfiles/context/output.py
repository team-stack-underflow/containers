from os import environ
import boto3

sqs = boto3.client('sqs')

queue_url = f"https://sqs.us-east-1.amazonaws.com/%s/%s-output" % (environ["USER_ID"], environ["RUN_ID"])

if __name__ == "__main__":
    while True:
        line = input()
        print("out: ", line)
        if len(line) > 0:
            response = sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=line
            )


