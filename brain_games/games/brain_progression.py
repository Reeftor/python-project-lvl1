# -*- coding:utf-8 -*-

"""Brain_progression game logic."""

from random import randint

GAME_DESCR = 'What number is missing in the progression?'


def generate_progression():
    """Generate arithmetic progression for brain_progression game.

    Returns:
        progression and missing number.
    """
    num = randint(1, 100)
    step = randint(1, 10)
    length = 10
    progression = ''
    pos_to_hide = randint(0, length - 1)

    for pos in range(length):
        if pos == pos_to_hide:
            num_to_hide = str(num)
            progression += ' {0}'.format('..')
        else:
            progression += ' {0}'.format(num)
        num += step
    progression = progression[1:]

    return (progression, num_to_hide)


def make_question():
    """Brain_progression game function.

    Returns:
        question, correct_answer
    """
    progression, correct_answer = generate_progression()
    question = 'Question: {0}'.format(progression)
    return question, correct_answer
