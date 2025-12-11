# 🚀 Guia de Publicação no GitHub

## 📦 Preparação para Publicação

### 1️⃣ Verificar Arquivos

Certifique-se de que você tem:
- ✅ `.env.example` (modelo sem URLs reais)
- ✅ `.env` (com URLs reais - NÃO será enviado)
- ✅ `.gitignore` (protegendo arquivos sensíveis)
- ✅ `README.md` (documentação completa)
- ✅ `requirements.txt` (dependências)
- ✅ Todos os arquivos do projeto

### 2️⃣ Inicializar Git (se ainda não foi feito)

```powershell
# Entrar na pasta do projeto
cd E:\Documentos\PROJETOS\conferencia_nota

# Inicializar repositório Git
git init

# Adicionar todos os arquivos (exceto os do .gitignore)
git add .

# Verificar quais arquivos serão commitados
git status

# Confirmar que .env NÃO está na lista!
```

### 3️⃣ Criar Commit Inicial

```powershell
# Criar primeiro commit
git commit -m "🎉 Inicial: Sistema de Consulta de Notas

- Interface moderna com Streamlit
- Integração com Google Sheets
- Sistema de cache inteligente (TTL 5min)
- Detecção de avaliações faltantes
- Formatação padronizada de notas
- Variáveis de ambiente (.env)
- Documentação completa"
```

### 4️⃣ Criar Repositório no GitHub

1. Acesse https://github.com
2. Clique em "New repository"
3. Nome sugerido: `sistema-consulta-notas`
4. Descrição: "Sistema web para consulta de notas acadêmicas com Streamlit e Google Sheets"
5. **NÃO** marque "Initialize with README" (já temos um)
6. Clique em "Create repository"

### 5️⃣ Conectar e Enviar

```powershell
# Adicionar repositório remoto (substitua SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/sistema-consulta-notas.git

# Renomear branch para main (padrão atual do GitHub)
git branch -M main

# Enviar código para o GitHub
git push -u origin main
```

---

## 🔒 Segurança - Checklist Final

Antes de fazer o push, verifique:

### ✅ Verificações Obrigatórias:

```powershell
# 1. Verificar que .env está no .gitignore
Get-Content .gitignore | Select-String ".env"
# Deve retornar: .env

# 2. Verificar que .env NÃO está sendo rastreado
git status
# .env NÃO deve aparecer na lista!

# 3. Listar arquivos que serão enviados
git ls-files
# .env NÃO deve aparecer nesta lista!
```

### ❌ O que NÃO pode ir para o GitHub:
- ❌ `.env` (URLs reais)
- ❌ `venv/` (ambiente virtual)
- ❌ `__pycache__/` (cache Python)
- ❌ `.streamlit/` (configurações locais, exceto .example)
- ❌ `arquivos/` (arquivos internos e temporários)

### ✅ O que DEVE ir para o GitHub:
- ✅ `.env.example` (modelo)
- ✅ `.gitignore`
- ✅ `app.py`
- ✅ `requirements.txt`
- ✅ `README.md`
- ✅ Arquivos de documentação (.md)
- ✅ `.streamlit/secrets.toml.example`

---

## 🎯 Após Publicar

### Para outras pessoas usarem o projeto:

1. Clone o repositório:
```powershell
git clone https://github.com/SEU_USUARIO/sistema-consulta-notas.git
cd sistema-consulta-notas
```

2. Crie o ambiente virtual:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

3. Instale dependências:
```powershell
pip install -r requirements.txt
```

4. Configure o `.env`:
```powershell
Copy-Item .env.example .env
# Editar .env com as URLs reais
```

5. Execute:
```powershell
streamlit run app.py --server.port 8502
```

---

## 📱 Deploy em Produção (Streamlit Cloud)

### Opção 1: Streamlit Cloud (Gratuito)

1. Acesse: https://streamlit.io/cloud
2. Conecte sua conta GitHub
3. Selecione o repositório
4. Configure as variáveis de ambiente (Secrets):
   - Adicione as URLs no painel "Secrets"
   ```toml
   URL_2P_C_POO = "sua_url_aqui"
   URL_4P_A_ML = "sua_url_aqui"
   URL_4P_B_ML = "sua_url_aqui"
   URL_4P_C_ML = "sua_url_aqui"
   ```
5. Deploy automático!

### Modificação necessária para Streamlit Cloud:

No `app.py`, adicione suporte para Streamlit Secrets:

```python
import os
from dotenv import load_dotenv
import streamlit as st

# Carregar variáveis de ambiente
load_dotenv()

# URLs das planilhas (compatível com .env e Streamlit Cloud)
def get_url(key, default=""):
    # Tenta pegar do Streamlit Secrets primeiro (produção)
    if hasattr(st, 'secrets') and key in st.secrets:
        return st.secrets[key]
    # Senão, pega do .env (desenvolvimento)
    return os.getenv(key, default)

URLS = {
    "2º Período C - POO": get_url("URL_2P_C_POO"),
    "4º Período A - ML": get_url("URL_4P_A_ML"),
    "4º Período B - ML": get_url("URL_4P_B_ML"),
    "4º Período C - ML": get_url("URL_4P_C_ML")
}
```

---

## 🆘 Problemas Comuns

### Erro: ".env foi commitado acidentalmente"

Se você acidentalmente commitou o `.env`:

```powershell
# Remover .env do histórico
git rm --cached .env

# Adicionar ao .gitignore (se ainda não está)
echo ".env" >> .gitignore

# Commit da correção
git add .gitignore
git commit -m "🔒 Removido .env do repositório"

# Force push (CUIDADO!)
git push --force
```

⚠️ **IMPORTANTE**: Se o `.env` já foi enviado publicamente, considere as URLs comprometidas e gere novas!

---

## 📝 Comandos Git Úteis

```powershell
# Ver status
git status

# Ver histórico
git log --oneline

# Ver diferenças
git diff

# Adicionar arquivos específicos
git add arquivo.py

# Commit
git commit -m "mensagem"

# Push
git push

# Pull (atualizar)
git pull
```

---

## ✅ Checklist Final

Antes de fazer `git push`:

- [ ] `.env` está no `.gitignore`
- [ ] `.env` NÃO aparece em `git status`
- [ ] `.env.example` existe e está sem dados sensíveis
- [ ] README.md está completo e atualizado
- [ ] requirements.txt está atualizado
- [ ] Código está funcionando localmente
- [ ] Documentação está clara

**Tudo OK? Pode fazer o push!** 🚀
