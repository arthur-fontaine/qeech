import sys

from qeech_data.adapters.cli.commands.recommend_recipes import recommend_recipes

commands = {"recommend": recommend_recipes}


def main():
    command = sys.argv[1]

    commands[command]()


if __name__ == "__main__":
    main()
