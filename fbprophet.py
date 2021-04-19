from fbprophet import Prophet
from fbprophet.plot import plot_plotly

df_pred = df_result[['date','cumsum']]
df_pred = df_pred.rename(columns={'date':'ds','cumsum':'y'})  # change the column name

# model prediction
m = Prophet()
m.fit(df_pred)
future = m.make_future_dataframe(periods=240)
forecast = m.predict(future)

# chart
f_pred = plot_plotly(m, forecast)
st.plotly_chart(f_pred)
