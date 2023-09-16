# ~@Import_Libs:
import os
import hashlib

# ~@Functions:
def create_hash_archive(archive, algorithm): # -->> Cria Hash
    '''NOTE
    [Parâmetros]:
    "file"=O nome do arquivo do qual deseja calcular o hash (Representação).
    "algorithm"='sha256' Algoritmo de hash a ser utilizado (Exemplos: SHA-1, MD5, etc). 
    
    [Tratamento de ERROR]:
    "if not os.path.isfile(file)"= Verifica se o não arquivo existe, retornando FileNotFoundError se verdadeiro.
    
    [Hash]:
    "hash_obj"= Cria um objeto de hash com o algoritmo informado.
    
    [Aplicação do Hash]:
    "read_file"=Leitura em bytes (64kb), útil para lidar com arquivos grandes.
    "if not read_file"= Quando atinge o final do arquivo e é retornado uma string vazia (Nada para ler).
    "hash_obj.update(read_file)"= Atualiza o hash a mediada que os hash são lidos.
    "return hash_obj.hexdigest()"= Retorna o hash em formato hexadecimal (Padrão para verificação de Integridade).
    '''
    #TODO: Estabelecer msg de file não localizado. 
    if not os.path.isfile(f'archive/{archive}'):
        raise FileNotFoundError(f'O arquivo {archive} especificado não foi localizado ou não existe.')
    #TODO: Criar Hash com base no algoritmo.
    hash_obj = hashlib.new(algorithm) # Hash SHA256
    #TODO: Realizar leitura do arquivo em bytes e aplicar hash
    with open(os.path.join(os.getcwd(), f'archive/{archive}'), 'rb') as file:
        while True:
            read_file = file.read(65536) #NOTE: Bytes = 64KB.
            if not read_file: #NOTE: Quando realizado toda leitura finaliza loop.
                break
            hash_obj.update(read_file) #NOTE: Atualiza o hash conforme vai realizando leitura.
        #TODO: Retornar cálculo de hash em Hexadecimal. 
        return hash_obj.hexdigest()
    
def save_original_hash(archive, original_hash_archive): # -->> Salva o Hash
    '''NOTE
    [Salvando o Hash]:
    "if not os.path.exists('secret')"= Verifica se diretório não existe (Se True, faz a criação).
    "with open(os.path.join(os.getcwd(), f'secret/{archive}'.hash, 'w')) as file:"= Procura diretório local e faz a concatenação na pasta para salvamento.
    "file.write(original_hash_archive)"= Escreve hash em arquivo ".hash".
    '''
    #TODO: Criar pasta para armazenar o hash.
    if not os.path.exists('secret'):
        os.mkdir('secret')
    #TODO: Salvar hash do arquivo gerado.
    with open(os.path.join(os.getcwd(), f'secret/{archive}.pem'), 'w') as file:
        file.write(original_hash_archive)
        
def check_archive_integrity(archive='archive',algorithm='sha256'):
    '''NOTE
    [Pasta]:
    os.mkdir(archive)=Cria a pasta chamada "archive" no diretorio de execução.
    [Variaveis]:
    original_hash_archive = os.path.join(os.getcwd(), f"secret/{archive}.hash")=Informa diretório de hash. 
    hash_archive = create_hash_archive(archive, algorithm)=Cria o hash com base no conteudo do arquivo.
    existing_hash = None # sem hash no inicio
    '''
    original_hash_archive = os.path.join(os.getcwd(), f"secret/{archive}.pem") # Diretorio do hash
    hash_archive = create_hash_archive(archive, algorithm) # Cria o hash
    
    existing_hash = None # sem hash no inicio
    
    # Onde ta o hash se existir, abre e faz leitura
    if os.path.exists(original_hash_archive):
        with open(original_hash_archive, 'r') as f:
            existing_hash = f.read().strip() # Deixa sem ser None
        # Integridade    
        if hash_archive == existing_hash:
            print("O arquivo está íntegro.")    
        else:
            print("O arquivo foi alterado ou corrompido.")    
    
    # Se não existir hash, cria
    if existing_hash is None:
        print("Não há um hash disponível. Calculando o hash no arquivo.")
        save_original_hash(archive, hash_archive)    
    
# End Script:
if __name__ == "__main__":
    # Cria a pasta "archive"
    if not os.path.exists('archive'):
        os.mkdir('archive')
        print('Crie um arquivo na pasta "archive" e tente novamente.')
        exit()
    archive = input("Digite o nome do arquivo a verificar: ")

    try:
        check_archive_integrity(archive)
    except FileNotFoundError as Error:
        print(Error)
    except Exception as Error:
        print(f"Ocorreu um erro: {str(Error)}")