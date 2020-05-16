# -*- coding: utf-8 -*-

"""Brain games engine module."""

from brain_games.cli import get_answer, get_username

CORRECT_ANSWERS_REQUIRED = 3


def welcome_user():
    """Ask user name and greetings him.

    Returns:
        user_name
    """
    user_name = get_username()
    print('Hello, {0}'.format(user_name))
    return user_name


def run(game=None):
    """Start the game.

    GAME_DESCR - global constant, should contains a game
    description.

    Args:
        game: name of module, which contains a game logic
        def make_question():
        should return (question, correct_answer).
    """
    print('\nWelcome to the Brain Games!')
    if game is not None:
        print(game.GAME_DESCR)
    print()
    user_name = welcome_user()
    print()
    if game is not None:
        gameprocess(user_name, game.make_question)


def gameprocess(user_name, gamefuncs):
    """Continue of run function.

    Args:
        user_name: user name
        gamefuncs: game function that returns question
        and correct answer
    """
    rezult = qac(gamefuncs)
    final_msg(user_name, rezult)


def qac(gamefuncs):
    """Question-Answer Cycle.

    Args:
        gamefuncs: see gameprocess function

    Returns:
        True if user gives correct answers of all questions,
        False if user give at least one wrong answer.
    """
    correct_answers = 0
    while correct_answers != CORRECT_ANSWERS_REQUIRED:
        question, correct_answer = gamefuncs()
        print(question)
        answer = get_answer()
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer))
            return False
    return True


def final_msg(user_name, rezult):
    """Gen final message of game depends on rezult.

    Args:
        user_name: see gameprocess() args.
        rezult: bool, see True if user win, Flase if else.
    """
    if rezult:
        print('Congratulations, {0}!'.format(user_name))
    else:
        print("Let's try again, {0}!".format(user_name))
