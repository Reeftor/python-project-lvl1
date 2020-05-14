# -*- coding:utf-8 -*-

"""Brain_even game logic."""


from random import randint

GAME_DESCR = 'Answer "yes" if number even otherwise answer "no".'


def make_question():
    """Brain_even game function.

    Returns:
        question, correct_answer
    """
    num = randint(1, 100)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = 'Question: {0}'.format(num)
    return question, correct_answer
