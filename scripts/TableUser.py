import boto3
from configparser import ConfigParser
from schema.UserSchema import UserSchema

config = ConfigParser()
config.read('../config.ini')
environment = config.get('DEFAULT', 'enviroment')

# DYNAMO CREDENTIALS
region = config.get('DYNAMODB', 'region')
url = config.get('DYNAMODB', 'url')
acceskey = config.get('DYNAMODB', 'accesskey')
secretkey = config.get('DYNAMODB', 'secretkey')

dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=url, aws_access_key_id=acceskey, aws_secret_access_key=secretkey)
table = UserSchema().table

if environment:
    table = table + '_' + environment

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName= table,
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
#table.meta.client.get_waiter('table_exists').wait(TableName=table)

# Print out some data about the table.
print(table.item_count)