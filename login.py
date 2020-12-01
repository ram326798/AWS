import json
import boto3  
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    print(event)
    response = table.scan(FilterExpression=Attr('username').eq(event['username']) & Attr('password').eq(event['password'])  )
    print(response['Count'])
    if response['Count'] == 0:
        return(" user not found")
    else:
        return {
            'statusCode': 200,
            'body': json.dumps("Login successful")
        }
