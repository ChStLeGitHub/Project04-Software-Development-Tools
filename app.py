import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('/Users/cslewicki/Desktop/Sprint4Project/vehicles_us.csv')

price_data = px.histogram(car_data[car_data['price'] <= 50000],
                          color_discrete_sequence=['blue'],
                          labels={'price': 'Price of Car (In Dollars)'},
                          nbins=10,
                          opacity=0.5,
                          title='Number of Advertised Cars By Price ($50,000 Max)',
                          x='price')

price_data.update_layout(autosize=False, width=1000, height=600)

price_data.update_traces(marker_line_color='black', marker_line_width=1.5)

price_data.update_xaxes(tickvals=[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000],
                        ticktext=[0, '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K', '50K'])

price_data.update_yaxes(title_text='Number of Cars',
                        tickvals=[0, 1000, 2000, 3000, 4000,
                                  5000, 6000, 7000, 8000, 9000, 10000],
                        ticktext=[0, '1K', '2K', '3K', '4K', '5K', '6K', '7K', '8K', '9K', '10K'])


miles_vs_price = px.scatter(car_data[car_data['odometer'] > 0][car_data['odometer'] <= 300000][car_data['price'] <= 50000],
                            x='odometer',
                            y='price',
                            title='Number of Miles Driven By Used Cars vs Price Scatterplot',
                            trendline='ols',
                            trendline_color_override='orange')

miles_vs_price.update_xaxes(title_text='Number of Miles Driven',
                            tickvals=[0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000,
                                       160000, 170000, 180000, 190000, 200000, 210000, 220000, 230000, 240000, 250000, 260000, 270000, 280000, 290000, 300000])

miles_vs_price.update_yaxes(title_text='Price of Car')

st.header('Start of Sprint 4 Project Plots')
st.plotly_chart(price_data)
st.plotly_chart(miles_vs_price)
checkbox_value = st.checkbox('Check Here When Done Looking At The Plots')
if checkbox_value:
    st.header('End of Sprint 4 Project Plots')
