# Repositório Digital Administrativo (RDA)

Este projeto foi desenvolvido como parte da disciplina **Pensamento Computacional para Sistemas de Larga Escala** no curso de Engenharia de Software.

## 📝 Descrição
O **RDA** é uma solução de backend e interface para a gestão, armazenamento e recuperação de documentos oficiais de um setor administrativo público. O foco do sistema é garantir a integridade, a auditabilidade e a escalabilidade no manejo de grandes volumes de arquivos (PDFs, editais, atas e processos).

## 🎯 Objetivos
- **Escalabilidade:** Suportar o crescimento exponencial de dados de um órgão público.
- **Segurança:** Implementar controle de acesso rigoroso (RBAC) e conformidade com a LGPD.
- **Eficiência:** Reduzir o tempo de busca de documentos físicos através de indexação inteligente.
- **PBL:** Aplicar os quatro pilares do pensamento computacional em um cenário real.

## 🏗️ Sistema Proposto
**Nome:** RDA - Repositório Digital Administrativo  
**Público-alvo:** Servidores públicos e gestores administrativos.

### Módulos Principais:
1. **Upload e Versionamento:** Garantia de que documentos não sejam sobrescritos sem rastro.
2. **Motor de Busca:** Pesquisa por metadados e conteúdo (OCR).
3. **Módulo de Auditoria:** Log de quem acessou, alterou ou baixou cada arquivo.
4. **Gestão de Retenção:** Automatização do descarte de documentos conforme a tabela de temporalidade.

## 🧠 Pensamento Computacional Aplicado
- **Decomposição:** O problema de "gerir arquivos" foi quebrado em: Autenticação, Armazenamento de Objetos, Indexação de Busca e Barramento de Eventos para Auditoria.
- **Reconhecimento de Padrões:** Uso de metadados padronizados (Dublin Core) e fluxos de aprovação similares a sistemas de protocolo eletrônico.
- **Abstração:** Representação de diferentes tipos de arquivos (imagem, texto, planilha) sob uma interface única de "Documento".
- **Algoritmos:** Algoritmos de hash (SHA-256) para integridade de arquivos e algoritmos de busca por relevância.

## 📂 Estrutura do Repositório
```text
RDA_Public_Sector/
│
├── README.md              # Documentação principal
├── Design.md              # Detalhamento técnico (Decomposição e Abstração)
├── Diagrama.png           # Arquitetura do sistema em larga escala
├── Desafios.md            # Barreiras técnicas e soluções (LGPD, Storage)
└── src/                   # Mockups e protótipo inicial
