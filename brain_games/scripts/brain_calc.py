# -*- coding:utf-8 -*-

"""Main script."""


from brain_games.engine import run
from brain_games.games import brain_calc


def main():
    """Start brain_calc game."""
    run(brain_calc)


if __name__ == '__main__':
    main()
