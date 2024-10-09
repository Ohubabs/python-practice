import boto3


def ec2_describe():

    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    #for instance in response['InstanceId']:
    print(response)

ec2_describe()

---
import boto3
import json

def ec2_describe():

    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['running']}])
    for reservation in response['Reservations']:
        for instances in reservation['Instances']:
             instance_id = instances.get('InstanceId')
    print(instance_id)

ec2_describe()
