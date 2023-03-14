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


        
