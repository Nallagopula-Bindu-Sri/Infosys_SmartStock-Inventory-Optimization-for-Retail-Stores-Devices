import pandas as pd
import plotly.express as px
# Load your dataset
file_path = ("/Users/bindusri/Desktop/smart stock code/smart_stock_retail_dataset.csv")
data = pd.read_csv(file_path)
# Clean column names
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")
data['date'] = pd.to_datetime(data['date'])
# Create interactive scatter plot using Plotly
fig = px.scatter(
    data,
    x='date',
    y='stock_price',
    title='Stock Price Over Time',
    labels={'date': 'Date', 'stock_price': 'Stock Price'},
    template='plotly_white'
)
# Add gridlines
fig.update_layout(
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightGray'),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightGray')
)
# Show figure
fig.show()