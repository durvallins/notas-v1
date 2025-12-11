# 🔄 Sistema de Cache e Atualização de Dados

## Como funciona o cache?

O sistema usa cache para melhorar a performance e reduzir o número de requisições ao Google Sheets.

### ⏱️ Configuração Atual

- **Tempo de expiração**: 5 minutos (300 segundos)
- **Tipo de cache**: `@st.cache_data`

Isso significa que os dados da planilha são buscados do Google Sheets apenas uma vez a cada 5 minutos. Durante esse período, todas as consultas usam os dados em cache.

## 🔄 Como atualizar os dados manualmente?

### Opção 1: Botão de Atualização (Recomendado)
1. Clique no botão **"🔄 Atualizar Dados"** no topo da página
2. O cache será limpo imediatamente
3. Os dados mais recentes serão carregados na próxima consulta

### Opção 2: Recarregar a Página
1. Pressione **F5** ou **Ctrl+R** no navegador
2. Aguarde 5 minutos desde o último carregamento
3. Os dados serão atualizados automaticamente

### Opção 3: Para Desenvolvedores
No terminal, você pode limpar o cache do Streamlit:
```powershell
# Parar o Streamlit (Ctrl+C)
# Limpar o cache
streamlit cache clear
# Reiniciar o Streamlit
streamlit run app.py --server.port 8505
```

## 📊 Quando os dados são atualizados?

1. **Primeira consulta**: Dados são buscados do Google Sheets
2. **Consultas seguintes (< 5 min)**: Dados em cache são usados
3. **Após 5 minutos**: Cache expira e novos dados são buscados
4. **Botão Atualizar**: Cache é limpo imediatamente

## ⚙️ Ajustar o tempo de cache

Para alterar o tempo de expiração do cache, edite o arquivo `app.py`:

```python
@st.cache_data(ttl=300)  # Altere 300 para o tempo desejado em segundos
def load_data(url):
    ...
```

### Exemplos:
- `ttl=60` - 1 minuto
- `ttl=300` - 5 minutos (padrão atual)
- `ttl=600` - 10 minutos
- `ttl=1800` - 30 minutos

## 💡 Dicas

- Use o botão "🔄 Atualizar Dados" quando souber que as notas foram alteradas
- O cache ajuda a reduzir o tempo de carregamento
- Em produção, considere aumentar o `ttl` para 10-15 minutos
- O timestamp exibido mostra quando os dados foram carregados pela última vez
