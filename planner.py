import json

def generate_plan(goal, hours_per_week):
    goal = goal.lower()

    with open("topics.json", "r") as f:
        topics_data = json.load(f)

    if goal not in topics_data:
        return {}

    topics = topics_data[goal]
    plan = {}

    for i, topic in enumerate(topics, start=1):
        plan[f"Week {i}"] = topic

    return plan
