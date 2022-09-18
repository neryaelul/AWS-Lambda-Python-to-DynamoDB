# CloudZone Test - Nerya Elul 

Hello dear friends!

My name is Nerya, 

And this is my test for the CloudZone Company, 
A connection between **AWS** tools: **Lambda, API Gateway, Dynamodb**

I also Put the class file, and put the full code of Lambda function

## Installation

Get customersDB Class To Your Code and put your DynamoDB Table

```bash
customers = customersDB('MyTable')
```

## API Examples
### Header Authorization 
```
Authorization: neryanerya
```
### GET - Check Id
#### URL
```https://s73edk94da.execute-api.eu-west-1.amazonaws.com/default/server```

#### Params
```id: MyId```

#### Example Request: 
```https://s73edk94da.execute-api.eu-west-1.amazonaws.com/default/server?id=MyId```

#### Example Response
```
{
    "code": 302,
    "status": "OK",
    "message": "This User exist"
}
```

### PUT - Add New
#### Example Request
#### URL 
```https://s73edk94da.execute-api.eu-west-1.amazonaws.com/default/server```
#### Body
```
{
  "tasktype": "create",
  "data": {
    "id": "MyNewId"
  }
}
```
#### Example Response
```
{
    "code": 200,
    "status": "OK",
    "message": "New User Id adding successfully"
}
```

#### By Nerya Elul

