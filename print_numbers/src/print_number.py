# program that prints the numbers 1,2,3,4,5,6,7,8,10
def print_numbers():
    print( ",".join([str(num_print) for num_print in range(1,11) if num_print != 9] ))


if __name__ == '__main__':
    exit(print_numbers())
