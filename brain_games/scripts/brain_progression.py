# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.engine import run
from brain_games.games import brain_progression


def main():
    """Start brain_progression game."""
    run(brain_progression)


if __name__ == '__main__':
    main()
