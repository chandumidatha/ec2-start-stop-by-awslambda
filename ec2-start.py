import boto3

# Set the AWS region and instance IDs
region = 'ap-south-1'
instances = ['i-12345cb6de4f78g9h', 'i-08ce9b2d7eccf6d26']

# Create an EC2 client
ec2 = boto3.client('ec2', region_name=region)

# Lambda handler function
def lambda_handler(event, context):
    # Start the specified EC2 instances
    ec2.start_instances(InstanceIds=instances)
    
    # Print a message confirming the instances have been started
    print('Started your instances: ' + str(instances))
