import sys
import os
from cx_Freeze import setup, Executable
 
arquivos = []
 

 
configuracao = Executable(
    script='app.py', 
    icon='icone.ico'
)
setup(
    name = 'Gerador de Dados Aleatórios', 
    version = '1.0', 
    description = 'Com esse programa, você pode automatizar o processo de criação de dados aleatórios, incluindo nomes, e-mails, telefones(Bresil), cidades e estados.',
    author = 'Jonatas L. de Sousa',            
    options = {'build_exe': {'include_files': arquivos, "include_msvcr":True}}, 
    executables = [configuracao]
)