import sys


try:
    1 / 0
except ZeroDivisionError as ex:
    print("exception!", ex)
finally:
    print("finally run in always conditions")


def ex_raise():
    raise Exception("broken code")


try:
    ex_raise()
except Exception as ex:
    print("captured ex:", ex)

try:
    sys.exit(1)
except Exception:
    print("no ...")
except:
    print("not type exception!")
