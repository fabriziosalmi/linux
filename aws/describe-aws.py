import boto3

def list_ec2_instances(region):
    ec2_client = boto3.client('ec2', region_name=region)
    instances = ec2_client.describe_instances()
    detailed_instances = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_details = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'Architecture': instance.get('Architecture', 'N/A'),
                'CPUs': instance.get('CpuOptions', {}).get('CoreCount', 'N/A'),
                'RAM': 'See instance type for details',
                'RootDeviceType': instance.get('RootDeviceType', 'N/A')
            }
            detailed_instances.append(instance_details)
    return detailed_instances

def list_security_groups(region):
    ec2_client = boto3.client('ec2', region_name=region)
    groups = ec2_client.describe_security_groups()
    detailed_groups = []
    for group in groups['SecurityGroups']:
        group_details = {
            'GroupName': group['GroupName'],
            'GroupId': group['GroupId'],
            'InboundRules': group.get('IpPermissions', []),
            'OutboundRules': group.get('IpPermissionsEgress', [])
        }
        detailed_groups.append(group_details)
    return detailed_groups

def list_subnets_and_route_tables(region):
    ec2_client = boto3.client('ec2', region_name=region)
    subnets = ec2_client.describe_subnets()
    route_tables = ec2_client.describe_route_tables()
    return subnets['Subnets'], route_tables['RouteTables']

def list_rds_instances(region):
    rds_client = boto3.client('rds', region_name=region)
    instances = rds_client.describe_db_instances()
    return instances['DBInstances']

def list_ebs_volumes(region):
    ec2_client = boto3.client('ec2', region_name=region)
    volumes = ec2_client.describe_volumes()
    return volumes['Volumes']

def list_efs_file_systems(region):
    efs_client = boto3.client('efs', region_name=region)
    file_systems = efs_client.describe_file_systems()
    return file_systems['FileSystems']

def list_s3_buckets(region):
    s3_client = boto3.client('s3', region_name=region)
    buckets = s3_client.list_buckets()
    return buckets['Buckets']

def list_backup_plans(region):
    backup_client = boto3.client('backup', region_name=region)
    backup_plans = backup_client.list_backup_plans()['BackupPlansList']
    return backup_plans

def format_ec2_instances(instances):
    markdown = "## EC2 Instances\n"
    for instance in instances:
        markdown += f"- **Instance ID**: `{instance['InstanceId']}`, **Type**: `{instance['InstanceType']}`, **State**: `{instance['State']}`, **Architecture**: `{instance['Architecture']}`, **CPUs**: `{instance['CPUs']}`, **RAM**: `{instance['RAM']}`, **Root Device Type**: `{instance['RootDeviceType']}`\n"
    return markdown

def format_security_groups(groups):
    markdown = "## Security Groups\n"
    for group in groups:
        markdown += f"- **Group Name**: `{group['GroupName']}`, **Group ID**: `{group['GroupId']}`\n"
        markdown += "  - **Inbound Rules**:\n"
        for rule in group['InboundRules']:
            ip_protocol = rule.get('IpProtocol', 'N/A')
            from_port = rule.get('FromPort', 'N/A')
            to_port = rule.get('ToPort', 'N/A')
            ip_ranges = ', '.join([ip.get('CidrIp', 'N/A') for ip in rule.get('IpRanges', [])])
            markdown += f"    - Protocol: `{ip_protocol}`, Ports: `{from_port}-{to_port}`, IP Ranges: `{ip_ranges}`\n"

        markdown += "  - **Outbound Rules**:\n"
        for rule in group['OutboundRules']:
            ip_protocol = rule.get('IpProtocol', 'N/A')
            from_port = rule.get('FromPort', 'N/A')
            to_port = rule.get('ToPort', 'N/A')
            ip_ranges = ', '.join([ip.get('CidrIp', 'N/A') for ip in rule.get('IpRanges', [])])
            markdown += f"    - Protocol: `{ip_protocol}`, Ports: `{from_port}-{to_port}`, IP Ranges: `{ip_ranges}`\n"
    return markdown



def format_subnets_and_route_tables(subnets, route_tables):
    markdown = "## Subnets and Route Tables\n"
    for subnet in subnets:
        markdown += f"- **Subnet ID**: `{subnet['SubnetId']}`, **CIDR**: `{subnet['CidrBlock']}`\n"
    for route_table in route_tables:
        markdown += f"- **Route Table ID**: `{route_table['RouteTableId']}`\n"
    return markdown

def format_rds_instances(instances):
    markdown = "## RDS Instances\n"
    for instance in instances:
        markdown += f"- **DB Instance Identifier**: `{instance['DBInstanceIdentifier']}`, **DB Engine**: `{instance['Engine']}`\n"
    return markdown

def format_ebs_volumes(volumes):
    markdown = "## EBS Volumes\n"
    for volume in volumes:
        markdown += f"- **Volume ID**: `{volume['VolumeId']}`, **State**: `{volume['State']}`\n"
    return markdown

def format_efs_file_systems(file_systems):
    markdown = "## EFS File Systems\n"
    for fs in file_systems:
        markdown += f"- **File System ID**: `{fs['FileSystemId']}`, **Life Cycle State**: `{fs['LifeCycleState']}`\n"
    return markdown

def format_s3_buckets(buckets):
    markdown = "## S3 Buckets\n"
    for bucket in buckets:
        markdown += f"- **Bucket Name**: `{bucket['Name']}`\n"
    return markdown

def format_backup_plans(backup_plans):
    markdown = "## Backup Plans\n"
    for plan in backup_plans:
        markdown += f"- **Backup Plan Name**: `{plan['BackupPlanName']}`, **Backup Plan ID**: `{plan['BackupPlanId']}`\n"
    return markdown

def main():
    region = 'eu-south-1'

    # EC2 Instances
    ec2_instances = list_ec2_instances(region)
    print(format_ec2_instances(ec2_instances))

    # Security Groups
    security_groups = list_security_groups(region)
    print(format_security_groups(security_groups))

    # Subnets and Route Tables
    subnets, route_tables = list_subnets_and_route_tables(region)
    print(format_subnets_and_route_tables(subnets, route_tables))

    # RDS Instances
    rds_instances = list_rds_instances(region)
    print(format_rds_instances(rds_instances))

    # EBS Volumes
    ebs_volumes = list_ebs_volumes(region)
    print(format_ebs_volumes(ebs_volumes))

    # EFS File Systems
    efs_file_systems = list_efs_file_systems(region)
    print(format_efs_file_systems(efs_file_systems))

    # S3 Buckets
    s3_buckets = list_s3_buckets(region)
    print(format_s3_buckets(s3_buckets))

    # Backup Plans
    backup_plans = list_backup_plans(region)
    print(format_backup_plans(backup_plans))

if __name__ == "__main__":
    main()
