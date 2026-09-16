import json
import boto3
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from moto import mock_aws
from lambda_function import lambda_handler


@mock_aws
def test_lambda_increments_count():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='visitor-count',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    table.put_item(Item={'id': '1', 'count': 0})

    event = {'httpMethod': 'GET'}
    context = {}
    response = lambda_handler(event, context)

    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['count'] == 1