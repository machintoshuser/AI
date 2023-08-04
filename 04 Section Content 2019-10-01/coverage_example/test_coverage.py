from part1 import my_func
from part2 import *


def test_my_func():  # we can see here that you don't get 100% coverage
    assert (my_func(11) == 121)
    # assert (my_func(3) == 27)  # adding this in gets you full coverage

def test_my_func_1():
    assert(my_func_1(11) == 121)  # you're at 100% coverage here with this -- but is this really a "good" test?

# pipenv run pytest --cov part2 test_coverage.py
