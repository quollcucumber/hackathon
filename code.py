df['What grade do you usually achieve overall?'] = df['What grade do you usually achieve overall?'].replace(['A+', 'A', 'B+', 'B', 'C', 'D or below'], [0, 1, 2, 3, 4, 5], inplace=True)
