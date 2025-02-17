import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados(file_path):
    """Carrega o dataset."""
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])  
    return df

def analise_vendas_por_periodo(df):
    """Realiza a análise de vendas por período (mensal)."""
    df['month'] = df['date'].dt.to_period('M')  
    vendas_por_mes = df.groupby('month')['total_price'].sum()

    plt.figure(figsize=(10, 6))
    vendas_por_mes.plot(kind='line', marker='o', color='blue')
    plt.title('Vendas Totais por Mês')
    plt.xlabel('Mês')
    plt.ylabel('Total de Vendas (R$)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return vendas_por_mes

def visualizar_produtos_vendidos(df):
    """Cria um gráfico de barras para os produtos mais vendidos."""
    top_products = df['product_category'].value_counts().head(5)
    plt.figure(figsize=(10, 6))
    top_products.plot(kind='bar', color='skyblue')
    plt.title('Produtos Mais Vendidos')
    plt.xlabel('Categoria de Produto')
    plt.ylabel('Número de Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def analise_vendas_por_categoria(df):
    """Realiza a análise de vendas por categoria de produto."""
    vendas_por_categoria = df.groupby('product_category')['total_price'].sum()

    plt.figure(figsize=(10, 6))
    vendas_por_categoria.plot(kind='bar', color='orange')
    plt.title('Vendas Totais por Categoria de Produto')
    plt.xlabel('Categoria de Produto')
    plt.ylabel('Total de Vendas (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return vendas_por_categoria

def main():

    vendas_por_mes = analise_vendas_por_periodo(df)
    print(vendas_por_mes)
    
    visualizar_produtos_vendidos(df)
    
    vendas_por_categoria = analise_vendas_por_categoria(df)
    print(vendas_por_categoria)

if __name__ == '__main__':

    file_path = 'data/mock_sales_data.csv'
    
    df = carregar_dados(file_path)
    main()
