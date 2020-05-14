# -*- coding:utf-8 -*-

"""Brain_prime game logic."""

from random import randint

GAME_DESCR = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isprimenum():
    """Generate number and check it on prime.

    Returns:
        Generated number, isPrime number (str)
    """
    num = randint(0, 100)
    prime = 'yes'
    if num > 1:
        numbers = 2  # div num / numbers from 2 to numbers
        while prime == 'yes' and numbers < num:
            if num % numbers == 0:
                prime = 'no'
            numbers += 1
    else:
        prime = 'no'
    return (num, prime)


def make_question():
    """Brain_prime game function.

    Returns:
        question, correct_answer
    """
    num, prime = isprimenum()
    question = 'Quesion: {0}'.format(num)
    return question, prime
