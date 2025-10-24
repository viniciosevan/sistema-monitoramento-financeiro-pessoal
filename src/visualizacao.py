import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def grafico_gastos_por_categoria(df):
    resumo = df.groupby('categoria')['valor'].sum().abs().sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=resumo.values, y=resumo.index, ax=ax)
    ax.set_title('Gastos por Categoria')
    ax.set_xlabel('Valor (R$)')
    ax.set_ylabel('Categoria')
    st.pyplot(fig)  

def grafico_gastos_mensais(df):
    mensais = df.groupby('mes')['valor'].sum()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x=mensais.index.astype(str), y=mensais.values, marker='o', ax=ax)
    ax.set_title('Evolução Mensal dos Gastos')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Total (R$)')
    st.pyplot(fig)