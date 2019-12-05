#!/usr/bin/env python
"""
check your manifest file after-the-fact
"""
import pandas as pd


def main():
    # making data frame from csv file
    data = pd.read_csv('manifest.csv')

    # sorting by first name
    data.sort_values('filename', inplace=True)

    # making a bool series
    bool_series = data['filename'].duplicated(keep=False)  # False means consider all of the same values as duplicates

    # displaying data
    # print(data.head())

    # display data
    x = data[bool_series]
    if len(x) == 0:
        print('No duplicates')
    else:
        # print(x)
        x.to_csv('./duplicates.csv')
        print('DUPLICATES FOUND!!')
        print('SEE: duplicates.csv')


if __name__ == '__main__':
    main()
