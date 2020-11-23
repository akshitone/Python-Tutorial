import matplotlib.pyplot as plt
import pandas as pd

data = {'Name': ['Akshit', 'Viral', 'Suru'],
        'Jan': [143, 122, 101],
        'Feb': [122, 98, 62],
        'Mar': [65, 88, 32]}

df = pd.DataFrame(data, columns=['Name', 'Jan', 'Feb', 'Mar'])

df['Total'] = df['Jan'] + df['Feb'] + df['Mar']

color = [(1, .4, .4), (1, .6, 1), (.5, .3, 1)]
plt.pie(df['Total'], labels=df['Name'], colors=color, autopct='%1.1f%%')
plt.axis(True)
plt.show()

print(df)
