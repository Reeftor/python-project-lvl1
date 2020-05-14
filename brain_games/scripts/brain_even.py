# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.engine import run
from brain_games.games import brain_even


def main():
    """Start brain_even game."""
    run(brain_even)


if __name__ == '__main__':
    main()
