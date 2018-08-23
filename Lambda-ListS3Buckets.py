def lambda_handler(event, context):
    import boto3, os

    myS3 = boto3.client('s3')
    try:
    	results = myS3.list_buckets()
    	print (results)
    	output = ""
    	for bucket in results['Buckets']:
    		output = output + bucket['Name'] + "<br>"
    	print("<h1><font color=green>S3 Bucket List:</font></h1><br><br>" + output)
    except:
    	print("<h1><font color=red>Error!</font></h1><br><br>")
