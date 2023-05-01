import streamlit as st
import pandas as pd 
import json
import plotly.express as px
from sqlalchemy import create_engine
#from pandas.io import sql
import pymysql
import streamlit as st
#import mysql.connector as connection
import pandas as pd












col1, col2, col3 = st.columns(3)

with col1:
    st.image('https://download.logo.wine/logo/PhonePe/PhonePe-Logo.wine.png', width=150)
with col2:
    st.title("Phonepe")
    st.text('Datavisualation')    
with col3:
    pass

# year=st.selectbox('select year', ['Trans_2018_1', 'Trans_2018_2','Trans_2018_3','Trans_2018_4'])

col4, col5 = st.columns(2)


with col4:
    year = st.selectbox("Select Year", ('Trans_2018_1', 'Trans_2018_2','Trans_2018_3','Trans_2018_4'))
with col5:
    dataFilter = st.selectbox("Users or Transactions", ("count", "amount"))


engine = create_engine("mysql+pymysql://root:senthil12345@localhost:3306/phonepe",pool_size=1000, max_overflow=2000)
sql=f'select * from {year}'
mysql_df=pd.read_sql(sql, engine, index_col=None,chunksize=None)
mysql_df


if dataFilter:  
    fig = px.choropleth(
    mysql_df,                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color=dataFilter,
    color_continuous_scale='Greens')
    
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
  






