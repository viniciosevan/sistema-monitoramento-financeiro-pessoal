import streamlit as st
from processador_dados import carregar_dados, resumo_por_categoria
from visualizacao import grafico_gastos_por_categoria, grafico_gastos_mensais
from relatorio import gerar_relatorio_pdf

st.title("📊 Monitoramento Financeiro Pessoal")

arquivo = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

if arquivo:
    df = carregar_dados(arquivo)
    st.dataframe(df.head())
    
    st.subheader("Resumo por Categoria")
    st.bar_chart(df.groupby('categoria')['valor'].sum().abs())

    if st.button("Gerar Gráficos"):
        grafico_gastos_por_categoria(df)
        grafico_gastos_mensais(df)
    
    if st.button("Gerar Relatório PDF"):
        gerar_relatorio_pdf(df)
        st.success("Relatório gerado com sucesso!")