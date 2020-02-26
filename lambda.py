import json, boto3

def lambda_handler(event, context):
    
    client = boto3.client('iam')
    response = client.list_users()
    print ("Full output returned by api call:")
    print (response)
    print ("Formatted response:")
    for item in response["Users"]:
        print('{} has the arn {}'.format(item["UserName"],item["Arn"]))
    return True