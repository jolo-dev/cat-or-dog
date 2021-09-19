import json
from model import predict


def what_animal(event, context):
    print(event)
    # payload = json.loads(event["body"])
    body = event.get("body")
    image_path = json.loads(body).get("image_path")
    result = predict(image_path)
    body = {"result": result}

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

