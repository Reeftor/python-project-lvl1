# -*- coding:utf-8 -*-

"""Brain_calc game logic."""

import operator
from random import choice, randint

GAME_DESCR = 'What is the result of the expression?'


def make_question():
    """Brain_calc game function.

    Returns:
        question, correct_answer
    """
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    ch_oper = choice(list(operations.keys()))
    correct_answer = str(operations[ch_oper](num1, num2))
    question = 'Question: {0} {1} {2}'.format(num1, ch_oper, num2)
    return question, correct_answer
