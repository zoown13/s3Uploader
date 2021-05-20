from chalice import Chalice
import boto3

app = Chalice(app_name='s3Uploader')

client = boto3.client('s3')

@app.route('/uploads/{name}', cors=True)
def uploads(name):
    url = client.generate_presigned_url('put_object', Params= {'Bucket': "media-query-mediabucket-1i4slys4cekco",
                                                        "Key": name, "ContentType": 'image/jpeg'},
                                                         ExpiresIn=300)
                                                    
    return {'uploadUrl': url}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
