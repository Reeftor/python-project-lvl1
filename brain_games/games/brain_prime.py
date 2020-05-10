# -*- coding:utf-8 -*-

"""Brain_prime game logic."""

from random import randint

import prompt


def isprimenum():
    """Generate number and check it on prime.

    Returns:
        Generated number, isPrime number(bool)
    """
    num = randint(0, 100)
    prime = 'yes'
    if num > 1:
        for numbers in range(2, num):
            if num % numbers == 0:
                prime = 'no'
                break
    else:
        prime = 'no'
    return (num, prime)


def brain_prime(user_name):
    """Brain_progression game function.

    Args:
        user_name: The name of user.
    """
    answer = ''
    correct_answer = ''
    req_correct = 3
    correct_answers = 0

    while correct_answers != 3 and answer == correct_answer:
        num, correct_answer = isprimenum()
        print('Question: {0}'.format(num))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
    if correct_answers == req_correct:
        print('Congratulations, {0}!'.format(user_name))
    else:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer))
        print("Let's try again, {0}!".format(user_name))
