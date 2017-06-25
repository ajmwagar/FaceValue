from timeit import default_timer
fd = __import__("feed")
az = __import__("imgEmotion")

# def main():
while 1:
    print("Enabling ... Please wait")

    i = 1

    start = default_timer()

    duration = default_timer() - start
    print(duration)

    if duration >= 40:
        az.getEmotion(fd.imgpath)
        start = default_timer()
        print(duration)
    fd.runFeed()
# main()
