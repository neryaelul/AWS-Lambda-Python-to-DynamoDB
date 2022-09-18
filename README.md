# LambdaCloudZoneTest
# CloudZone TEST - Nerya Elul

Foobar is a Python library for dealing with word pluralization.

## Installation

Get customersDB Class To Your Code and put your DynamoDB Table like this

```bash
customers = customersDB('MyTable')
```

## API Request Example
### GET - Check Id
#### Example Request
```
id=MyId
```

URL: ```
https://j7u5ydav73.execute-api.eu-west-1.amazonaws.com/prod/server?id=MyId```
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
URL: ```
https://j7u5ydav73.execute-api.eu-west-1.amazonaws.com/prod/server```


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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
