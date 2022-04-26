import time
from timer import Timer

t = Timer()

# Start the timer
t.start()

# Simulating some processing
print("Mocking a function executing...")
time.sleep(100)
print("Finish processing...")

for i in range(1000):
    pass

# Stop timer
t.stop()
