from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

from config.constants import DOCKER_IMAGE, DOCKER_TIMEOUT, DOCKER_WORK_DIR


def get_docker_command_line_executor():
    docker = DockerCommandLineCodeExecutor(
        image=DOCKER_IMAGE,
        timeout=DOCKER_TIMEOUT,
        work_dir=DOCKER_WORK_DIR,
    )
    return docker


async def start_docker_container(docker):
    print("Starting Docker Container...")
    await docker.start()
    print("Docker Container Started!")


async def stop_docker_container(docker):
    print("Stopping Docker Container...")
    await docker.stop()
    print("Docker Container Stopped!")
