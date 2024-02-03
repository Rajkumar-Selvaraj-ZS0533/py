# hello.py

def handler(event, context):
    print("hello world")
    return {"statusCode": 200, "body": "Hello, World!"}
