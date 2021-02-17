import pandas as pd
df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
df
count=df['continent'].value_counts().tolist()
count
continent=['Asia','Africa','Americans','Europe','Oceania']
import plotly.express as px
pie_chart = px.pie(df, values=count, names=continent, color=continent, hover_name=continent)
import plotly
pie_chart.update_traces(textposition ='inside',textinfo='percent+label')
plotly.offline.plot(pie_chart,filename='Piechart1.html')
'Piechart1.html'