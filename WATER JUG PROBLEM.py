def water_jug_problem():
    jug_a = 0
    jug_b = 0
    max_a = 4
    max_b = 3
    goal = 2
    print("Steps to reach the goal:")
    jug_b = max_b
    print(f"Fill Jug B: A = {jug_a}, B = {jug_b}")
    pour = min(jug_b, max_a - jug_a)
    jug_a += pour
    jug_b -= pour
    print(f"Pour B -> A: A = {jug_a}, B = {jug_b}")
    jug_b = max_b
    print(f"Fill Jug B: A = {jug_a}, B = {jug_b}")
    pour = min(jug_b, max_a - jug_a)
    jug_a += pour
    jug_b -= pour
    print(f"Pour B -> A: A = {jug_a}, B = {jug_b}")
    jug_a = 0
    print(f"Empty Jug A: A = {jug_a}, B = {jug_b}")
    jug_a = jug_b
    jug_b = 0
    print(f"Pour B -> A: A = {jug_a}, B = {jug_b}")
    jug_b = max_b
    print(f"Fill Jug B: A = {jug_a}, B = {jug_b}")
    pour = min(jug_b, max_a - jug_a)
    jug_a += pour
    jug_b -= pour
    print(f"Pour B -> A: A = {jug_a}, B = {jug_b}")
    if jug_a == goal:
        print("Goal reached!")
    else:
        print("Goal not reached.")
water_jug_problem()
