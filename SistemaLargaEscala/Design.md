design_content = """# Design do Sistema: RDA

Este documento detalha como os princípios do Pensamento Computacional moldaram a arquitetura do RDA.

1. Decomposição do Sistema
Para lidar com larga escala, o sistema foi decomposto em microserviços:

Service-Auth: Gere permissões e sessões.

Service-Storage: Interface com serviços de armazenamento em nuvem ou servidores locais.

Service-Indexer: Responsável por ler o conteúdo dos arquivos e tornar a busca instantânea.

Service-Logger: Registra ações para conformidade legal.

2. Abstração e Modelagem
O sistema abstrai a complexidade do hardware de armazenamento. Para o usuário, não importa se o arquivo está em um servidor físico ou no S3; a interface interage com um objeto "Documento" que possui:

ID_Unico

Timestamp

Hash_Integridade

Nivel_Acesso

3. Reconhecimento de Padrões
Identificamos que 80% das interações seguem o padrão "Consultar -> Visualizar -> Baixar". Com base nisso, implementamos um sistema de Cache para documentos frequentemente acessados, reduzindo a carga no storage principal.

4. Algoritmos Chave
Cálculo de Hash: Executado no upload e periodicamente para garantir que o arquivo não foi corrompido ou alterado por terceiros.

Busca Booleana: Algoritmo para filtrar documentos por setor, data e palavras-chave simultaneamente.
"""
