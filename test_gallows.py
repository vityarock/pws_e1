import pytest
from gallows import *
import builtins

builtins.foo = ['_', '_', '_', '_', '_', '_', '_', '_']
target = 'coverage'
answer = 'e'


def test_letter_check():
    test_result = letter_check(target, answer)
    print(test_result)
    assert test_result == False, "тест не пройден"

test_letter_check()
