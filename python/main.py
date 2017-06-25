from timeit import default_timer
fd = __import__("feed")
az = __import__("imgEmotion")

print("Enabling ... Please wait")

start = default_timer()

duration = default_timer() - start
print(duration)
fd.runFeed()


while True:
    if duration >= 40:
        az.getEmotion(fd.imgpath)
        start = default_timer()
