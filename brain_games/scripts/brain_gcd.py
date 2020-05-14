# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.engine import run
from brain_games.games import brain_gcd


def main():
    """Start brain_gcd game."""
    run(brain_gcd)


if __name__ == '__main__':
    main()
