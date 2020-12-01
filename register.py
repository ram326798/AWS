import json
import boto3
import logging

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')
def lambda_handler(event, context):

    result = table.get_item(
        Key={
            'username': event['username']
        }
    )
    if 'Item' not in result:
        response=table.put_item(Item=event)
        return {
        'statusCode': 200,
        "message":"User Registered Successfully"
    }
    else:
        response={"output":"user already exists"}
        
    return response
