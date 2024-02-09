# ec2-start-stop-by-awslambda
To start and stop EC2 instances at regular intervals using the AWS Lambda service

## **Setting Up Lambda IAM Role**
To grant necessary permissions to your Lambda function, follow these steps:

#### Access AWS Management Console:
```bash
1. Go to the IAM Service:
2. Navigate to the IAM (Identity and Access Management) service.
```
#### Create a New Role:
```bash
1. Click on "Roles" in the left-hand navigation pane.
2. Click the "Create role" button.
```
#### Select Lambda as the Service:
```bash
1. Choose "Lambda" as the service that will use this role, then click "Next: Permissions".
2. Define Permissions:
3. Switch to the "JSON" tab.
```
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
