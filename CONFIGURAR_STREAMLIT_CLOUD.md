# 🔐 Configuração de Secrets no Streamlit Cloud

## Passo a Passo para Adicionar as URLs:

### 1️⃣ Acessar o Dashboard do Streamlit Cloud
- Acesse: https://share.streamlit.io/
- Faça login com sua conta GitHub

### 2️⃣ Encontrar seu App
- Procure pelo app: **notas-v1**
- Clique nos **três pontinhos (⋮)** ao lado do app
- Selecione **"Settings"** (Configurações)

### 3️⃣ Adicionar Secrets
- No menu lateral, clique em **"Secrets"**
- Cole o seguinte conteúdo na caixa de texto:

```toml
# URLs das planilhas do Google Sheets
URL_2P_C_POO = "https://docs.google.com/spreadsheets/d/e/2PACX-1vReM-efNOlMd4VoJL3GgRkaYI7oSHlawzwABQQe61idQmAQRUtDnJLeREaK4HxNaQ/pub?gid=898723192&single=true&output=csv"
URL_4P_A_ML = ""
URL_4P_B_ML = ""
URL_4P_C_ML = ""
```

### 4️⃣ Salvar
- Clique em **"Save"** (Salvar)
- O app será reiniciado automaticamente

### 5️⃣ Verificar
- Aguarde o app reiniciar (pode levar 1-2 minutos)
- Acesse: https://notas-v1git-wgvdnwyxbvur4rqejkma5g.streamlit.app/
- Teste selecionando "2º Período C - POO"

---

## 📋 Formato dos Secrets

**IMPORTANTE:** No Streamlit Cloud, use o formato **TOML** (não .env):

```toml
# Correto ✅
URL_2P_C_POO = "sua_url_aqui"

# Errado ❌ (formato .env)
URL_2P_C_POO=sua_url_aqui
```

---

## 🎥 Tutorial Visual

1. **Dashboard** → Seus Apps
2. **⋮** (três pontinhos) → Settings
3. **Secrets** (menu lateral)
4. Cole as URLs no formato TOML
5. **Save**
6. Aguarde reiniciar

---

## ⚠️ Troubleshooting

### Se ainda não funcionar:

1. **Verifique o formato:**
   - Use aspas duplas `" "`
   - Formato TOML, não .env

2. **Reinicie manualmente:**
   - Settings → **"Reboot app"**

3. **Verifique os logs:**
   - Settings → **"Logs"**
   - Procure por erros relacionados a secrets

---

## 🔗 Links Úteis

- Dashboard: https://share.streamlit.io/
- Documentação Secrets: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management
- Seu App: https://notas-v1git-wgvdnwyxbvur4rqejkma5g.streamlit.app/

---

## 📝 Checklist

- [ ] Acessei o Streamlit Cloud Dashboard
- [ ] Encontrei meu app "notas-v1"
- [ ] Abri Settings → Secrets
- [ ] Colei as URLs no formato TOML
- [ ] Salvei as configurações
- [ ] Aguardei o app reiniciar
- [ ] Testei o app no navegador

---

**Após configurar, seu app funcionará perfeitamente!** 🚀
