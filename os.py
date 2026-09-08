import time
import request

target = input("enter target bitch: ")

while True:
  r = request.get(target)
print(r.status_code)
time.sleep(5)
print("attack finished bigger hope u got ip blocked")
