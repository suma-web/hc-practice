import random

member = ['A', 'B', 'C', 'D', 'E', 'F']

new_member = random.sample(member, len(member))
n = random.choice([2,3])

print(f"Aグループ：{sorted(new_member[:n])}")
print(f"Bグループ：{sorted(new_member[n:])}")