from autogen_agentchat.agents import CodeExecutorAgent


def get_code_executor_agent(code_executor):
    code_executor_agent = CodeExecutorAgent(
        name='Python_Code_Executor',
        code_executor=code_executor
    )
    return code_executor_agent
