# CloudZone Test - Nerya Elul 

Hello Dear Freinds!

My name is Nerya, 

And this is my test for the CloudZone company, 
A connection between **AWS** tools: **Lambda, API Gateway, Dynamodb**

I also Put the class file, and put the full code of Lambda function

## Installation

Get customersDB Class To Your Code and put your DynamoDB Table like this

```bash
customers = customersDB('MyTable')
```

## API Request Example
### Header Authorization 
```
Authorization: neryanerya
```
### GET - Check Id
#### Example Request
```
id=MyId
```

#### URL: ```
https://s73edk94da.execute-api.eu-west-1.amazonaws.com/default/server?id=MyId```
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
### URL 
```
https://s73edk94da.execute-api.eu-west-1.amazonaws.com/default/server
```
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

### By Nerya Elul

