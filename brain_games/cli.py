# -*- coding: utf-8 -*-

"""Functions module."""

import prompt


def welcome_user():
    """User Greetings. Returns a string.

    # noqa: DAR201

    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name
