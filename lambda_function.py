import json
import boto3
from cdb import customersDB 
def lambda_handler(event, context):
    
   
        customers = customersDB('customers')
        
        if event and event['httpMethod']:
            Authorization = event['headers'].get('Authorization', None)
            if Authorization != None and event['headers']['Authorization'] == 'test':
                
                if event['httpMethod'] == "PUT":
                    bodyJson2Arr = json.loads(event['body'])
                    if bodyJson2Arr['tasktype'] == "create":
                        if bodyJson2Arr['data']['id']:
                            exist = customers.get(bodyJson2Arr['data']['id'])
                            message = exist
                            if not exist:
                                customers.create(bodyJson2Arr['data']['id'])
                                statusCode = 200
                                resTypeStatus = 'OK'
                                message = 'New User Id adding successfully'
                            else:
                                statusCode = 302
                                resTypeStatus = 'OK'
                                message = 'Sorry but this User alredy exist'
                        else:
                            statusCode = 419
                            resTypeStatus = 'MISSING ARGUMENTS'
                            message = 'Sorry but not found any Id in your request'
                    else:
                        statusCode = 419
                        resTypeStatus = 'MISSING ARGUMENTS'
                        message = 'Sorry but not found any Create in your request'
                        
                elif event['httpMethod'] == 'GET':
                    id = event['multiValueQueryStringParameters'].get('id', None)
                    if id == None:
                        statusCode = 419
                        resTypeStatus = 'MISSING ARGUMENTS'
                        message = 'Sorry but not found any Id in your request'
                    else:    
                        if customers.get(event['multiValueQueryStringParameters']['id'][0]):
                            statusCode = 302
                            resTypeStatus = 'OK'
                            message = 'This User exist'
                        else:
                            statusCode = 404
                            resTypeStatus = 'OK'
                            message = 'This User not found ):'
                else:
                    statusCode = 405
                    message= 'This method type is not currently supported.'
                    resTypeStatus = 'METHOD NOT ALLOWED'
            else:
                statusCode = 403
                message= 'Failed to pass authorization.'
                resTypeStatus = 'Forbidden'
    
        jsonDataBody = {'code': statusCode, 'status': resTypeStatus,'message': message}
    
        return {
            'headers': {
                "content-type":"application/json"
            },
            'statusCode': statusCode,
            'body': json.dumps(jsonDataBody)
        }
