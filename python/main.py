from timeit import default_timer
fd = __import__("feed")

# def main():
while 1:
    print("Enabling ... Please wait")

    i = 1

    start = default_timer()

    duration = default_timer() - start

    start = default_timer()
    print(duration)
    fd.runFeed()
# main()test.jpeg
