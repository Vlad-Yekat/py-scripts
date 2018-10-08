# sort stack recursively using only push, pop and isepmpty


def insert(element, stack):
    if len(stack) != 0 and element > stack[-1]:
        top = stack.pop()
        insert(element, stack)
        stack.append(top)
    else:
        stack.append(element)


def stack_sort(stack):
    if len(stack) != 0:
        top = stack.pop()
        stack_sort(stack)
        insert(top, stack)


stack = [1, 2, 3, 4]
print(stack)
stack_sort(stack)
print(stack)