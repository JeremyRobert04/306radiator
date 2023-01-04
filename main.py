#!/usr/bin/env python3

import sys

from src.my_parser import MyParser as Parser
from src.radiator import Radiator

def main(args=None):
    if args is None:
        args = sys.argv

    parser = Parser(args)

    nPow, n, ir, jr, i, j = parser.check_cmd()
    radiator = Radiator(n, nPow, ir, jr, i, j)

    radiator.radiator()
    sys.exit(0)

if __name__ == '__main__':
    main()