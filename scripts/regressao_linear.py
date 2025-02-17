import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('data/mock_sales_data.csv')


df['date'] = pd.to_datetime(df['date'])


df['year_month'] = df['date'].dt.to_period('M')


df_grouped = df.groupby('year_month')['total_price'].sum().reset_index()


df_grouped['time_index'] = np.arange(len(df_grouped))


X = df_grouped[['time_index']]  
y = df_grouped['total_price'] 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

plt.figure(figsize=(12, 6))
plt.plot(df_grouped['year_month'].astype(str), df_grouped['total_price'], label='Vendas Reais', marker='o', linestyle='-')
plt.plot(df_grouped.iloc[len(X_train):]['year_month'].astype(str), y_pred, color='red', label='Previsão (Regressão Linear)', marker='x', linestyle='--')

plt.xticks(rotation=45)
plt.xlabel('Mês/Ano')
plt.ylabel('Vendas Totais')
plt.title('Previsão de Vendas Totais por Mês')
plt.legend()
plt.grid()
plt.show()
