# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.engine import run
from brain_games.games import brain_prime


def main():
    """Start brain_prime game."""
    run(brain_prime)


if __name__ == '__main__':
    main()
