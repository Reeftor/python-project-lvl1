# -*- coding:utf-8 -*-

"""Brain_even game logic."""


from random import randint

import prompt


def brain_even(user_name):
    """Brain_even game function.

    Args:
        user_name: The name of user.
    """
    answer = ''
    correct_answer = ''
    req_correct = 3
    correct_answers = 0
    while correct_answers != 3 and answer == correct_answer:
        number = randint(1, 100)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
    if correct_answers == req_correct:
        print('Congratulations, {0}!'.format(user_name))
    else:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer))
        print("Let's try again, {0}!".format(user_name))
