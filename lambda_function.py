import json
import boto3

def lambda_handler(event, context):
    ses = boto3.client('ses', region_name='eu-west-2')
    
    body = json.loads(event['body'])
    name = body.get('name', 'Unknown')
    email = body.get('email', 'Unknown')
    message = body.get('message', 'No message')
    
    ses.send_email(
        Source='YOUR_VERIFIED_EMAIL@gmail.com',
        Destination={'ToAddresses': ['YOUR_VERIFIED_EMAIL@gmail.com']},
        Message={
            'Subject': {'Data': f'New enquiry from {name}'},
            'Body': {
                'Text': {
                    'Data': f'Name: {name}\nEmail: {email}\nMessage: {message}'
                }
            }
        }
    )
    
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'message': 'Email sent successfully'})
    }
