import argparse
import math
import numbers

parser = argparse.ArgumentParser(description="a simple calculator")

parser.add_argument(
    "numbers",
    metavar="N",
    nargs="+",
    help="a number for the accumulator",
)

parser.add_argument(
    "-add",
    "--addition",
    action="store_const",
    const=sum,
    help="sum the numbers",
)
parser.add_argument(
    "-mul",
    "--multiplication",
    action="store_const",
    const=math.prod,
    help="multiplication the numbers",
)

args = parser.parse_args()

numbers = []

for i, number in enumerate(args.numbers):
    # isdigit() returns True if all characters in the string are digits.
    if number.isdigit() == False:
        numbers.append(float(number))
    else:
        numbers.append(int(number))

if args.addition:
    print(sum(numbers))
elif args.multiplication:
    print(math.prod(numbers))
