import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def carregar_dados(file_path):
    """Carrega o dataset."""
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date']) 
    return df

def analise_vendas(df):
    """Realiza a análise exploratória dos dados."""
    total_sales = df['total_price'].sum()
    avg_ticket = df['total_price'].mean()

    top_products = df['product_category'].value_counts().head(5)

    top_payment_methods = df['payment_method'].value_counts()

    top_cities = df['customer_city'].value_counts().head(5)

    return {
        "Total de Vendas (R$)": round(total_sales, 2),
        "Ticket Médio (R$)": round(avg_ticket, 2),
        "Produtos Mais Vendidos": top_products.to_dict(),
        "Métodos de Pagamento Mais Utilizados": top_payment_methods.to_dict(),
        "Cidades com Mais Compras": top_cities.to_dict(),
    }

def visualizar_produtos_vendidos(df):
    """Cria um gráfico de barras para os produtos mais vendidos."""
    top_products = df['product_category'].value_counts().head(5)
    plt.figure(figsize=(10, 6))
    top_products.plot(kind='bar', color='skyblue')
    plt.title('Produtos Mais Vendidos')
    plt.xlabel('Categoria de Produto')
    plt.ylabel('Número de Vendas')
    plt.xticks(rotation=45)
    plt.show()

def visualizar_metodos_pagamento(df):
    """Cria um gráfico de pizza para os métodos de pagamento."""
    payment_method_counts = df['payment_method'].value_counts()
    plt.figure(figsize=(8, 8))
    payment_method_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(payment_method_counts)))
    plt.title('Distribuição dos Métodos de Pagamento')
    plt.ylabel('')
    plt.show()

if __name__ == "__main__":
    file_path = 'data/mock_sales_data.csv'
    
    df = carregar_dados(file_path)

    analise = analise_vendas(df)
    print("Análise de Vendas:")
    for key, value in analise.items():
        print(f"{key}: {value}")

    visualizar_produtos_vendidos(df)
    visualizar_metodos_pagamento(df)

