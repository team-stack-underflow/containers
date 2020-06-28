from os import environ
import boto3
import subprocess

sqs = boto3.client('sqs')

queue_url = f"https://sqs.us-east-1.amazonaws.com/%s/%s-output.fifo" % (environ["USER_ID"], environ["RUN_ID"])

if __name__ == "__main__":
    compile = subprocess.run(environ["COMPILE_CMD"].split(), capture_output=True, text=True)
    if compile.returncode != 0:
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=compile.stderr,
            MessageAttributes={
                "client": {
                    "StringValue": environ["RUN_ID"],
                    "DataType": "String"
                }
            },
            MessageDeduplicationId="CompileError",
            MessageGroupId="CompileError"
        )
    exit(compile.returncode)
    