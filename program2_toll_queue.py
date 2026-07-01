from queue import Queue

toll = Queue(maxsize=5)

toll.put("Car")
toll.put("Bus")
toll.put("Bike")

print("Vehicles in Queue:")
print(list(toll.queue))

print("Vehicle Passed:", toll.get())

print("Remaining Vehicles:")
print(list(toll.queue))

print("Queue Full:", toll.full())
print("Queue Empty:", toll.empty())
