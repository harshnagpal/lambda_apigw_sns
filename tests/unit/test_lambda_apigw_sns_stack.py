import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_apigw_sns.lambda_apigw_sns_stack import LambdaApigwSnsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_apigw_sns/lambda_apigw_sns_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaApigwSnsStack(app, "lambda-apigw-sns")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
