# 1. Create an empty list called `task_list`
task_list = []

# 2. Add a few `str` elements, representing some everyday tasks e.g. 'Make Dinner'
task_list = ['brush teeth', 'make dinner', 'fill dog water bowl']
task_list.append('clean toilet')
# you can only append one element at once when using .append method

# 3. Print out `task_list`
print(task_list)

# 4. Remove the last task
task_list.pop()

# 5. Print out `task_list`
print (task_list)

# 6. Print out the number of elements in `task_list`
num_of_tasks = len(task_list)
print(num_of_tasks)

# OR

# print(len(task_list))