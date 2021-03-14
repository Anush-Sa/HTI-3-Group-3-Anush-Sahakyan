import sys

def odd(start, stop):
    for num in range(int(start), int(stop)):
        for i in str(num):
            if int(i) % 2 == 0:
                break
        else:
            yield num

if __name__ == '__main__':
    for n in odd(sys.argv[1], sys.argv[2]):
        print(n, end=' ')
    print()

