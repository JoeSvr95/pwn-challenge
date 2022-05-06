import time
from timer import Timer

t = Timer()

# # Start the timer
# t.start()

# # Simulating some processing
# print("Mocking a function executing...")
# time.sleep(100)
# print("Finish processing...")

# for i in range(1000):
#     pass

# # Stop timer
# t.stop()

t.format_message(34)
t.format_message(30.12345)
t.format_message(100)
t.format_message(100.4564)
t.format_message(4532)
t.format_message(4532.2312)
