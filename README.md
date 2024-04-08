# Consulta de Músicos - Base de Dados Genealógica com PySWIP

Este é um programa Python que utiliza a biblioteca PySWIP para consultar informações sobre músicos em uma base de dados genealógica em Prolog. O programa permite consultar músicos que tocam um instrumento específico, músicos de uma banda que tocam um instrumento específico, consultar o instrumento e banda de um músico, além de adicionar novos músicos à base de dados.

## Funcionamento

O programa consiste em duas classes principais:

1. **Musico**: Representa um músico com os atributos nome, instrumento e banda.

2. **BaseDadosMusicos**: É responsável por gerenciar a base de dados genealógica e realizar as consultas. Essa classe utiliza a biblioteca PySWIP para integrar o Prolog ao Python.

O programa inicializa a base de dados com fatos e regras predefinidos, como os músicos, os instrumentos que tocam e as bandas a que pertencem. Em seguida, oferece um menu de opções ao usuário para consultar informações sobre os músicos ou adicionar novos músicos à base de dados.

## Como Usar

1. **Instalar as Dependências**: Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/). Além disso, é necessário instalar a biblioteca PySWIP. Você pode instalar usando o seguinte comando pip:

   ```
   pip install pyswip
   ```

2. **Clonar o Repositório**: Clone o repositório deste projeto em seu ambiente local.

3. **Executar o Programa**: No terminal ou prompt de comando, navegue até o diretório onde o arquivo Python `musico.py` está localizado e execute-o com o comando:

   ```
   python musico.py
   ```

4. **Utilizar o Programa**: Após executar o programa, você será apresentado com um menu de opções. Escolha uma das opções digitando o número correspondente e pressionando Enter. Você poderá consultar músicos, adicionar novos músicos ou sair do programa.

5. **Interagir com o Programa**: Siga as instruções apresentadas pelo programa para realizar consultas ou adicionar novos músicos. Você pode consultar músicos que tocam um instrumento específico, músicos de uma banda que tocam um instrumento específico, ou consultar o instrumento e banda de um músico.

6. **Encerrar o Programa**: Para sair do programa, selecione a opção "Sair" no menu principal.

Certifique-se de que o SWI-Prolog esteja instalado em seu sistema, pois o PySWIP depende dele para funcionar. Você pode baixar o SWI-Prolog em [swi-prolog.org](https://www.swi-prolog.org/download/stable).

Se você tiver problemas ou dúvidas durante a execução do programa, consulte a seção de [Issues](https://github.com/LucasDinizDev/Programa-Progenitor/issues) do repositório ou entre em contato com o desenvolvedor.
