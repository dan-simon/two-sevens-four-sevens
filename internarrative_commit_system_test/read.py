import os.path as path
import sys
import time

pause = .07

def get_time(x):
    if x == float('inf'):
        return 'an eternity (or is it an infinity?)'
    x = round(x, 1)
    hours = int(x // 3600)
    minutes = int(x // 60 % 60)
    seconds = round(x % 60, 1)
    parts = []
    if hours:
        parts.append(str(hours) + ' hour' + 's' * (hours != 1))
    if minutes:
        parts.append(str(minutes) + ' minute' + 's' * (minutes != 1))
    if seconds:
        parts.append(str(seconds) + ' second' + 's' * (seconds != 1))
    if len(parts) == 3:
        return parts[0] + ', ' + parts[1] + ', and ' + parts[2]
    elif len(parts) == 2:
        return parts[0] + ' and ' + parts[1]
    elif len(parts) == 1:
        return parts[0]
    else:
        return 'no time at all'

def main():
    p = path.join(path.dirname(__file__), '../two_sevens_four_sevens_main.md')
    pause = .04
    with open(p) as f:
        s = f.read()
    print('Estimated reading time: ' + get_time(pause * len(s)))
    on = True
    ind = 0
    while ind < len(s):
        try:
            if on:
                print(s[ind], end='')
                ind += 1
                sys.stdout.flush()
            time.sleep(pause)
        except KeyboardInterrupt:
            print('\b\b', end='')
            sys.stdout.flush()
            on = not on

if __name__ == '__main__':
    main()
