import pandas as pd
import plotly.figure_factory as ff

file = pd.read_csv("data.csv")
fig = ff.create_distplot([file["Avg Rating"].tolist()], ["Rating"])
fig.show()