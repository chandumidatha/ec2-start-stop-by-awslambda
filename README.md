# ec2-start-stop-by-awslambda
To start and stop EC2 instances at regular intervals using the AWS Lambda service

## **Step1: Setting Up Lambda IAM Role**
To grant necessary permissions to your Lambda function, follow these steps:

#### Access AWS Management Console:
1. Go to the IAM Service:
2. Navigate to the IAM (Identity and Access Management) service.
#### Create a New Role:
1. Click on "Roles" in the left-hand navigation pane.
2. Click the "Create role" button.
#### Select Lambda as the Service:
1. Choose "Lambda" as the service that will use this role, then click "Next: Permissions".
2. Define Permissions
3. Switch to the "JSON" tab.
#### Replace any existing JSON with the provided IAM policy:

```bash
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Start*",
        "ec2:Stop*"
      ],
      "Resource": "*"
    }
  ]
}
```
## **Step 2: Create Lambda Function**
1. Navigate to Lambda service and create a function.
2. Select "Author from scratch" and provide a function name.
3. Choose Runtime (Python3.9), Architecture (x86_64), and Execution role. Then click "Create function".

## **Step 3: Configure Lambda Function**
Write a Lambda function to start or stop EC2 instances.
Use the appropriate Python code provided below:

EC2 Start Python code:
```bash
import boto3

region = 'ap-south-1'
instances = ['i-12345cb6de4f78g9h', 'i-08ce9b2d7eccf6d26']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('Started your instances: ' + str(instances))
```
EC2 Stop Python code:
```bash
import boto3

region = 'ap-south-1'
instances = ['i-12345cb6de4f78g9h', 'i-08ce9b2d7eccf6d26']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('Stopped your instances: ' + str(instances))
```
Test the Lambda function.

## **Step 4: Schedule Lambda Execution**
1. Go to CloudWatch service and select "Events" under Rules.
2. Create a rule for starting EC2 instances.
   (i) Select "Schedule", set Cron expression, and choose the Lambda function for starting instances.
   (ii) Example: 13 21 ? * MON-SAT * for Monday to Saturday at 09:13 PM.
3. Repeat the same steps to create a rule for stopping EC2 instances.

Additional Notes:

CloudWatch Rules Automation:
1. CloudWatch rules can automate Lambda function execution based on specific conditions or schedules.
2. You can enable, disable, or delete the cronjobs as needed.
3. By following these steps, you can automate the start and stop of your Amazon EC2 instances using Lambda and CloudWatch rules.
