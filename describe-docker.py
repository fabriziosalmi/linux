import json
import docker

def format_attribute(attribute):
    """ Formats complex attributes to a readable JSON string. """
    return json.dumps(attribute, indent=2)

def list_docker_containers():
    client = docker.from_env()
    containers = client.containers.list(all=True)
    container_details = []
    for container in containers:
        container.reload()  # Reload the latest data from Docker daemon
        details = {
            'ContainerID': container.short_id,
            'Image': container.image.tags[0] if container.image.tags else 'N/A',
            'Name': container.name,
            'Status': container.status,
            'Command': container.attrs.get('Config', {}).get('Cmd', 'N/A'),
            'Created': container.attrs.get('Created', 'N/A'),
            'Ports': container.attrs.get('NetworkSettings', {}).get('Ports', {}),
            'Networks': list(container.attrs.get('NetworkSettings', {}).get('Networks', {}).keys()),
            'Mounts': container.attrs.get('Mounts', []),
            'Environment': container.attrs.get('Config', {}).get('Env', []),
            'ResourceLimits': container.attrs.get('HostConfig', {}).get('Resources', {})
        }
        container_details.append(details)
    return container_details

def format_docker_containers(containers):
    markdown = "## Docker Containers\n"
    for container in containers:
        markdown += (
            f"- **Container ID**: `{container['ContainerID']}`\n"
            f"  - **Image**: `{container['Image']}`\n"
            f"  - **Name**: `{container['Name']}`\n"
            f"  - **Status**: `{container['Status']}`\n"
            f"  - **Command**: `{container['Command']}`\n"
            f"  - **Created**: `{container['Created']}`\n"
            f"  - **Ports**: \n```\n{format_attribute(container['Ports'])}\n```\n"
            f"  - **Networks**: `{', '.join(container['Networks'])}`\n"
            f"  - **Mounts**: \n```\n{format_attribute(container['Mounts'])}\n```\n"
            f"  - **Environment Variables**: \n```\n{format_attribute(container['Environment'])}\n```\n"
            f"  - **Resource Limits**: \n```\n{format_attribute(container['ResourceLimits'])}\n```\n"
        )
    return markdown

def main():
    docker_containers = list_docker_containers()
    print(format_docker_containers(docker_containers))

if __name__ == "__main__":
    main()
