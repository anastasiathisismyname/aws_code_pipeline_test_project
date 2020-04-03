import json
import requests


def lambda_handler(event, context):

    result = "failed"

    env = event["ENV"]

    if env in ["ci", "qa", "dev"]:

        url = event["test_url"]

        if env in ["ci", "dev"]:

            response = requests.get(f"{url}/get")

            if 200 == response.status_code:

                if "args" in json.loads(response.content):

                    result = "passed"

    return {"result": f"{result}"}


if __name__ == "__main__":
    from helper import *
    # aws_access_key_id = get_aws_access_key_id(r'C:\Users\Anastasiia_Pyrih\Desktop\New folder\sample.project\sample.project1\aws_lambda_project\tests\credentials')
    # aws_secret_access_key = get_aws_secret_access_key(r'C:\Users\Anastasiia_Pyrih\Desktop\New folder\sample.project\sample.project1\aws_lambda_project\tests\credentials')
    # session = boto3.Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    event = get_event_content(
        r'C:\Users\Anastasiia_Pyrih\Desktop\New folder\sample.project\aws_code_pipeline_test_project\pipeline_event_ci_env.json')
    assert lambda_handler(event, None)["result"] == "passed"