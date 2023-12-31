import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
from openpyxl import load_workbook

def exibir_menu():
    print("Menu principal")
    print("1 - Carteira")
    print("2 - Compromissos financeiros")
    print("3 - Metas")
    print("4 - Emergências")
    print("5 - Dinheiro livre")
    print("6 - Dicas")
    print("7 - Gráficos")
    print("8 - Sair")

print("Bem-vindo ao nosso aplicativo EasyCash, agora ficou mais fácil gerenciar sua vida financeira")

carteira = 0  # Movido a inicialização da carteira para fora do loop
compromissos = [] # Lista para armazenar compromissos
metas = []  # Lista para armazenar metas financeiras


while True:
    exibir_menu()
    Opcao = int(input("Escolha uma opção: "))

    if Opcao == 1:
        print("Você quer:")
        print("1 - Visualizar carteira")
        print("2 - Adicionar valor")
        print("3 - Recuperar valor ")
        OpcaoCarteira = int(input("Digite a opção que deseja:"))

        if OpcaoCarteira == 1:
            def visualizar_carteira(carteira):
                print("Atualmente você tem: " + str(carteira))  # Convertido para string

            visualizar_carteira(carteira)

        elif OpcaoCarteira == 2:
            def adicionar_carteira(carteira):
                while True:
                    novo_valor = float(input("Digite o valor a ser adicionado: "))
                    if novo_valor == 0:
                        break
                    carteira = carteira + novo_valor
                    print(f"Novo valor da carteira: {carteira}")
                return carteira

            carteira = adicionar_carteira(carteira)
            print(f"Valor final da carteira: {carteira}")

        elif OpcaoCarteira == 3:
            def recuperar_carteira(carteira=None):
                while True:
                    sacar_valor = float(input("Digite o valor a ser resgatado: "))
                    if sacar_valor == 0:
                        break
                    elif carteira is not None:
                        if carteira >= sacar_valor:
                            carteira -= sacar_valor
                            print(f"Valor carteira: {carteira}")
                        else:
                            print("Saldo insuficiente. Operação não realizada.")
                    else:
                        print("Carteira vazia. Operação não realizada.")
                return carteira

            carteira = recuperar_carteira(carteira)
            print(f"Valor final da carteira: {carteira}")

    elif Opcao == 2:
        print("Opção 2 - Compromissos financeiros")
        compromissos = []  # Lista para armazenar compromissos financeiros


        def adicionar_compromisso():
            print("1 - Adicionar compromisso")
            novo_compromisso = input("Digite o compromisso: ")
            valor_compromisso = float(input("Digite o valor do compromisso: "))
            data_vencimento = input("Digite a data de vencimento (formato AAAA-MM-DD): ")

            compromisso = {
                'Compromisso': novo_compromisso,
                'Valor': valor_compromisso,
                'Data de Vencimento': data_vencimento
            }

            compromissos.append(compromisso)
            print("Compromisso adicionado com sucesso!")

        def gerenciar_compromissos():

            while True:
                print("MENU")
                print("1 - Adicionar compromisso")
                print("2 - Editar compromissos")
                print("3 - Excluir compromissos")
                print("4 - Visualizar compromissos")
                print("5 - Voltar ao menu principal")

                opcao_compromissos = int(input("Escolha uma opção: "))

                if opcao_compromissos == 1:
                    adicionar_compromisso()

                elif opcao_compromissos == 2:
                    print("Opção selecionada: 2 - Editar")

                    if not compromissos:
                        print("Não há compromissos para editar.")
                    else:
                        print("Compromissos disponíveis:")
                        for i, compromisso in enumerate(compromissos, 1):
                            print(f"{i} - {compromisso}")

                        indice_compromisso = int(input("Escolha o número do compromisso a ser editado: ")) - 1

                        if 0 <= indice_compromisso < len(compromissos):
                            novo_valor = input("Digite o novo valor para o compromisso: ")
                            compromissos[indice_compromisso] = novo_valor
                            print("Compromisso editado com sucesso!")
                        else:
                            print("Índice inválido. Tente novamente.")

                elif opcao_compromissos == 3:
                    print("Opção selecionada: 3 - Excluir")

                    if not compromissos:
                        print("Não há compromissos para excluir.")
                    else:
                        print("Compromissos disponíveis:")
                        for i, compromisso in enumerate(compromissos, 1):
                            print(f"{i} - {compromisso}")

                        indice_compromisso = int(input("Escolha o número do compromisso a ser excluído: ")) - 1

                        if 0 <= indice_compromisso < len(compromissos):
                            compromisso_removido = compromissos.pop(indice_compromisso)
                            print(f"Compromisso '{compromisso_removido}' removido com sucesso!")
                        else:
                            print("Índice inválido. Tente novamente.")

                elif opcao_compromissos == 4:
                    print("Opção selecionada: 4 - Visualizar")

                    if not compromissos:
                        print("Não há compromissos cadastrados.")
                    else:
                        for i, compromisso in enumerate(compromissos, 1):
                            print(f"{i} - {compromisso}")

                elif opcao_compromissos == 5:
                    print("Voltando......")

                    break  # Voltar ao menu principal

                else:
                    print("Opção inválida. Tente novamente.")


        gerenciar_compromissos()

    elif Opcao == 3:
        print("Opção 3 - Metas")

        while True:
            print("1 - Adicionar meta")
            print("2 - Editar meta")
            print("3 - Excluir meta")
            print("4 - Visualizar metas")
            print("5 - Voltar ao menu principal")
            opcao_metas = int(input("Escolha uma opção: "))

            if opcao_metas == 1:

                def adicionar_meta():

                    # metas = []
                    while True:
                        nome_meta = input("Qual o nome da meta que deseja realizar? ")
                        prazo_meta = input("Qual o prazo final para esta meta? ")
                        valor_meta = float(input("Qual o valor que deverá ser atingido para esta meta? "))

                        nova_meta = {'Nome': nome_meta, 'Prazo': prazo_meta, 'Valor': valor_meta}
                        metas.append(nova_meta)
                        print(nova_meta)

                        selecao = input(
                            "Caso deseje adicionar mais metas pressione 'Enter', caso deseje encerrar escreva 'Sair'")
                        if selecao.lower() == 'sair':
                            break  # Sai do loop se 'sair' for digitado'''
                            # else:
                            return nova_meta


                adicionar_meta()



            elif opcao_metas == 2:
                nome_meta_editar = input("Qual o nome da meta que deseja editar? ")

                try:
                    # Encontrar a meta pelo nome na lista de metas
                    meta_para_editar = next(meta for meta in metas if meta['Nome'] == nome_meta_editar)

                    # Obter o índice da meta na lista
                    index_meta = metas.index(meta_para_editar)

                    # Solicitar nova descrição
                    nova_descricao = input(f"Digite a nova descrição para '{nome_meta_editar}': ")

                    # Atualizar a descrição da meta no dicionário
                    meta_para_editar['Nome'] = nova_descricao

                    # Atualizar a meta na lista
                    metas[index_meta] = meta_para_editar

                    print(f"A meta '{nome_meta_editar}' foi editada com sucesso.")
                except StopIteration:
                    print(f"Meta '{nome_meta_editar}' não encontrada.")

            elif opcao_metas == 3:

                while True:
                    nome_meta_excluir = input("Qual o nome da meta que deseja excluir? ")

                    # Procura a meta na lista pelo nome

                    for meta in metas:
                        if meta['Nome'] == nome_meta_excluir:
                            metas.remove(meta)
                            print(f"A meta '{nome_meta_excluir}' foi excluída.")
                            break

                    else :
                        print(f"Meta '{nome_meta_excluir}' não encontrada.")

                    selecao = input("Deseja tentar excluir outra meta? (Digite 'Sim' ou 'Não') ")
                    if selecao.lower() != 'sim':
                        break

            elif opcao_metas == 4:
                print(metas)


            elif opcao_metas == 5:
                break  # Voltar ao menu principal

    elif Opcao == 4:
        print("Opção 4 - Emergências")

        def gerenciar_emergencias(carteira_emergencias):
            while True:
                print("1 - Adicionar fundos para emergências")
                print("2 - Utilizar fundos de emergências")
                print("3 - Visualizar saldo de emergências")
                print("4 - Voltar ao menu principal")
                opcao_emergencias = int(input("Escolha uma opção: "))

                if opcao_emergencias == 1:
                    valor_adicional = float(input("Digite o valor a ser adicionado para emergências: "))
                    carteira_emergencias += valor_adicional
                    print(f"Novo saldo de emergências: {carteira_emergencias}")

                elif opcao_emergencias == 2:
                    if carteira_emergencias > 0:
                        valor_utilizado = float(input("Digite o valor a ser utilizado para emergências: "))
                        if carteira_emergencias >= valor_utilizado:
                            carteira_emergencias -= valor_utilizado
                            print(f"Fundos de emergências utilizados. Novo saldo: {carteira_emergencias}")
                        else:
                            print("Saldo insuficiente em emergências.")
                    else:
                        print("Sem fundos de emergências disponíveis.")

                elif opcao_emergencias == 3:
                    print(f"Saldo de emergências disponível: {carteira_emergencias}")

                elif opcao_emergencias == 4:
                    break  # Voltar ao menu principal

                else:
                    print("Opção inválida. Tente novamente.")


        # Chamada para a função de gerenciamento de emergências
        carteira_emergencias = 0  # Inicialização da carteira de emergências
        gerenciar_emergencias(carteira_emergencias)

    elif Opcao == 5:
        print("Opção 5 - Dinheiro livre")

        def gerenciar_dinheiro_livre(carteira_dinheiro_livre):
            while True:
                print("1 - Adicionar dinheiro livre")
                print("2 - Utilizar dinheiro livre")
                print("3 - Visualizar saldo de dinheiro livre")
                print("4 - Voltar ao menu principal")
                opcao_dinheiro_livre = int(input("Escolha uma opção: "))

                if opcao_dinheiro_livre == 1:
                    valor_adicional = float(input("Digite o valor a ser adicionado como dinheiro livre: "))
                    carteira_dinheiro_livre += valor_adicional
                    print(f"Novo saldo de dinheiro livre: {carteira_dinheiro_livre}")

                elif opcao_dinheiro_livre == 2:
                    if carteira_dinheiro_livre > 0:
                        valor_utilizado = float(input("Digite o valor a ser utilizado como dinheiro livre: "))
                        if carteira_dinheiro_livre >= valor_utilizado:
                            carteira_dinheiro_livre -= valor_utilizado
                            print(f"Dinheiro livre utilizado. Novo saldo: {carteira_dinheiro_livre}")
                        else:
                            print("Saldo insuficiente de dinheiro livre.")
                    else:
                        print("Sem dinheiro livre disponível.")

                elif opcao_dinheiro_livre == 3:
                    print(f"Saldo de dinheiro livre disponível: {carteira_dinheiro_livre}")

                elif opcao_dinheiro_livre == 4:
                    break  # Voltar ao menu principal

                else:
                    print("Opção inválida. Tente novamente.")


        # Chamada para a função de gerenciamento de dinheiro livre
        carteira_dinheiro_livre = 0  # Inicialização da carteira de dinheiro livre
        gerenciar_dinheiro_livre(carteira_dinheiro_livre)

    elif Opcao == 6:
        print("Você selecionou a opção 6 - Dicas de Investimentos.")
        print("Dica 1: Diversifique seus investimentos para reduzir riscos.")
        print("Dica 2: Faça uma análise cuidadosa antes de tomar decisões de investimento.")
        print("Dica 3: Considere investir em ativos de longo prazo para o crescimento sustentável.")
        print("Para mais dicas acesse: 'https://riconnect.rico.com.vc/blog/dicas-de-investimento/'")

    elif Opcao == 7:
        print("7 - Gráficos")

        dados_financeiros = {
            'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='M'),
            'Receitas': [5000, 5500, 6000, 4800, 7000, 7500, 8000, 7200, 8500, 9000, 9500, 8800],
            'Despesas': [3000, 3200, 3500, 2800, 4000, 4200, 4500, 3800, 5000, 5200, 5500, 4800]
        }

        df = pd.DataFrame(dados_financeiros)
        df.set_index('Data', inplace=True)

        # Criar um gráfico de barras mensal
        plt.figure(figsize=(10, 6))
        df['Saldo'] = df['Receitas'] - df['Despesas']
        plt.bar(df.index.strftime('%b %Y'), df['Saldo'], color=['green' if x >= 0 else 'red' for x in df['Saldo']])
        plt.title('Saldo Mensal')
        plt.xlabel('Mês')
        plt.ylabel('Saldo')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Mostrar o gráfico
        plt.show()

    elif Opcao == 8:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")