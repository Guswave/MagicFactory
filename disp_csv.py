#! /usr/bin/env python3

import csv
with open('test.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(spamreader)
    spamreader = sorted(spamreader,
                        key=lambda row:
                        int(row[9])
                        )
    for row in spamreader:
        print(', '.join(row))
