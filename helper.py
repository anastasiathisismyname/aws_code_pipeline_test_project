import json


def get_event(path):
    with open(path) as f:
        return json.dumps(json.load(f))


def get_event_content(path):
    with open(path) as f:
        return json.load(f)


def get_aws_access_key_id(path):
    with open(path) as f:
        return f.read().split('\n')[0]


def get_aws_secret_access_key(path):
    with open(path) as f:
        return f.read().split('\n')[1]
