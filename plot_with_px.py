import sqlite3
import pandas as pd
import plotly.express as px

connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql("""SELECT * FROM plotting;""", con=connection)
connection.close()

fig = px.scatter(plotting_df, x="gdp_per_capita", y="life_expectancy",
                 animation_frame="dt_year", animation_group="country_name",
                 size="population", color="continent", hover_name="country_name",  # hover_name就是你移動滑鼠時顯示的資料為何,設一個變數給它
                 size_max=100, range_x=[500, 100000], range_y=[20, 90], log_x=True,
                 title="Gapminder Clone 1800-2023")
fig.write_html("gapminder_clone.html", auto_open=True)