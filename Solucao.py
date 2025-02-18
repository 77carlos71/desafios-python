import json
import os

# Função para pausar a execução até o usuário pressionar ENTER
def pausa():
    input("\nPressione ENTER para continuar...")

# Problema 1: Soma dos números de 1 até 13
def problema1():
    print("===============")
    print("Problema 1: Cálculo da Soma (1 até 13)")

    while True:  # Loop até o valor válido ser digitado
        try:
            n = int(input("Digite um número de 1 até 13: "))
            
            # Verifica se o número está no intervalo correto
            if n < 1 or n > 13:
                print("Ops! Você só pode digitar números de 1 até 13.")
                continue  # Retorna ao loop e solicita a entrada novamente

            break  # Sai do loop se o número for válido

        except ValueError:
            print("Ops! Valor inválido. Por favor, digite um número inteiro.")
    
    # Aqui a gente define o limite e começa a soma com 0
    INDICE, SOMA, K = n, 0, 0
    
    # Enquanto o contador for menor que o número escolhido, soma os números
    while K < INDICE:
        K += 1
        SOMA += K
    
    print(f"Resultado: SOMA = {SOMA}")
    print("===============")


# Problema 2: Verificação se um número está na sequência de Fibonacci
def problema2():
    print("===============")
    print("Problema 2: Checando a Sequência de Fibonacci")
    
    try:
        n = int(input("Digite um número para ver se está na sequência de Fibonacci: "))
    except ValueError:
        print("Ops! Valor inválido. Use um número inteiro.")
        print("===============")
        pausa()
        return
    
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
        
    if n in fib:
        print(f"O número {n} faz parte da sequência de Fibonacci.")
    else:
        print(f"O número {n} NÃO faz parte da sequência de Fibonacci.")
    print("===============")
    pausa()

# Problema 3: Analisando o faturamento diário
def problema3():
    print("===============")
    print("Problema 3: Analisando o Faturamento Diário")

    faturamento_json = '''
    {
      "1": 2000,
      "2": 2500,
      "3": 0,
      "4": 3000,
      "5": 3500,
      "6": 0,
      "7": 4000,
      "8": 1500,
      "9": 5000,
      "10": 2500,
      "11": 3000,
      "12": 4000,
      "13": 3500,
      "14": 0
    }
    '''

    faturamento = json.loads(faturamento_json)
    validos = [valor for valor in faturamento.values() if valor > 0]
    if not validos:
        print("Não teve nenhum dia com faturamento.")
        print("===============")
        pausa()
        return

    menor, maior = min(validos), max(validos)
    media = sum(validos) / len(validos)
    dias_acima_media = sum(1 for valor in validos if valor > media)
    
    print(f"Menor faturamento diário: R${menor:.2f}")
    print(f"Maior faturamento diário: R${maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
    print("===============")
    pausa()

# Problema 4: Percentual de faturamento por estado
def problema4():
    print("===============")
    print("Problema 4: Percentual de Faturamento por Estado")
    
    faturamento_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    total = sum(faturamento_estado.values())
    for estado, valor in faturamento_estado.items():
        print(f"{estado}: {(valor / total * 100):.2f}%")
    print("===============")
    pausa()

# Problema 5: Inverter uma string sem usar funções prontas tipo reverse
def problema5():
    print("===============")
    print("Problema 5: Inversão de String")

    s = input("Digite uma string para inverter: ")
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    
    print("String original:", s)
    print("String invertida:", invertida)
    print("===============")
    pausa()

# Menu de Opções
def menu():
    print("\n========================")
    print("Menu de Opções:")
    print("1 - Problema 1: Soma (1 até 13)")
    print("2 - Problema 2: Sequência de Fibonacci")
    print("3 - Problema 3: Faturamento Diário")
    print("4 - Problema 4: Percentual por Estado")
    print("5 - Problema 5: Inverter String")
    print("6 - Sair")
    print("========================")

# Função para exibir o menu e chamar o problema selecionado pelo usuário
def main():
    while True:

        menu()
        escolha = input("Escolha uma opção (1-6): ")
        
        if escolha == '1':
            problema1()
        elif escolha == '2':
            problema2()
        elif escolha == '3':
            problema3()
        elif escolha == '4':
            problema4()
        elif escolha == '5':
            problema5()
        elif escolha == '6':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            pausa()

if __name__ == "__main__":
    main()
