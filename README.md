# Gerador-de-Dados-para-teste-App-no-Terminal-

***

## Descrição:

Este programa gera dados aleatórios para teste. Você pode gerar com ele dados arbitrários do seguinte tipo: nomes, emails, telefones, cidades e estados.

***

## Requisitos:

* Ter o Python 3 instalado no seu computador. 

***


## Como rodar o projeto?

Assim que clonar este código, sugiro que você crie um ambiente virtual isolando os arquivos que estão no seu computador do diretório do projeto.

### Criando ambiente virtual com Python:

#### Requisitos:

* Ter habilitado a opção **Add to Path** na hora da instalação do Python.

#### Passo a passo

1. Clone o projeto.

2. Estando dentro da pasta do projeto, abra o seu terminal.

CASO ESTEJA NO **WINDOWS**, RODE O COMANDO ABAIXO E AGUARDE A CRIAÇÃO:

```
python -m venv nome_do_ambiente_virtual
```

**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

CASO ESTEJA NO LINUX OU NO MAC, RODE O COMANDO ABAIXO E A AGUARDE A CRIAÇÃO:

```
python3 -m venv nome_do_ambiente_virtual
```
**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

3. Ative o ambiente virtual através do seu terminal:

NO CASO DO **WINDOWS**, RODE:
```
nome_do_ambiente_virtual\Scripts\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

NO CASO DO **LINUX** OU **MAC**, RODE:

```
source nome_do_ambiente_virtual\bin\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

***

### Instalando bibliotecas necessárias:


Feito isso, vamos instalar as bibliotecas necessárias através do arquivo requirements.txt:
No **Windows**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip install -r requirements.txt
```
No **Linux** ou **MAC**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip3 install -r requirements.txt
```
Pronto! Você está apto para rodar o projeto.

***

### Gerando executável:

**OBS: PARA GERAR O EXECUTÁVEL VOCÊ PRECISA BAIXAR O CONTEÚDO DO ARQUIVO requirements.txt. COMO FAZER ISSO FOI EXPLICADO ACIMA.**

Caso você queira um executável do projeto. Você deve ter executado as etapas anteriores. - ATÉ A PARTE DE INSTALAR AS BIBLIOTECAS DO ARQUIVO requirements.txt.

Feito isso, você deve estar com o seu ambiente virtual ativado e abrir o seu terminal na pasta raiz do projeto.

Estando lá, digite o seguinte comando

NO **WINDOWS**:
```
python setup.py build
```

NO **LINUX** OU NO **MAC**:
```
python3 setup.py build
```

Uma pasta **build**, com um arquivo **app.exe** deve ser gerada.
O ARQUIVO **app.exe** será o seu executável.