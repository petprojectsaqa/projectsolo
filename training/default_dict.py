import collections

with open('tasks_qa.txt') as tasks_file:
    tasks = list(map(lambda x: x.replace('\n', ''), tasks_file.readlines()))


task_dict = collections.defaultdict(list)
for line in tasks:
    tester_name, task = line.split(':')
    task_dict[tester_name].append(task)
print(task_dict)