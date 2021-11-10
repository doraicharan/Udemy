import pandas as pd
from IPython.display import display
df = pd.read_csv('temporal.csv')

print(df.describe())
format_dict = {'data science':'${0:,.2f}', 'Mes':'{:%m-%Y}', 'machine learning':'{:.2%}'}
df['Mes'] = pd.to_datetime(df['Mes'])
df.head().style.format(format_dict)
format_dict = {'Mes':'{:%m-%Y}'}
display(df.style.render())
display(df.head().style.format(format_dict).highlight_max(color='darkgreen').highlight_min(color='darkred')
)