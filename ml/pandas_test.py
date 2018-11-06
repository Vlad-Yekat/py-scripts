'''
using pandas as SQL
'''

import pandas as pd

frame = pd.DataFrame({
    'city': ['Moscow', 'Yekaterinburg', 'Sankt-Peterburg'],
    'population': [12506000, 1468000, 5350000],
    'year': [1147, 1723, 1703]
})

new_city= {'city':'Omsk', 'population':1172000, 'year':1716}
frame = frame.append(new_city, ignore_index=True)
# frame.to_csv('city.csv', sep=',', header=False, index=None)

# select from frame where city=Moscow
print(frame[frame.city=='Moscow'])