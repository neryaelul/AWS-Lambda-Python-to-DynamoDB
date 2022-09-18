import json
import boto3

class customersDB:
    def __init__(self,dynamoDBTable):
        self.client = boto3.resource('dynamodb')
        self.tableDynamoDB = dynamoDBTable
        self.table = self.client.Table(self.tableDynamoDB)
    def get(self,CustomerId):
        response = self.table.get_item(
            Key={
                'id': CustomerId
            }
        )
        if 'Item' in response:
            return True
        else:
            return False
    def create(self,CustomerId):
        self.table.put_item(
                Item={
                    'id': CustomerId
                }
            )
        return True

def lambda_handler(event, context):
    customers = customersDB('customers_ids')

    if event and event['httpMethod']:
        if event['httpMethod'] == "PUT":
            bodyJson2Arr = json.loads(event['body'])
            if bodyJson2Arr['tasktype'] == "create":
                if bodyJson2Arr['data']['id']:
                    exist = customers.get(bodyJson2Arr['data']['id'])
                    message = exist
                    if not exist:
                        customers.create(bodyJson2Arr['data']['id'])
                        statusCode = 200
                        code = 200
                        resTypeStatus = 'OK'
                        message = 'New User Id adding successfully'
                    else:
                        statusCode = 302
                        resTypeStatus = 'OK'
                        code = 302
                        message = 'Sorry but this User alredy exist'
                else:
                    statusCode = 419
                    code = 419
                    resTypeStatus = 'MISSING ARGUMENTS'
                    message = 'Sorry but not found any Id in your request'
            else:
                statusCode = 419
                code = 419
                resTypeStatus = 'MISSING ARGUMENTS'
                message = 'Sorry but not found any Create in your request'
                
        if event['httpMethod'] == 'GET':
            if customers.get(event['multiValueQueryStringParameters']['id'][0]):
                statusCode = 302
                code = 302
                resTypeStatus = 'OK'
                message = 'This User exist'
            else:
                statusCode = 404
                code = 404
                resTypeStatus = 'OK'
                message = 'This User not found ):'
            
        jsonDataBody = {'code': code, 'status': resTypeStatus,'message': message}
                  
        return {
            'headers': {
                "content-type":"application/json"
            },
            'statusCode': 200,
            'body': json.dumps(jsonDataBody)
        }
