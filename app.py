from random import choice, choices
from os import linesep



# Constante que contém os dados a serem escolhidos
DADOS_ARBITRARIOS = {
    # Nomes
    '1': (  "Julia", "Enzo", "Ana", "Pedro", "Larissa", "Lucas", "Mariana",
            "Gabriel", "Isabela", "Thiago", "Beatriz", "Matheus", "Carolina",
            "Felipe", "Camila", "Vinicius", "Amanda", "Jose", "Isabel",
            "Leonardo" 
        ), 
    # Tipos de email
    '2': (
            'hotmail', 'outlook', 'gmail', 'yahoo'
        ), 
    # Os DDs válidos no Brasil
    '3': (  "92", "97", "93", "94", "95", "96", "91", "83", "68", "69", 
            "63", "79", "88", "81", "87", "82", "84", "83", "86", "89", 
            "77", "75", "98", "99", "71", "73", "61", "62", "64", "65", 
            "66", "67", "11", "12", "13", "14", "15", "16", "17", "18", 
            "19", "21", "22", "24", "27", "28", "31", "32", "33", "34", 
            "35", "37", "38", "41", "42", "43", "44", "45", "46", "47", 
            "48", "49"
        ), 
    # Cidades
    '4': (  "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador",
            "Brasília", "Curitiba", "Fortaleza", "Manaus", "Recife",
            "Porto Alegre", "Goiânia", "Belém", "São Luís", "Campinas",
            "São José", "Natal", "Santos", "Florianópolis", "João Pessoa",
            "Vitória"
        ), 
    # Estados
    '5': (  "São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia",
            "Distrito Federal", "Paraná", "Ceará", "Amazonas",
            "Pernambuco", "Rio Grande do Sul", "Goiás", "Pará",
            "Maranhão", "Santa Catarina", "Sergipe", "Paraíba",
            "Rio Grande do Norte", "Espirito Santo"
        )
}



def retorna_mensagem_inicial() -> str:
    mensagem_inicial = 'Bem-vindo ao Gerador de Dados de Testes - '\
        f'Para finalizar o programa, digite "parar"{linesep}'\
        f'{30 * "-"}{linesep}'\
        f'Escolha uma ou mais opções abaixo a serem geradas aleatóriamente.{linesep}'\
        f'[1] - Nome{linesep}'\
        f'[2] - E-mail{linesep}'\
        f'[3] - Telefone{linesep}'\
        f'[4] - Cidade{linesep}'\
        f'[5] - Estado{linesep}'\
        'Digite uma ou mais opções: '
    return mensagem_inicial


def validar_mensagem_inicial() -> str:
    escolha_usuario = input(retorna_mensagem_inicial()).lower().strip()
    while True:
        if escolha_usuario != ',' and (escolha_usuario in ('1,2,3,4,5') or escolha_usuario == 'parar'):
            return escolha_usuario
        print("Ops! Parace que você digitou uma opção inválida.")
        escolha_usuario = input(retorna_mensagem_inicial()).lower().strip()
        

def retorna_mensagem_salvar_txt() -> str:
    return f'{30 * "-"}{linesep}Gostaria de salvar os dados em um arquivo de texto?(s/n) '


def validar_mensagem__salvar_txt() -> str:
    escolha_usuario = input(retorna_mensagem_salvar_txt()).lower().strip()
    while True:
        if escolha_usuario == 's' or escolha_usuario == 'n':
            return escolha_usuario
        print("Ops! Parace que você digitou uma opção inválida.")
        escolha_usuario = input(retorna_mensagem_salvar_txt()).lower().strip()


def exibe_valores(valores: list | tuple):
    for valor in valores:
        print(valor)
    print(30 * '-')


def salva_dados_em_txt(valores):
    with open('dados.txt', 'a', encoding='utf-8', newline='') as file:
        for valor in valores:
            file.write(f'{valor}{linesep}')



while True:
    
    escolha_operacao = validar_mensagem_inicial()

    if escolha_operacao == 'parar':
        print("Encerrando o programa")
        break

    else:
        
        opcoes_escolhidas = escolha_operacao.split(',')
        respostas = []

        for opcao_escolhida in opcoes_escolhidas:
            
            if opcao_escolhida == '2': 
                nome_aleatorio = choice(DADOS_ARBITRARIOS["1"]).lower()
                email_aleatorio = choice(DADOS_ARBITRARIOS[opcao_escolhida])
                respostas.append(f'{nome_aleatorio}@{email_aleatorio}.com')

            elif opcao_escolhida == '3':
                ddd_aleatorio = choice(DADOS_ARBITRARIOS[opcao_escolhida])
                telefone_aleatorio = "".join(choices("1234567890", k=8))
                respostas.append(f'55{ddd_aleatorio}9{telefone_aleatorio}')

            else:

                valor_aleatorio = choice(DADOS_ARBITRARIOS[opcao_escolhida])
                respostas.append(valor_aleatorio)


        opcao_salvar_txt = validar_mensagem__salvar_txt() 
        
        if opcao_salvar_txt == 'n':
            exibe_valores(respostas)

        else:
            exibe_valores(respostas)
            salva_dados_em_txt(respostas)
        
       
        


