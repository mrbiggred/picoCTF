import os

# Run the format-string-1 application 100 times
# This didn't work for reasons I don't understand.
for i in range(25):
    payload = "%{i}$s"
    os.system("{payload} | ./format-string-1")