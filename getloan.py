import json
import decimal
import boto3  

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Loans')

def lambda_handler(event, context):
    print(event)
    response = table.get_item(Key={'username': event['username']})
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(response['Item'],cls=DecimalEncoder)
        # "message":"Loan Details"
    }

    return response['Item']