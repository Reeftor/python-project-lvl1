# -*- coding: utf-8 -*-

"""CLI Functions module."""

import prompt


def get_username():
    """Get username.

    Returns:
        Username.
    """
    name = prompt.string('May I have your name? ')
    return name


def get_answer():
    """Get user answer.

    Returns:
        User answer
    """
    user_answer = prompt.string('Your answer: ')
    return user_answer
