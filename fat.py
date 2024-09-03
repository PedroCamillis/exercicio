import json

with open('fat.json') as file:
    dados = json.load(file)

faturamentos = [item['faturamento'] for item in dados if item['faturamento'] > 0]
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_faturamento = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = len([f for f in faturamentos if f > media_faturamento])

print(f"Menor valor de faturamento ocorrido em um dia do mês: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}")
