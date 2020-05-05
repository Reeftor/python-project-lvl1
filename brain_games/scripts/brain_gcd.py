# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.cli import welcome_user
from brain_games.games.brain_gcd import brain_gcd


def main():
    """Start brain calc game."""
    print('\nWelcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.\n')
    name = welcome_user()
    brain_gcd(name)


if __name__ == '__main__':
    main()
