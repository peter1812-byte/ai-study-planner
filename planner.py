def generate_plan(goal, hours_per_week):
    goal = goal.lower()

    if goal == "ai":
        topics = [
            "Python basics",
            "Data analysis with Python",
            "Introduction to machine learning"
        ]
    else:
        topics = [
            "Python basics",
            "Data structures",
            "Basic software design"
        ]

    plan = {}

    for i, topic in enumerate(topics, start=1):
        plan[f"Week {i}"] = topic

    return plan
