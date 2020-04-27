# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.cli import welcome_user
from brain_games.games.brain_even import brain_even


def main():
    """Start brain even game."""
    print('\nWelcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = welcome_user()
    brain_even(name)


if __name__ == '__main__':
    main()
