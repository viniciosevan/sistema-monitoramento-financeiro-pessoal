from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def gerar_relatorio_pdf(df, caminho='reports/relatorio_2025_01.pdf'):
    # 🔹 Cria a pasta reports/ se não existir
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    resumo = df.groupby('categoria')['valor'].sum()
    total = df['valor'].sum()

    c = canvas.Canvas(caminho, pagesize=A4)
    c.drawString(50, 800, f"Relatório Financeiro - {datetime.now().strftime('%B/%Y')}")
    c.drawString(50, 780, f"Total: R$ {total:.2f}")
    c.drawString(50, 760, "Gastos por categoria:")

    y = 740
    for cat, val in resumo.items():
        c.drawString(70, y, f"{cat}: R$ {val:.2f}")
        y -= 20

    c.save()