# -*- coding:utf-8 -*-

"""Brain_gcd game logic."""

from random import randint

import prompt


def gcd(num1, num2):
    """Greatest common divisor function. Returns a gcd number.

    # noqa: DAR201

    Args:
        num1: First number,
        num2: Second number.
    """
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


def brain_gcd(user_name):
    """Brain_gcd game function.

    Args:
        user_name: The name of user.
    """
    answer = ''
    correct_answer = ''
    req_correct = 3
    correct_answers = 0

    while correct_answers != 3 and answer == correct_answer:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        print('Question: {0} {1}'.format(num1, num2))
        answer = prompt.string('Your answer: ')
        correct_answer = str(gcd(num1, num2))
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
    if correct_answers == req_correct:
        print('Congratulations, {0}!'.format(user_name))
    else:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer))
        print("Let's try again, {0}!".format(user_name))
