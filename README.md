# Desafio Bootcamp Santander/DIO - Simulando um Malware de Captura de Dados Simples em Python e Aprendendo a se Proteger

Todo o projeto foi baseado na seguinte configuração abaixo:

Pycharm: https://www.jetbrains.com/pycharm/download/

Projeto 1: Ransoware
- Utilizando a biblioteca do Fernet, foi feito o import do cryptography.fernet para auxiliar a criação do codigo
- Dois codigos foram criados (criptografar.py [para criptografar os arquivos] e descriptografar.py [para descriptografar os arquivos]
- Foram utilizados dois arquivos para simular os arquivos criptografados (dentro da pasta test_files [senha.txt e dados.txt])
 
Ao executar o criptografar.py, os dados armazenados na pasta test_files são criptografados e dois aquivos sao criados, um chamado LEIA ISSO.txt é criado com as instruções e o outro chave.key para ser usado para descriptografar. (Como foi feito para meios educativos a key é visivel)

Depois dos dados serem criptografados, executando o arquivo descriptografar.py, ele lê o arquivo chave.key para conseguir descriptografar os dados.

Projeto 2: Keylogger
- Foram criados dois codigos um chamado keylogger.pyw e keylogger_email.pyw (A extensão .pyw é para a execução do arquivo ficar "invisivel")

Ao executar o keylogger.pyw, toda entrada digitada é enviada para um arquivo criado chamado log.txt

Já o keylogger_email.pyw, toda entrada inserida é armazenada e a cada 60 segundos (determinado no codigo) é redirecionado para um endereço de email.
