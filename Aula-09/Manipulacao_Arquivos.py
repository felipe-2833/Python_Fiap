from pathlib import Path
this = Path(__file__).parent

path = this/"arquivo.txt"
arquivo = open(path)

arquivo.read()
arquivo.close() #fechar arquivo deve ser feito smepre oa final de uma operação de abertura

#gerenciador de contexto, faz coom que o arquivo seja fechado automaticamente ao termino do bloco
with open(path) as arquivo:
    texto = arquivo.read()
    #não necessita de .close()
    
print(texto)