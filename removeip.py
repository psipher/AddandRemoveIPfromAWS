  import boto3
ec2_client = boto3.client('ec2')
def lambda_handler(event, context):
    response = ec2_client.revoke_security_group_ingress(
        GroupId='sg-0742aa1cc6eb524d5',
        IpPermissions=[
            {
                'FromPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '203.0.113.0/24',
                        
                    },
                ],
                'ToPort': 22,
            },
        ],
    )
