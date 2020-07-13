from os import environ
import boto3

sqs = boto3.client('sqs')

queue_url = f"https://sqs.us-east-1.amazonaws.com/%s/%s-%s-output.fifo" % (environ["USER_ID"], environ["CLIENT_ID"], environ["RUN_ID"])

if __name__ == "__main__":
    count = 0
    while True:
        line = input()
        print("out: ", line)
        if len(line) > 0:
            count += 1
            sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=line,
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
