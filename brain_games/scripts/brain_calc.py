# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.cli import welcome_user
from brain_games.games.brain_calc import brain_calc


def main():
    """Start brain calc game."""
    print('\nWelcome to the Brain Games!')
    print('What is the result of the expression?\n')
    name = welcome_user()
    brain_calc(name)


if __name__ == '__main__':
    main()
