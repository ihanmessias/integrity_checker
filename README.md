# 🔑 Verificador de Integridade de Arquivos

Este é um script Python simples que permite verificar a integridade de arquivos usando funções de hash. Ele pode calcular o hash de um arquivo e compará-lo com um hash original salvo anteriormente para verificar se o arquivo foi alterado ou corrompido.

## Pré-requisitos

Certifique-se de ter Python instalado em seu sistema. Este script foi testado em Python 3.x.

## Uso

1. Clone este repositório em seu sistema ou faça o download do arquivo `integrity_checker.py`.

2. Execute o script `integrity_checker.py` da seguinte maneira:

    ```bash
    python integrity_checker.py
    ```
## Info

1. O script solicitará que você digite o nome do arquivo que deseja verificar. Certifique-se de colocar o arquivo na pasta "archive" do repositório.

2. O script calculará o hash do arquivo especificado e o comparará com o hash original salvo.

3. Você receberá uma das seguintes mensagens:

> "O arquivo está íntegro." se o arquivo não foi alterado ou corrompido.

> "O arquivo foi alterado ou corrompido." se o arquivo foi modificado desde que o hash original foi salvo.

> "Não há um hash disponível. Calculando o hash no arquivo." se não houver um hash original disponível e o script calculará o hash e o salvará.

## Como funciona
***O script usa as seguintes funções:***

`create_hash_archive(archive, algorithm)`: Calcula o hash de um arquivo usando o algoritmo especificado (por padrão, SHA-256).

`save_original_hash(archive, original_hash_archive)`: Salva o hash original do arquivo em um arquivo .pem na pasta "secret".

`check_archive_integrity(archive='archive', algorithm='sha256')`: Verifica a integridade do arquivo, calculando o hash atual e comparando-o com o hash original.

## Estrutura do Diretório

`archive`: Coloque os arquivos que deseja verificar aqui.

`secret`: Armazena os hashes originais dos arquivos.

## Contribuindo
Sinta-se à vontade para contribuir para este projeto abrindo problemas ou enviando solicitações pull. Se você tiver sugestões de melhorias ou encontrar problemas, ficaremos felizes em ouvir suas opiniões.

### 🤝 Suporte/Contato

[![LinkedIn Badge](https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=)](https://www.linkedin.com/in/ihanmessias/)
[![Whatsapp Badge](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/61996487935)
[![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/devlinuxtv/)

✉ ihanmessias.dev@gmail.com

<p align="center">Ihan Messias Nascimento dos Santos</p>