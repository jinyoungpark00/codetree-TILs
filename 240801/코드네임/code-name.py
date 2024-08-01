class Agent():
    def __init__(self, code_name="", score=0):
        self.code_name = code_name
        self.score = score

agent_list = [Agent() for _ in range(5)]

for i in range(5):
    code_name, score = input().split()
    score = int(score)
    agent_list[i].code_name = code_name
    agent_list[i].score = score

agent_list.sort(key=lambda agent :agent.score)

print(agent_list[0].code_name, agent_list[0].score)