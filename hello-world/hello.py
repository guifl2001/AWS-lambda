import json

def handler(event, context):
    print('Event:', event)
    response_message = 'Hello, World!'

    if 'queryStringParameters' in event and 'Name' in event['queryStringParameters']:
        response_message = 'Hello, ' + event['queryStringParameters']['Name'] + '!'

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': response_message
        })
    }
