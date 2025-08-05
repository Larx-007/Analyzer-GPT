import asyncio

from config.docker_utils import get_docker_command_line_executor, start_docker_container, stop_docker_container
from models.openai_model_client import get_model_client
from teams.data_analyzer_team import get_data_analyzer_team


async def main():
    openai_model_client = get_model_client()
    docker = get_docker_command_line_executor()
    team = get_data_analyzer_team(openai_model_client, docker)
    try:
        task = 'Can you give me a graph of types of flowers in my data iris.csv'
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            print(f"{message.source}: {message.content}")
    except Exception as e:
        print(e)
    finally:
        await stop_docker_container(docker)

if __name__ == '__main__':
    asyncio.run(main())
