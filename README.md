# Explorando Fundamentos de Cibersegurança com Desafios de Código em Python - Dio Santander Bootcamp Cibersegurança #2
Este repositório reúne as soluções dos desafios propostos no Santander Bootcamp Cibersegurança #2. Os desafios abordam fundamentos de cibersegurança, explorados por meio de exercícios de código em Python. São dois desafios onde cada um aborda uma parte específica no contexto da Cibersegurança.

# Primeiro Desafio - Verificação de Integridade de Arquivos com Hashes

## Descrição
Você foi encarregado de criar um sistema simples que verifica a integridade de arquivos, comparando o hash fornecido pelo usuário com o hash real do arquivo. Na função verificar_hashes que irá receber uma lista de hashes e compará-los com os valores esperados para cada arquivo. Seu objetivo é verificar se o hash calculado é igual ao hash esperado.

## Entrada
Uma lista de pares de hashes (hash calculado e hash esperado), separados por vírgulas, e cada par separado por ponto e vírgula.

## Saída
Para cada par de hashes fornecido, o código imprime o resultado "Correto" ou "Inválido".

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                            | Saída            |
|------------------------------------|------------------|
| abc123, abc123                     | Correto          |
| def456, def789                     | Inválido         |
| 123abc, 123abc; 456def, 456def     | Correto, Correto |

* Primeiro Desafio: Concluído em 10 de dezembro de 2024.

# Segundo Desafio - Simulação de Enumeração de Serviços em um Servidor

## Descrição
Desenvolva um sistema que simule a enumeração de serviços em um servidor, dado um conjunto de portas e serviços associados. Você deve receber uma lista de números de portas e, para cada porta, retornar o serviço associado. Se a porta não estiver no dicionário, retorna "Desconhecido".

## Entrada
Uma lista de números de portas separados por vírgula.

## Saída
Uma lista de serviços correspondentes a essas portas.

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada            | Saída                                |
|--------------------|--------------------------------------|
| 22, 80, 443        | ['SSH', 'HTTP', 'HTTPS']             |
| 21, 53, 3306       | ['FTP', 'DNS', 'MySQL']              |
| 23, 443, 8080      | ['Telnet', 'HTTPS', 'Desconhecido']  |

* Segundo Desafio: Concluído em 10 de dezembro de 2024.
