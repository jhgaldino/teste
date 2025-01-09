import json
print("\n")
print("--------------------")
print("Atividade 1")
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print(f"SOMA = {SOMA}")  # 91 de saída

print("\n")
print("--------------------")
print("Atividade 2")
def fibonacci(num):
    # casos base
    a, b = 0, 1
    fib_sequencia = [a, b]
    
    while b <= num:
        a, b = b, a + b
        fib_sequencia.append(b)
    
    if num in fib_sequencia:
        return f"{num} pertence à sequência de Fibonacci"
    return f"{num} não pertence à sequência de Fibonacci"

# Teste
numero = 34
print(fibonacci(numero)) # resultado: 34 pertence à sequência de Fibonacci

print("\n")
print("--------------------")
print("Atividade 3")
def analise_vendas(data):
    # filtrar dias com vendas válidas
    vendas_validas = [day['valor'] for day in data if day['valor'] > 0]
    minimo_vendas = min(vendas_validas)
    maximo_vendas = max(vendas_validas)
    media_vendas = sum(vendas_validas) / len(vendas_validas)
    # contar dias com vendas acima da média
    media_dias = sum(1 for value in vendas_validas if value > media_vendas)
    
    return {
        'menor_valor': minimo_vendas,
        'maior_valor': maximo_vendas,
        'dias_acima_media': media_dias
    }

# criar arquivo chamado 'faturamento.json' para esse teste, com dias e valores
with open('faturamento.json') as f:
    data = json.load(f)
    
result = analise_vendas(data)
print(result)

print("\n")
print("--------------------")
print("Atividade 4")
def calcular_percentual_estados():
    vendas = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    total = sum(vendas.values())
    # calcular percentual de vendas por estado
    porcentagens = {
        estado: (valor / total) * 100 
        for estado, valor in vendas.items()
    }
    # exibir percentuais
    for estado, porcentagem in porcentagens.items():
        print(f"{estado}: {porcentagem:.2f}%")

# Teste
print("\nPercentuais por estado:")
calcular_percentual_estados()

print("\n")
print("--------------------")
print("Atividade 5")
def inverter_string(texto):
    texto_invertido = ""
    # inverter string
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido


# Teste
texto = "Hello World!"
print(f"\nString original: {texto}")
print(f"String invertida: {inverter_string(texto)}")