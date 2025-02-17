# 📊 Análise de Vendas com Previsão de Tendências

Este projeto realiza a análise de um conjunto de dados fictício de vendas, utilizando **Python, Pandas, Matplotlib e Scikit-Learn** para visualizar insights e prever tendências futuras nas vendas.

## 📌 Funcionalidades
- Carregamento e processamento de dados de vendas.
- Análise exploratória com visualizações gráficas.
- Construção de um modelo de **Regressão Linear** para previsão de vendas.
- Gráficos comparativos entre vendas reais e previsões.

## 🛠 Tecnologias Utilizadas
- **Python 3.10+**
- **Pandas** (manipulação de dados)
- **NumPy** (operações matemáticas)
- **Matplotlib** (visualização de dados)
- **Scikit-Learn** (modelo de regressão e avaliação)

## 📂 Estrutura do Projeto
```
analise_de_vendas/
├── data/
│   ├── mock_sales_data.csv   # Dataset fictício de vendas
├── notebooks/
│   ├── analise_vendas.ipynb  # Análise exploratória no Jupyter Notebook
├── scripts/
│   ├── process_data.py       # Script de processamento e previsão
├── README.md                 # Documentação do projeto
├── requirements.txt          # Dependências do projeto
```

## 🚀 Como Executar
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/analise_de_vendas.git
cd analise_de_vendas
```

### 2️⃣ Criar e ativar um ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o script de análise
```bash
python scripts/process_data.py
```

## 📊 Exemplo de Saída (Regressão Linear)
```text
Mean Squared Error: 125430.67
R-squared: 0.82
```

O gráfico gerado mostrará as **vendas reais ao longo do tempo** e a **previsão baseada no modelo de regressão linear**.

## 🔥 Melhorias Futuras
- Implementar modelos mais avançados como **ARIMA ou Redes Neurais**.
- Criar um **dashboard interativo** para visualização dinâmica.
- Incluir mais variáveis explicativas na previsão.

---
📌 **Autor:** Eduardo Xerxenevsky  
📧 Contato: eduardoxer@gmail.com

