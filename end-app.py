import subprocess #allows to execute command in terminal from python

def stop_services():
    subprocess.run(["docker-compose", "down"], check=True)

if __name__ == "__main__":
    stop_services()