# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.cli import welcome_user
from brain_games.games.brain_progression import brain_progression


def main():
    """Start brain progression game."""
    print('\nWelcome to the Brain Games!')
    print('What number is missing in the progression?\n')
    name = welcome_user()
    brain_progression(name)


if __name__ == '__main__':
    main()
