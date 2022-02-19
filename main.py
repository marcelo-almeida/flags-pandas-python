import pandas as pd
from pandas.core.series import Series


class DataFrameInfo:

    def __init__(self):
        self.flags = pd.read_csv('data/flags.csv')
        # print(f'head():\n{self.flags.head()}')
        # print('-----------------------------------')
        # print(f'tail():\n{self.flags.tail()}')
        # print('-----------------------------------')
        self.countries = pd.read_csv('data/countries.csv')
        self.lines_flag = self.flags.shape[0]
        self.lines_countries = self.countries.shape[0]

    def has_colors(self) -> Series:
        colors = self.flags['green'] + self.flags['gold'] + self.flags['blue'] + self.flags['white']
        return colors == 4

    def print_countries(self, condition: Series):
        print(f'Countries:\n{self.flags[condition.values]["name"]}')

    def print_attributes(self):
        for index, columns in enumerate(self.flags.columns):
            attributes = self.flags[columns]
            has_none_values = any(attributes.isnull())
            print(f'{index} {columns}: Has any {columns} with none? {has_none_values}. {attributes.unique()}')
            if attributes.unique().size > 8 and attributes.dtype != 'object':
                print(f'{index} {columns} min: {attributes.min()} max: {attributes.max()} '
                      f'mean: {round(attributes.mean(), 2)} std {round(attributes.std(), 2)}')

    def find_frequency(self):
        colors = pd.DataFrame()
        for column in self.flags.columns:
            if column in ['red', 'green', 'blue', 'gold', 'white', 'black', 'orange']:
                colors[column] = self.flags[column].value_counts()
        print(colors)
        colors.plot(kind='barh', subplots=True, figsize=(8, 25))

    def inner_merge(self):
        both = pd.merge(self.flags, self.countries, how='inner', left_on='name', right_on='country')
        lines_both = both.shape[0]
        print(lines_both)

    def left_merge(self):
        just_flags = pd.merge(self.flags, self.countries, how='left', left_on='name', right_on='country')
        just_flags = just_flags[pd.isnull(just_flags['country']) == True]
        lines_just_flags = just_flags.shape[0]
        print(f'just flags: {just_flags["name"]}')

    def right_merge(self):
        just_countries = pd.merge(self.flags, self.countries, how='right', left_on='name', right_on='country')
        just_countries = just_countries[pd.isnull(just_countries['name']) == True]
        lines_just_countries = just_countries.shape[0]
        print(f'just countries: {just_countries["country"]}')


def main():
    info = DataFrameInfo()
    condition = info.has_colors()
    info.print_countries(condition=condition)
    info.print_attributes()
    info.find_frequency()
    info.inner_merge()
    info.left_merge()
    info.right_merge()


if __name__ == '__main__':
    main()
