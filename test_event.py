from fusion.scoring import push
import time

print("injecting fake event...")
push("IRAN",20)
time.sleep(2)
print("done")
