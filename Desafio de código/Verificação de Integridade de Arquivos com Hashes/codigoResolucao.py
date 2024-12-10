# Primeiro desafio proposto do bootcamp Santander / Verificação de Integridade de Arquivos com Hashes
# Lucas Galvão dos Santos
# 10/Dezembro/2024

def verificar_hashes(lista_hashes):
  
    for hash_comparacao in lista_hashes:
        
        hash_calculado, hash_esperado = hash_comparacao.split(",")
        
        # TODO: Verifique se o hash calculado é igual ao hash esperado:
        
        # Removendo espaços em branco antes da comparação
        hash_calculado = hash_calculado.strip()
        hash_esperado = hash_esperado.strip()
        
        # Verifique se o hash calculado é igual ao hash esperado
        if hash_calculado == hash_esperado:
            print("Correto")
        else:
            print("Inválido")
        

print("Digite os pares de hashes no formato 'hash_calculado, hash_esperado' separados por ponto e vírgula:")
hashes_usuario = input("> ")

lista_hashes = hashes_usuario.split(";")

verificar_hashes(lista_hashes)