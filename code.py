def counterGame(n):
    count = bin(n).count('1')
    while n % 2 == 0:
        count += 1
        n = n >> 1
    if count % 2 == 0:
        return 'Louise'
    else:
        return 'Richard'


