from openpyxl import Workbook

arquivo_excel = Workbook()

planilha1 = arquivo_excel.active

planilha1['A1'] = 'NOME_PRODUTO'
planilha1['B1'] = 'VALOR_PRODUTO'
planilha1['C1'] = 'COR'
planilha1['A2'] = "Iphone 11"
planilha1['B2'] = (f'R${4920.85}')
planilha1['C2'] = "PRETO"

arquivo_excel.save("relatorio.xlsx")