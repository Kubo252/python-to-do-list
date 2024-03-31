import subprocess
import docker

def get_container_info():
    client = docker.from_env()
    containers = client.containers.list() #list of running containers
    return containers

def start_services():
    subprocess.run(["docker-compose", "up", "--build", "-d"], check=True)
    containers = get_container_info()
    for container in containers:
        # get container name or id
        container_id_or_name = container.name if container.name else container.id
        # in case of failure, restart and configure containers
        subprocess.run(["docker", "update", "--restart=always", container_id_or_name], check=True)

if __name__ == "__main__":
    start_services()
