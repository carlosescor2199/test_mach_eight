import sys
from pairs import get_pairs

if __name__ == '__main__':
    list_of_numbers = []
    for num in sys.argv[1].split(","):
        try:
            list_of_numbers.append(int(num))
        except ValueError:
            print("list must contain only integers, {} is not valid".format(num))

    target_sum = int(sys.argv[2])
    pairs = get_pairs(list_of_numbers, target_sum)

    for pair in pairs:
        print("{}, {}".format(pair[0], pair[1]))
