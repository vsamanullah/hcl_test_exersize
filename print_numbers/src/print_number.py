
# program that prints the numbers 1,2,3,4,5,6,7,8,10
def print_numbers():
    print( ','.join(str(num_to_print) for num_to_print in range(1, 11)) )


if __name__ == '__main__':
    exit(print_numbers())
