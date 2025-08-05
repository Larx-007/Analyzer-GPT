from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from agents.code_executor_agent import get_code_executor_agent
from agents.data_analyzer_agent import get_data_analyzer_agent


def get_data_analyzer_team(model_client, docker):
    data_analyzer_agent = get_data_analyzer_agent(model_client)
    code_executor_agent = get_code_executor_agent(docker)
    text_mention_termination = TextMentionTermination('STOP')
    team = RoundRobinGroupChat(
        name='analyzer_gpt',
        participants=[data_analyzer_agent, code_executor_agent],
        termination_condition=text_mention_termination,
        max_turns=10
    )
    return team
