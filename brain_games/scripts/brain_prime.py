# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.cli import welcome_user
from brain_games.games.brain_prime import brain_prime


def main():
    """Start brain prime game."""
    print('\nWelcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')
    name = welcome_user()
    brain_prime(name)


if __name__ == '__main__':
    main()
