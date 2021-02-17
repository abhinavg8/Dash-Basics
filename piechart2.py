import plotly.express as px

import pandas as pd

df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                  color='lifeExp')
fig.show()