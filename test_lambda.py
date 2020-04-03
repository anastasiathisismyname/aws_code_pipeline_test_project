import pytest
from lambda_function import *
from pprint import pprint


event = get_event_content(r'C:\Users\Anastasiia_Pyrih\Desktop\New folder\sample.project\aws_code_pipeline_test_project\pipeline_event_ci_env.json')


def test_lambda():

    assert lambda_handler(event, None)["result"] == "passed"