# Program 3: GPS Navigation using Stack

stack = []

stack.append("Home")
stack.append("Mall")
stack.append("Park")

print("Current Place:", stack[-1])

print("Going Back from:", stack.pop())
print("Current Place:", stack[-1])

stack.append("Lake")

print("Current Place:", stack[-1])
print("Navigation History:")
print(stack)
