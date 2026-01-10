from planner import generate_plan

goal = input("Enter your learning goal (AI / Software Engineering): ")
hours = int(input("Enter available study hours per week: "))

plan = generate_plan(goal, hours)

print("\nYour study plan:")
for week, topic in plan.items():
    print(f"{week}: {topic}")
