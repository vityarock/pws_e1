import pytest
from gallows import *
import builtins




builtins.foo = ['_', '_', '_', '_', '_', '_', '_', '_']
target = 'coverage'
answer = 'e'

def test_letter_check():
    test_result = letter_check(target, answer)
    assert test_result != True, "тест не пройден"
# assert test_result == False, "тест пройден" 


test_letter_check()
