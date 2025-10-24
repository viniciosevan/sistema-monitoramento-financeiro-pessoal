import pandas as pd

def carregar_dados(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    df['data'] = pd.to_datetime(df['data'])
    df['mes'] = df['data'].dt.to_period('M')
    return df

def resumo_por_categoria(df):
    return df.groupby('categoria')['valor'].sum().sort_values()
def gastos_mensais(df):
    return df.groupby('mes')['valor'].sum()

def media_gastos(df):
    return df[df['valor'] < 0]['valor'].mean()

def alertar_gastos_acima_media(df):
    media = abs(media_gastos(df))
    gastos_mes = abs(df[df['valor'] < 0]['valor'].sum())
    if gastos_mes > 1.2 * media:
        return f"Atenção! Gastos acima da média ({gastos_mes:.2f} > {media:.2f})"
    return "Gastos dentro da média."