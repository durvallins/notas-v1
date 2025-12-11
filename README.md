# 📚 Sistema de Consulta de Notas

Sistema web para consulta de notas acadêmicas desenvolvido com Streamlit.

## 🎯 Funcionalidades

- Seleção de turma e disciplina
- Consulta de notas por matrícula
- Interface moderna e responsiva
- Integração com Google Sheets
- Detecção de avaliações faltantes
- **Formatação padronizada** de notas (sempre com 1 casa decimal)
- **Cache inteligente** com atualização automática a cada 5 minutos
- **Botão de atualização manual** para buscar dados mais recentes

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
4. Visualize suas notas AV_01 e AV_02

### 🔄 Atualização de Dados

- Os dados são atualizados automaticamente a cada **5 minutos**
- Para forçar uma atualização imediata, clique no botão **"🔄 Atualizar Dados"** no topo da página
- Isso é útil quando as notas foram alteradas recentemente na planilha

## 🎓 Turmas Disponíveis

- 2º Período C - POO
- 4º Período A - ML (em breve)
- 4º Período B - ML (em breve)
- 4º Período C - ML (em breve)

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
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências Python
├── .env               # Variáveis de ambiente (NÃO VERSIONAR)
├── .env.example       # Exemplo de configuração
├── .gitignore         # Arquivos ignorados pelo Git
├── README.md          # Este arquivo
└── venv/              # Ambiente virtual Python
```
