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
