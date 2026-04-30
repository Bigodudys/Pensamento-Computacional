import hashlib
import datetime

# ==========================================
# 1. Módulo de Autenticação (Service-Auth)
# ==========================================
def autenticar_usuario(token):
    """Simula uma verificação de controle de acesso (RBAC)."""
    usuarios_validos = {
        "token_admin_123": "Gestor_Admin",
        "token_comum_456": "Servidor_Comum"
    }
    return usuarios_validos.get(token, None)

# ==========================================
# 2. Módulo de Auditoria (Service-Logger)
# ==========================================
def registrar_log(acao, usuario, detalhe):
    """Garante o rastro de auditoria para conformidade legal (LGPD)."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[LOG AUDITORIA] {timestamp} | Usuário: {usuario} | Ação: {acao} | Alvo: {detalhe}")

# ==========================================
# 3. Módulo de Armazenamento (Service-Storage)
# ==========================================
class RepositorioStorage:
    def __init__(self):
        # Abstração dos bancos de dados
        self.banco_metadados = {} # Simula o banco NoSQL
        self.storage_fisico = {}  # Simula o armazenamento S3/Local

    def gerar_hash_integridade(self, conteudo):
        """Algoritmo SHA-256 para garantir que o arquivo não sofra alterações."""
        return hashlib.sha256(conteudo.encode('utf-8')).hexdigest()

    def fazer_upload(self, usuario, nome_arquivo, conteudo, setor):
        doc_id = f"DOC_{len(self.banco_metadados) + 1:04d}"
        hash_arquivo = self.gerar_hash_integridade(conteudo)

        # Abstração do "Documento"
        metadados = {
            "id_unico": doc_id,
            "nome": nome_arquivo,
            "setor": setor,
            "hash_sha256": hash_arquivo,
            "data_upload": datetime.datetime.now().strftime("%Y-%m-%d"),
            "tier_armazenamento": "SSD_Rapido" # Conceito de Tiered Storage
        }

        # Salvando nos "bancos"
        self.banco_metadados[doc_id] = metadados
        self.storage_fisico[doc_id] = conteudo

        registrar_log("UPLOAD", usuario, doc_id)
        return doc_id

# ==========================================
# 4. Módulo de Busca (Service-Indexer)
# ==========================================
class MotorDeBusca:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def buscar_termo(self, usuario, palavra_chave):
        """Algoritmo de busca linear simples nos metadados e conteúdo."""
        resultados = []
        for doc_id, metadados in self.repositorio.banco_metadados.items():
            conteudo = self.repositorio.storage_fisico[doc_id]
            
            # Verifica se o termo está no título ou no conteúdo do arquivo
            if palavra_chave.lower() in conteudo.lower() or palavra_chave.lower() in metadados["nome"].lower():
                resultados.append(metadados)

        registrar_log("BUSCA", usuario, f"Termo pesquisado: '{palavra_chave}'")
        return resultados

# ==========================================
# Simulação de Execução (Main)
# ==========================================
if __name__ == "__main__":
    print("-" * 50)
    print("INICIANDO SISTEMA RDA - PROTÓTIPO DE LARGA ESCALA")
    print("-" * 50)
    
    # Instanciando os serviços
    storage = RepositorioStorage()
    motor_busca = MotorDeBusca(storage)

    # 1. Simulação de Login
    token_recebido = "token_admin_123"
    usuario_logado = autenticar_usuario(token_recebido)
    
    if usuario_logado:
        print(f"\n✅ Login efetuado com sucesso: {usuario_logado}\n")
        
        # 2. Simulação de Uploads
        print("--- Processando Uploads de Arquivos ---")
        storage.fazer_upload(
            usuario_logado, 
            "Ata_Reuniao_RH.txt", 
            "Ata da reuniao sobre contratacoes e registro de ponto.", 
            "Recursos Humanos"
        )
        storage.fazer_upload(
            usuario_logado, 
            "Edital_Licitacao_001.pdf", 
            "Edital oficial para a compra de novos computadores e servidores em nuvem.", 
            "Compras"
        )
        
        # 3. Simulação de Busca
        print("\n--- Realizando Busca de Documentos ---")
        resultados = motor_busca.buscar_termo(usuario_logado, "computadores")
        
        # 4. Exibição de Resultados
        print("\n--- Resultados Encontrados ---")
        if resultados:
            for res in resultados:
                print(f"📄 ID: {res['id_unico']} | Arquivo: {res['nome']}")
                print(f"   Setor: {res['setor']}")
                print(f"   Integridade (Hash): {res['hash_sha256']}")
                print(f"   Armazenamento: {res['tier_armazenamento']}\n")
        else:
            print("Nenhum documento encontrado.")
            
    else:
        print("\n❌ ERRO: Acesso Negado. Token inválido.")
