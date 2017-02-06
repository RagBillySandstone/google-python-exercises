# My artifact from following the Argparse Tutorial from the Python site:
# https://docs.python.org/2.7/howto/argparse.html

import argparse
parser = argparse.ArgumentParser(description='calculate X to the power of Y')

# -v and -q are conflicting or 'mutually exclusive'
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action="store_true")
group.add_argument('-q', '--quiet', action='store_true')

parser.add_argument('x', type=int, help='the base')
parser.add_argument('y', type=int, help='the exponent')

args = parser.parse_args()

answer = args.x**args.y

if args.quiet:
  print answer
elif args.verbose:
  print "{} to the power of {} equals {}".format(args.x, args.y, answer)
else:
  print "{}^{} == {}".format(args.x, args.y, answer)

