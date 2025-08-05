import asyncio
from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken


async def main():

    docker = DockerCommandLineCodeExecutor(
        auto_remove=False,
        container_name='my_container',
        work_dir='experiment/test_dir',
        timeout=120
    )

    code_executor_agent = CodeExecutorAgent(
        name='CodeExecutorAgent',
        code_executor=docker,
    )

    task = TextMessage(
        content='''Here is the code 
```python
import matplotlib
print("hello world 2")
```
    ''',
        source='user'
    )

    await docker.start()

    result = await code_executor_agent.on_messages(
        messages=[task],
        cancellation_token=CancellationToken()
    )

    print("The result is", result)

    await docker.stop()


if (__name__ == '__main__'):
    asyncio.run(main())
