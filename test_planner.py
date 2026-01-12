from planner import generate_plan

def test_generate_plan_ai():
    plan = generate_plan("ai", 5)
    assert len(plan) > 0

def test_generate_plan_invalid_goal():
    plan = generate_plan("unknown", 5)
    assert plan == {}
