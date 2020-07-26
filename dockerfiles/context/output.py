from os import environ
import boto3

sqs = boto3.client('sqs')

queue_url = f"https://sqs.us-east-1.amazonaws.com/%s/%s-%s-output.fifo" % (environ["USER_ID"], environ["CLIENT_ID"], environ["RUN_ID"])
box_suffix = "-boxed"

if __name__ == "__main__":
    count = 0
    while True:
        line = input()
        print("out: ", line)
        count += 1
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=line+box_suffix,
            MessageAttributes={
                "client": {
                    "StringValue": environ["CLIENT_ID"],
                    "DataType": "String"
                },
                "containerId": {
                    "StringValue": environ["RUN_ID"],
                    "DataType": "String"
                }
            },
            MessageDeduplicationId=str(count),
            MessageGroupId="ProgramOutput"
        )
