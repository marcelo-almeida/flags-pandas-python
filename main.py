import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series


def retrieve_csv():
    flags = pd.read_csv('data/flags.csv')
    print(f'head():\n{flags.head()}')
    print('-----------------------------------')
    print(f'tail():\n{flags.tail()}')
    print('-----------------------------------')
    return flags


def has_colors(flags: DataFrame) -> Series:
    colors = flags['green'] + flags['gold'] + flags['blue'] + flags['white']
    return colors == 4


def print_countries(flags: DataFrame, condition: Series):
    print(f'Countries:\n{flags[condition.values]["name"]}')


def main():
    flags = retrieve_csv()
    condition = has_colors(flags=flags)
    print_countries(flags=flags, condition=condition)


if __name__ == '__main__':
    main()
