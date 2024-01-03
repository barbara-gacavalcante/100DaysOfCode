### Aula 01
- python é uma linguagem interpretada, orientada a objetos, de alto nível e com semântica dinâmica. suporta módulos e pacotes, o que possibilita uma programação modularizada e o reuso de código.
- foi criada em 1990, na Holanda, para suceder a linguagem ABC, e a grande diferença entre elas é que python possui funcionalidades como Listas, Dicionários, declarações básicas e identação obrigatória.
- python é tanto interpretada quanto compilada. o interpretador faz a tradução de cada comando em tempo de execução. já o compilador, traduz o código todo de uma só vez. graças ao relatório de erros criado pelo compilador, o interpretador consegue interromper a execução no primeiro erro encontrado.
- PEP (Python Enhancement Proposals): melhorias sugeridas por qualquer usuário, que a comunidade testa, avalia e possivelmente implementa nas novas versões.
- é uma linguagem de propósito geral. muito usada em tarefas laterais (como acessar dados em um BD, criar planilhas etc.). além disso, por ser muito legível e ter linguagem expressiva, bem como muitos módulos, é fortemente adotada pela comunidade científica.

#### Modo interativo:
no prompt de comando, basta digitar 'py' para acessar o modo interativo.
#### Modo script: 
o código python é isolado em um arquivo '.py', e um editor de texto é usado para escrevê-lo.

### Aula 02
#### Tipos embutidos, variáveis, operadores
#### Manipulação de Strings:
**concatenação:**
texto1 = 'olá'
texto2 = 'Python'
print(texto1 + texto2) = oláPython

**multiplicação:**
texto1 = 'python'
print(texto1 * 3) = pythonpythonpython

**maiúsculas:**
texto2.upper()

**capitalização:**
texto2.capitalize()

#### Entrada do usuário
input() 
###### *obs: armazena o valor inserido em string, necessário converter para manipular
**Limitar casas decimais:** {:.2f} (quando usamos o .format())

#### if, while, for...
**for:**  for variavel in range(inicio, fim, step)
