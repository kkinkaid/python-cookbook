def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)

# Discussion
def countdown(n):
    print('Start to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

