# 📚 Sistema de Consulta de Notas

Sistema web para consulta de notas acadêmicas desenvolvido com Streamlit.

## 🎯 Funcionalidades

- ✅ Seleção de turma e disciplina
- ✅ Consulta de notas por matrícula
- ✅ Interface moderna e responsiva
- ✅ Integração com Google Sheets
- ✅ Detecção de avaliações faltantes
- ✅ **Formatação padronizada** de notas (sempre com 1 casa decimal)
- ✅ **Cache inteligente** com atualização automática a cada 5 minutos
- ✅ **Botão de atualização manual** para buscar dados mais recentes
- ✅ **Exibição da MÉDIA** das avaliações (AV 01 + AV 02) / 2
- ✅ **Indicador visual de aprovação:**
  - 🎉 **Verde** para média ≥ 7.0 (APROVADO)
  - ⚠️ **Vermelho** para média < 7.0 (PROVA FINAL)
- ✅ **Mensagens contextuais** sobre situação acadêmica
- ✅ **Filtro por turma** para planilhas consolidadas (4º Períodos)
- ✅ **Detecção automática** de colunas da planilha

## 🆕 Novidades (Dezembro/2025)

### Coluna MÉDIA
- Sistema agora exibe a **média das duas avaliações**
- Cálculo automático: `(AV 01 + AV 02) / 2`
- Se a planilha já tiver a coluna MÉDIA, usa o valor da planilha

### Código de Cores
- **🟢 Verde** (média ≥ 7.0): Aluno aprovado direto
- **🔴 Vermelho** (média < 7.0): Aluno precisa fazer Prova Final (AF)
- Mensagens automáticas informando a situação

### Planilhas Consolidadas
- 4º Períodos agora usam uma **única planilha** com filtro por turma
- Reduz manutenção e facilita atualizações
- Coluna `TURMA` identifica cada turma (4P_A, 4P_B, 4P_C)

## ⚙️ Configuração Inicial

1. **Clone o repositório** (ou faça o download)

2. **Crie o ambiente virtual:**
```powershell
python -m venv venv
```

3. **Ative o ambiente virtual:**
```powershell
.\venv\Scripts\activate
```

4. **Instale as dependências:**
```powershell
pip install -r requirements.txt
```

5. **Configure as variáveis de ambiente:**
   - Copie o arquivo `.env.example` para `.env`
   ```powershell
   Copy-Item .env.example .env
   ```
   - Abra o arquivo `.env` e adicione as URLs das planilhas do Google Sheets

## 🚀 Como Executar

1. Certifique-se de que o ambiente virtual está ativo:
```powershell
.\venv\Scripts\activate
```

2. Execute o aplicativo (porta 8502):
```powershell
streamlit run app.py --server.port 8502
```

3. Acesse no navegador:
```
http://localhost:8502
```

## 📝 Como Usar

1. Selecione sua turma no menu dropdown
2. Digite sua matrícula (ex: 1806568)
3. Clique em "🔍 Consultar"
4. Visualize suas notas:
   - 📝 **AV 01** - Nota da primeira avaliação
   - 📝 **AV 02** - Nota da segunda avaliação
   - 📊 **MÉDIA** - Média das duas avaliações (com indicador de aprovação)

### 📊 Entendendo sua MÉDIA

- **🎉 Caixa Verde (média ≥ 7.0):** Você está **APROVADO**! Parabéns!
- **⚠️ Caixa Vermelha (média < 7.0):** Você precisará fazer a **PROVA FINAL (AF)**

### 🔄 Atualização de Dados

- Os dados são atualizados automaticamente a cada **5 minutos**
- Para forçar uma atualização imediata, clique no botão **"🔄 Atualizar Dados"** no topo da página
- Isso é útil quando as notas foram alteradas recentemente na planilha

## 🎓 Turmas Disponíveis

- 2º Período C - POO (planilha individual)
- 4º Período A - ML (planilha consolidada com filtro)
- 4º Período B - ML (planilha consolidada com filtro)
- 4º Período C - ML (planilha consolidada com filtro)

### 📋 Estrutura das Planilhas

#### 2º Período C - POO
```
Aluno | MATRÍCULA | AV. 01 | AV. 02 | MÉDIA
```

#### 4º Períodos A, B e C - ML (Consolidada)
```
TURMA | NOME | MATRÍCULA | AV 01 | AV 02 | MÉDIA
```
- Coluna `TURMA` contém: `4P_A`, `4P_B` ou `4P_C`
- Sistema filtra automaticamente pela turma selecionada

## 🛠️ Tecnologias

- Python 3.11+
- Streamlit
- Pandas
- Python-dotenv
- Google Sheets API

## 📦 Dependências

Ver arquivo `requirements.txt`

## 🔒 Segurança

- As URLs das planilhas são armazenadas no arquivo `.env` (não versionado)
- Use o arquivo `.env.example` como referência para configuração

## 📋 Estrutura do Projeto

```
conferencia_nota/
├── app.py                          # Aplicação principal
├── requirements.txt                # Dependências Python
├── .env                           # Variáveis de ambiente (NÃO VERSIONAR)
├── .env.example                   # Exemplo de configuração
├── .gitignore                     # Arquivos ignorados pelo Git
├── README.md                      # Este arquivo
├── PUBLICACAO.md                  # Guia de publicação no GitHub
├── CACHE_INFO.md                  # Informações sobre o sistema de cache
├── FORMATACAO_NOTAS.md            # Padrões de formatação de notas
├── CONFIGURAR_STREAMLIT_CLOUD.md  # Guia para deploy na nuvem
├── ESTRUTURA.md                   # Documentação da estrutura do projeto
├── SISTEMA_FILTRO_TURMAS.md       # Como funciona o filtro de turmas
├── IMPLEMENTACAO_MEDIA.md         # Documentação da coluna MÉDIA
├── .streamlit/
│   └── secrets.toml.example       # Template de secrets para Streamlit Cloud
├── arquivos/                      # Arquivos internos (não versionados)
│   ├── amb_virtual.txt
│   ├── orientacoes.txt
│   └── poo_2p.txt
└── venv/                          # Ambiente virtual Python
```

## 🔗 Links Úteis

- **Repositório GitHub:** https://github.com/durvallins/notas-v1
- **App em Produção:** https://notas-v1git-wgvdnwyxbvur4rqejkma5g.streamlit.app/

## 📚 Documentação Adicional

- [PUBLICACAO.md](PUBLICACAO.md) - Como publicar no GitHub
- [CACHE_INFO.md](CACHE_INFO.md) - Sistema de cache e atualização
- [FORMATACAO_NOTAS.md](FORMATACAO_NOTAS.md) - Padrões de formatação
- [CONFIGURAR_STREAMLIT_CLOUD.md](CONFIGURAR_STREAMLIT_CLOUD.md) - Deploy na nuvem
- [SISTEMA_FILTRO_TURMAS.md](SISTEMA_FILTRO_TURMAS.md) - Filtros de turmas consolidadas
- [IMPLEMENTACAO_MEDIA.md](IMPLEMENTACAO_MEDIA.md) - Funcionalidade da MÉDIA

## 🤝 Contribuindo

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto é de uso educacional.

---

**Desenvolvido com ❤️ para facilitar o acesso às notas acadêmicas**
