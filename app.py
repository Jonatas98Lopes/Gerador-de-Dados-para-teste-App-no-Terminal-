from random import choice, choices

#1. FAÇA TUDO ABAIXO:
while True:
    pass
    #2. EXIBA A MENSAGEM: "
    mensagem_inicial = '''Bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa, digite "parar"
       ------------------------------
       Escolha uma ou mais opções abaixo a serem geradas aleatóriamente.
       [1] - Nome
       [2] - E-mail
       [3] - Telefone
       [4] - Cidade
       [5] - Estado
       Digite uma ou mais opções: '''
    #3. RECEBE A ENTRADA DO USUÁRIO. S
    escolha_operacao = input(mensagem_inicial).lower().strip()

    #4. CASO A OPÇÃO SELECIONADA SEJA "parar":
    if escolha_operacao == 'parar':
        # a. SERÁ EXIBIDA A SEGUINTE MENSAGEM: "Encerrando o programa"
        print("Encerrando o programa")
        # b. O PROGRAMA DEVE ENCERRADO.
        break
    #5. CASO ELE DIGITE UMA OU MAIS DAS OPÇÕES A SEGUIR: 1,2,3,4,5:
    elif escolha_operacao in ('1,2,3,4,5'):
        # DEVEMOS TER UMA CONSTANTE QUE TERÁ OS NOMES QUE PODEM SER GERADOS.
        # DEVEMOS TER OUTRA CONSTANTE  QUE TERÁ OS SERVIDORES DE E-MAIL QUE PODEM SER GERADOS
        # DEVEMOS TER OUTRA CONSTANTE  QUE TERÁ OS SERVIDORES DE E-MAIL QUE PODEM SER GERADOS
        # DEVEMOS TER UMA CONSTANTE QUE TERÁ OS NOMES DAS CIDADES QUE PODEM SER GERADAS.
        # DEVEMOS TER UMA CONSTANTE  QUE TERÁ OS NOMES DOS ESTADOSQUE PODEM SER GERADOS.
        DADOS_ARBITRARIOS = {
            '1': (  "Julia",
                    "Enzo",
                    "Ana",
                    "Pedro",
                    "Larissa",
                    "Lucas",
                    "Mariana",
                    "Gabriel",
                    "Isabela",
                    "Thiago",
                    "Beatriz",
                    "Matheus",
                    "Carolina",
                    "Felipe",
                    "Camila",
                    "Vinicius",
                    "Amanda",
                    "Jose",
                    "Isabel",
                    "Leonardo" 
                ), 
            '2': (
                    'hotmail',
                    'outlook',
                    'gmail',
                    'yahoo'
                 ), 
            '3': ( # Os DDs válidos no Brasil
                "92", "97", "93", "94", "95", 
                "96", "91", "83", "68", "69", 
                "63", "79", "88", "81", "87", 
                "82", "84", "83", "86", "89", 
                "77", "75", "98", "99", "71", 
                "73", "61", "62", "64", "65", 
                "66", "67", "11", "12", "13", 
                "14", "15", "16", "17", "18", 
                "19", "21", "22", "24", "27", 
                "28", "31", "32", "33", "34", 
                "35", "37", "38", "41", "42", 
                "43", "44", "45", "46", "47", 
                "48", "49"), 

            '4': (  "São Paulo",
                    "Rio de Janeiro",
                    "Belo Horizonte",
                    "Salvador",
                    "Brasília",
                    "Curitiba",
                    "Fortaleza",
                    "Manaus",
                    "Recife",
                    "Porto Alegre",
                    "Goiânia",
                    "Belém",
                    "São Luís",
                    "Campinas",
                    "São José",
                    "Natal",
                    "Santos",
                    "Florianópolis",
                    "João Pessoa",
                    "Vitória"
                ), 
            '5': (  "São Paulo",
                    "Rio de Janeiro",
                    "Minas Gerais",
                    "Bahia",
                    "Distrito Federal",
                    "Paraná",
                    "Ceará",
                    "Amazonas",
                    "Pernambuco",
                    "Rio Grande do Sul",
                    "Goiás",
                    "Pará",
                    "Maranhão",
                    "Santa Catarina",
                    "Sergipe",
                    "Rio Grande do Norte",
                    "Paraíba",
                    "Espirito Santo"
                )}
        opcoes_escolhidas = escolha_operacao.split(',')
        # DEVEMOS UMA VARIÁVEL RESPOSTA
        resposta = []
       # PARA CADA UMA DAS OPÇÕES SELECIONADAS:
        for opcao_escolhida in opcoes_escolhidas:
            if opcao_escolhida == '3':
                resposta.append(f'55{choice(DADOS_ARBITRARIOS[opcao_escolhida])}
                    {choices("1234567890", k=8)}')
                resposta.append(
        # VAMOS ARMAZENADO UM RESULTADO ARBITRÁRIOS NA VARIÁVEL RESPOSTA
                    f'55{choice(DADOS_ARBITRARIOS[opcao_escolhida])}{choices("1234567890", k=8)}')

            else:
                resposta.append(choice(DADOS_ARBITRARIOS[opcao_escolhida]))

        



        # a. VOCÊ DEVE EXIBIR A SEGUINTE MENSAGEM :
        #  "
        #  ------------------------------
        #   Gostaria de salvar os dados em um arquivo de texto?(s/n)" 
        
        # SE ELE ESCOLHER 'n':
          # VAMOS EXIBIR OS DADOS NA TELA
        # SE ELE ESCOLHER 's':
          # VAMOS EXIBIR OS DADOS NA TELA
          # SALVAR OS DADOS NUM ARQUIVO TXT CHAMADO: dados.txt, CADA DADOS UM EMBAIXO DO OUTRO.
          # OBS: OS DADOS QUE ESTAVAM PRESENTES NO ARQUIVO dados.txt NÃO PODEM SER APAGADOS
        # QUALQUER OUTRA OPCAO DIGITADA:
          # "------------------------------
           #Ops! Parace que você digitou uma opção inválida.
           #Opções válidas: 
           #["s"] - Salvar dados em um arquivo txt 
           #["n"] - Não salvar dados em um arquivo txt
          # Reixibir a mensagem anterior para o usuário escolher



    #6. SE ELE DIGITAR ALGO DIFERENTE DISSO:
        #a. , O PROGRAMA DEVE EXIBIR O SEGUINTE: 
        #    "------------------------------
        #    Ops! Parace que você digitou uma opção inválida.
        #    Opções válidas: 
        #    [1] - Nome
        #    [2] - E-mail
        #    [3] - Telefone
        #    [4] - Cidade
        #    [5] - Estado
        #    ou ["parar"] para encerrar o programa."
        #    ------------------------------
          
        #b. Reiniciar o programa do zero.
        


