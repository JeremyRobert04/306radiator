import sys

import src.my_print as Print

class MyParser():
    def __init__(self, args = []) -> None:
        self.args = [x for ind, x in enumerate(args) if ind != 0]
        self.parsed_args = []

    def display_help(self):
        print("USAGE")
        print("\t./306radiator n ir jr [i j]\n")
        print("DESCRIPTION")
        print("\tn\t\tsize of the room")
        print("\t(ir, jr)\tcoordinates of the radiator")
        print("\t[i, j]\t\tOPTIONNAL: coordinates of a point in the room")

    def check_for_help(self):
        if self.args[0] in ("-h", "--help"):
            self.display_help()
            sys.exit(0)

    def format_args(self):
        if len(self.parsed_args) == 3:
            self.parsed_args.insert(0, self.parsed_args[0] ** 2)
            self.parsed_args.extend([None, None])
            return self.parsed_args[0] ** 2, self.parsed_args, None, None
        else:
            self.parsed_args.insert(0, self.parsed_args[0] ** 2)

    def check_params(self):
        if self.parsed_args[0] < 3:
            Print.print_error(f"Room size should be greater than 2 but got: {self.parsed_args[0]}")
        if not (1 <= self.parsed_args[1] <= (self.parsed_args[0] - 2)):
            Print.print_error(f"X coordinate for radiator should be between 1 <= X <= {self.parsed_args[0] - 2}, but got X: {self.parsed_args[1]}")
        if not (1 <= self.parsed_args[2] <= (self.parsed_args[0] - 2)):
            Print.print_error(f"Y coordinate for radiator should be between 1 <= Y <= {self.parsed_args[0] - 2}, but got Y: {self.parsed_args[2]}")
        if len(self.parsed_args) > 3:
            if not (1 <= self.parsed_args[3] <= (self.parsed_args[0] - 2)):
                Print.print_error(f"X coordinate for position should be between 1 <= X <= {self.parsed_args[0] - 2}, but got X: {self.parsed_args[3]}")
            if not (1 <= self.parsed_args[4] <= (self.parsed_args[0] - 2)):
                Print.print_error(f"Y coordinate for position should be between 1 <= Y <= {self.parsed_args[0] - 2}, but got Y: {self.parsed_args[4]}")
        return True

    def check_cmd(self):
        if not self.args:
            Print.print_error("Missing parameters\n\tDo -h to get help.")
        self.check_for_help()
        if len(self.args) < 3 or len(self.args) == 4:
            Print.print_error("Uncorrect number of parameters\n\tDo -h to get help.")
        if len(self.args) > 5 :
            Print.print_error("Too many parameters\n\tDo -h to get help.")
        self.parsed_args = [ self.safeIntConverter(value) for value in self.args]
        if any(value is None for value in self.parsed_args):
            Print.print_error("Parameters should only contains number.")
        self.check_params()
        self.format_args()
        return self.parsed_args

    def safeIntConverter(self, str):
        try:
            result = int(str)
            return result
        except:
            return None
