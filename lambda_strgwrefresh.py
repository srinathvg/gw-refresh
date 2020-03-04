import boto3
client = boto3.client('storagegateway')

def lambda_handler(event, context):
    try:
        arns = ['arn:aws:storagegateway:us-east-1:*:share/share-*', 'arn:aws:storagegateway:us-east-1:*:share/share-*', 'arn:aws:storagegateway:us-west-2:949663004247:share/share-6E55640B', 'arn:aws:storagegateway:us-west-2:949663004247:share/share-68936D0C']
        for arn in arns:
            try:
                response = client.refresh_cache(
                    FileShareARN='arn:aws:storagegateway:us-east-2:*:share/share-*'
                )
            except:
                print "Inner exception"
    except:
        print "Other exception"
    # TODO implement
    return 'Hello from Lambda'
