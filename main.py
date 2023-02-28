import sys
from pairs import get_pairs

if __name__ == '__main__':
    arr = []
    for num in sys.argv[1].split(","):
        try:
            arr.append(int(num))
        except ValueError:
            print("list must contain only integers, {} is not valid".format(num))

    numSum = int(sys.argv[2])
    pairs = get_pairs(arr, numSum)

    for pair in pairs:
        print("{}, {}".format(pair[0], pair[1]))
