# -*- coding:utf-8 -*-

"""Brain_gcd game logic."""

from random import randint

GAME_DESCR = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    """Greatest common divisor function.

    Args:
        num1: First number,
        num2: Second number.

    Returns:
        GCD
    """
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


def make_question():
    """Brain_gcd game function.

    Returns:
        quetion, correct_answer.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = 'Question: {0} {1}'.format(num1, num2)
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
