# -*- coding:utf-8 -*-

"""Brain_progression game logic."""

from random import randint

import prompt


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
            progression += ' {0}'.format(' ..')
        else:
            progression += ' {0}'.format(num)
        num += step
    progression = progression[1:]

    return (progression, num_to_hide)


def brain_progression(user_name):
    """Brain_progression game function.

    Args:
        user_name: The name of user.
    """
    answer = ''
    correct_answer = ''
    req_correct = 3
    correct_answers = 0

    while correct_answers != 3 and answer == correct_answer:
        progression, correct_answer = generate_progression()
        print('Question: {0}'.format(progression))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
    if correct_answers == req_correct:
        print('Congratulations, {0}!'.format(user_name))
    else:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer))
        print("Let's try again, {0}!".format(user_name))
