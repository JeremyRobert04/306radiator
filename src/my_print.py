import sys
import decimal

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_error(*args, **kwargs):
    """print the defines message to stderr and then exit(84)
    """
    print(bcolors.FAIL + "ERROR:\t" + bcolors.ENDC + "".join(map(str,args)), file=sys.stderr, **kwargs)
    sys.exit(84)

def print_vec_result(vectorX):
    """print an array

    Args:
        vectorX (array): array representing the vector X
    FIXME print line 28 print 2 times the value, unset the second one to pass the moulie
    """
    print()
    for value in vectorX:
        print(decimal.Decimal(value).quantize(decimal.Decimal('0.0'), rounding=decimal.ROUND_HALF_UP))

def print_specific_point(vectorX, n: int, coordinates):
    """print a value at a specific coordinates rounded at .1

    Args:
        vectorX (array): array representing the list of data
        n (int): size of the room
        coordinates ((x,y)): coordinate in x and y of the point
    """
    value = vectorX[coordinates[0] + coordinates[1] * n]
    print(decimal.Decimal(value).quantize(decimal.Decimal('0.0'), rounding=decimal.ROUND_HALF_UP))

def num_precision(num):
    """return the number without the trailing zeros and rounded at .1

    Args:
        num (numerical data): number

    Returns:
        float: your number rounded at .1 and without the trailing zeros
    """
    return ('%.1f' % num).rstrip('0').rstrip('.')

def print_matrix(matrixA):
    """print a 2d array

    Args:
        matrixA (2 dimensionnal array): print a 2 dimentionnal array with \\t between elements
    """
    for i, row in enumerate(matrixA):
        for j, col in enumerate(row):
            print(num_precision(col), end="")
            if j != len(matrixA[i]) - 1:
                print("\t", end="")
        print()