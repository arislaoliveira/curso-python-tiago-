"""
Programa inicial para referência dos primeiros passos em python!
Tiago Gutierres da Silva
Curitiba
19/04/2023
"""

"""
Metodologia adotada para geração da docstring inicial:
Nome do Programa:
Nome do Autor:
Data da Última modificação:

Texto introdutório com a explicação das principais funções do código!
"""

# Primeiro comando
print("Show!")
# Tipo de dados (classe) do literal do tipo string
print(type('Show!'))
# Exemplo de uma string vazia:
print('')
# Exemplo de uma docstring para texto multilinhas:
print("""
linha 1
linha 2
linha 3
""")
#Exemplo de caractere de escape!
print("Texto entre aspas: \'Olá\' ")
#Exemplo de manipulação de cursor
#Observe que o \b "backspace" apenas retrocede a posição do cursor!
print("Um te\nxto qua\tlqu\b\ber!")
#Exemplo de concatenação de strings:
print("uma string, " + "outra string, " + "ainda outra string!")
#Exemplo de repetição de strings:
print("Curso de Python!\n" * 5 )
#Exemplo de literal do tipo int (qualquer caractere numérico sem ponto é considerado int)
print(10)
print(type(10))
print(5 * 2)
#Exemplo de literal do tipo float (qualquer caractere numérico com ponto é considerado float)
print(10.)
print(type(10.))
print(15.3e2)
print(type(15.3e2))
print(5. * 2.)
#Exemplo de criação de variáveis
varDoTipoString = 'Um texto qualquer!'
print(type(varDoTipoString)) #stdout
varDoTipoInt = 100
print(type(varDoTipoInt))
varDoTipoFloat = 100.0
print(type(varDoTipoFloat))
# Conversão de tipos
b = 3 * 4  # Neste caso, o valor final é int
c = 3 * 4. # Neste caso, o valor final é float
#Exemplo de entrada de dados:
# COMO REGRA, a função input() SEMPRE retorna uma string!
# Caso deseje usar o valor como outro tipo de dado, a conversão deve ser manual
# através das funções int() e float().
# Caso queira converter novamente em string, utilizar a função str()
d =  int( input("Digite um valor INTEIRO: ") ) #stdin
print("Valor digitado: " + str(d))
print("Tipo do valor digitado: " + str(type(d)))

f =  float( input("Digite um valor PONTO FLUTUANTE: ") ) #stdin
print("Valor digitado: " + str(f))
print("Tipo do valor digitado: " + str(type(f)))