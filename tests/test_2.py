import pytest
from time import sleep

def dummy_test_2():
    num1 = 27
    num2 = 27

    sleep(3)

    assert num1 == num2

def dummy_test_3():
    num1 = 2
    num2 = 3

    sleep(7)

    assert num1 + num2 == num2 + num1