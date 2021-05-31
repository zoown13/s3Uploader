from chalice import Chalice
import boto3

app = Chalice(app_name='s3Uploader')

client = boto3.client('s3')

@app.route('/uploads/{name}', cors=True)
def uploads(name):
    url = client.generate_presigned_url('put_object', Params= {'Bucket': "media-query-mediabucket-1i4slys4cekco",
                                                        "Key": name, "ContentType": 'image/jpeg'},
                                                         ExpiresIn=300)
    if name in url:
        index = url.find(name)
        url = url[index-1:]
                                                    
    return url                                                
