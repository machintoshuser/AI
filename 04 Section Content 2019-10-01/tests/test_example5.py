# Example 5: using hypothesis

"""
TBD whether or not we want to use this example. Hypothesis definitely looks pretty cool so this is what I could hack together.


Some comments:
1. What is Property Based Testing and why is it different from traditional unit testing?
* Rather than writing a test that just explores a single scenario, you can write tests that describe a *range* of scenarios and let the computer explore the possibilities for you
* Automates most time consuming part of writing tests -- coming up with specific examples

https://hypothesis.works/
"""
from hypothesis import given, strategies as st


def reverse(x):
    """
    The basis of this question comes from leetcode question 7: Reverse Integer

    Given a 32-bit signed integer, reverse digits of an integer.
    """
    factor = 1
    if x < 0:
        x *= -1
        factor = -1

    sol = int(str(x)[::-1]) * factor
    return sol


@given(st.integers())  # here hypothesis will generate a random set of integers for us to test on
def test_reverse(x):
    y = abs(x)
    reverse_str_list = list(str(reverse(y)))
    for j in list(str(y))[::-1]:
        if (j == "0") & (len(str(y)) > 1):  # try uncommenting one of these if conditions to see why they were needed
            reverse_str_list.append("0")
        else:
            break
    assert(sorted(reverse_str_list) == sorted(list(str(y))))
