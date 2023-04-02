from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_sns as _sns,
    aws_apigateway as apigw
    # aws_sqs as sqs,
)
from constructs import Construct

class LambdaApigwSnsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        api_lambda = _lambda.Function(
            self, 'apiLambda',
            
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('src'),
            handler='apiLambda.handler',
        )
        
        api = apigw.RestApi(self,"broker-api")
        # v1 = api.root.add_resource("v1")
        # echo = api.root.add_resource("echo")
        lambda_method = api.root.add_resource("lambda")
        api_lambda_method = lambda_method.add_method("GET",apigw.LambdaIntegration(api_lambda),api_key_required=True)

        plan = api.add_usage_plan(
            "UsagePlan",
            name="Easy",
            throttle=apigw.ThrottleSettings (
            rate_limit=10,
            burst_limit=2
            )
        )
        key=api.add_api_key("ApiKey")
        plan.add_api_key(key)
        


        


        
