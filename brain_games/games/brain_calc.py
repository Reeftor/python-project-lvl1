# -*- coding:utf-8 -*-

"""Brain_calc game logic."""

import operator
from random import choice, randint

import prompt


def brain_calc(user_name):
    """Brain_calc game function.

    Args:
        user_name: The name of user.
    """
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    answer = ''
    correct_answer = ''
    req_correct = 3
    correct_answers = 0

    while correct_answers != 3 and answer == correct_answer:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        ch_oper = choice(list(operations.keys()))
        print('Question: {0} {1} {2}'.format(num1, ch_oper, num2))
        answer = prompt.string('Your answer: ')
        correct_answer = str(operations[ch_oper](num1, num2))
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
    if correct_answers == req_correct:
        print('Congratulations, {0}!'.format(user_name))
    else:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer))
        print("Let's try again, {0}!".format(user_name))
