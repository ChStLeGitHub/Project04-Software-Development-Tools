import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

# The code for preprocessing the data begins on the next line.
car_data = car_data.drop_duplicates()
# Sometimes datasets have rows that are exact duplicates, and it is a good idea to drop them if there are any.

# The following code replaces all of the null 'model_year' values with the median model year of the corresponding model.
median_model_year = car_data.groupby('model')['model_year'].median()


def fill_missing_model_year(row):
    if pd.isnull(row['model_year']):
        return median_model_year[row['model']]
    else:
        return row['model_year']


car_data['model_year'] = car_data.apply(fill_missing_model_year, axis=1)

# It doesn't make sense for the model years to be float values. They are now integer values.
car_data['model_year'] = car_data['model_year'].astype(int)

# The following code replaces all of the null 'cylinders' values with the median number of cylinders of the corresponding model.
median_cylinders = car_data.groupby('model')['cylinders'].median()


def fill_missing_cylinders(row):
    if pd.isnull(row['cylinders']):
        return median_cylinders[row['model']]
    else:
        return row['cylinders']


car_data['cylinders'] = car_data.apply(fill_missing_cylinders, axis=1)

car_data['cylinders'] = car_data['cylinders'].astype(int)
# It doesn't make sense for the number of cylinders to be float values. They are now integer values.

# The following code replaces all of the null 'odometer' values with the median odometer value of the corresponding model year.
median_odometer = car_data.groupby('model_year')['odometer'].median()


def fill_missing_odometer(row):
    if pd.isnull(row['odometer']):
        return median_odometer[row['model_year']]
    else:
        return row['odometer']


car_data['odometer'] = car_data.apply(fill_missing_odometer, axis=1)

car_data['paint_color'] = car_data['paint_color'].fillna('Unknown')
# It seems appropriate to me to replace missing paint color values with 'Unknown'.

car_data['is_4wd'] = car_data['is_4wd'].replace(1.0, 'Yes')
car_data['is_4wd'] = car_data['is_4wd'].fillna('No')
# I noticed that all of the is_4wd values were either 1.0 or NaN. I think it is more intuitive to use the words "Yes" and "No" instead.

# The code for the histogram begins on the next line.
price_data = px.histogram(car_data[car_data['price'] <= 50000],
                          color_discrete_sequence=['blue'],
                          labels={'price': 'Price of Car (In Dollars)'},
                          nbins=10,
                          opacity=0.5,
                          title='Number of Advertised Cars By Price ($50,000 Max)',
                          x='price')

price_data.update_layout(width=1000, height=600)

price_data.update_traces(marker_line_color='black', marker_line_width=1.5)

price_data.update_xaxes(tickvals=[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000],
                        ticktext=[0, '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K', '50K'])

price_data.update_yaxes(title_text='Number of Cars',
                        tickvals=[0, 1000, 2000, 3000, 4000, 5000, 6000, 7000,
                                  8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],
                        ticktext=[0, '1K', '2K', '3K', '4K', '5K', '6K', '7K', '8K', '9K', '10K', '11K', '12K', '13K', '14K', '15K'])

# The code for the scatterplot begins on the next line.
miles_vs_price = px.scatter(car_data[car_data['odometer'] > 0][car_data['odometer'] <= 300000][car_data['price'] <= 50000],
                            x='odometer',
                            y='price',
                            title='Number of Miles Driven By Used Cars vs Price Scatterplot',
                            trendline='ols',
                            trendline_color_override='orange')

miles_vs_price.update_xaxes(title_text='Number of Miles Driven',
                            tickvals=[0, 20000, 40000, 60000, 80000, 100000, 120000, 140000,
                                       160000, 180000, 200000, 220000, 240000, 260000, 280000, 300000])

miles_vs_price.update_yaxes(title_text='Price of Car')

# The code for what appears on the Render app begins on the next line.
st.header('Start of Sprint 4 Project Plots')
st.plotly_chart(price_data)
st.plotly_chart(miles_vs_price)
checkbox_value = st.checkbox('Check Here When Done Looking At The Plots')
if checkbox_value:
    st.header('End of Sprint 4 Project Plots')
