import boto3

client = boto3.client('s3')

response = client.list_buckets(
    MaxBuckets=2
)

print (response)

---
import boto3

client = boto3.client('s3')

response = client.list_buckets(
    MaxBuckets=2
)

print (response['ResponseMetadata']['HostId'])
