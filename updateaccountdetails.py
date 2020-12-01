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
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    # TODO implement

    response = table.update_item(Key={'username': event['username']},
        ExpressionAttributeNames={
            '#state':'state'
        },
        ExpressionAttributeValues={
          ':state': event['state'],
          ':accounttyped':event['accountType'],
            ':addressd':event['address'],
            ':contactd':event['contactNo'],
            ':countryd':event['country'],
            ':DOBd':event['DOB'],
            ':emaild':event['emailAddress'],
            ':pand':event['pan'],
        },
        UpdateExpression='SET #state = :state,accountType=:accounttyped, address=:addressd, contactNo=:contactd, country=:countryd, DOB=:DOBd, emailAddress=:emaild, pan=:pand', 
        ReturnValues='ALL_NEW',)

    response = {
        "statusCode": 200,
        "body": json.dumps(response['Attributes'],cls=DecimalEncoder),
        "message":"User Details updated"
    }

    return response