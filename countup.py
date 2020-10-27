import sys


def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n-1)


def countup(n):
  if n >= 0:
    print('Blastoff!')
  else:
    print(n)
    countup(n+1)


if sys.version_info[0] == 3:
  num = input('Enter number: ')
else:
  num = raw_input('Enter number: ')


num = int(num)

if num > 0:

  countdown(num)
elif num < 0:

  countup(num)
else:

  print('Blastoff!')
