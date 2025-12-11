import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Função para obter URLs (compatível com .env local e Streamlit Cloud)
def get_url(key, default=""):
    """
    Obtém URL de configuração.
    Prioriza Streamlit Secrets (produção) sobre .env (desenvolvimento).
    """
    # Tenta pegar do Streamlit Secrets primeiro (produção/cloud)
    try:
        if key in st.secrets:
            return st.secrets[key]
    except:
        pass
    # Senão, pega do .env (desenvolvimento local)
    return os.getenv(key, default)

# URLs das planilhas por turma
URLS = {
    "2º Período C - POO": get_url("URL_2P_C_POO"),
    "4º Período A - ML": get_url("URL_4P_A_ML"),
    "4º Período B - ML": get_url("URL_4P_B_ML"),
    "4º Período C - ML": get_url("URL_4P_C_ML")
}

# Carregar os dados com cache de 5 minutos
@st.cache_data(ttl=300)  # Cache expira em 5 minutos (300 segundos)
def load_data(url):
    try:
        data = pd.read_csv(url)
        # Normalizar nomes das colunas
        data.columns = data.columns.str.strip()
        return data
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

# Configuração da página
st.set_page_config(
    page_title="Sistema de Consulta de Notas", 
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS customizado
st.markdown("""
    <style>
    /* Importar fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main-title {
        text-align: center;
        color: #1f77b4;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    
    /* Estilização do botão */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #1f77b4 0%, #0d5a9e 100%);
        color: white;
        font-size: 16px;
        font-weight: 600;
        height: 48px !important;
        min-height: 48px !important;
        max-height: 48px !important;
        border-radius: 8px;
        border: none;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(31, 119, 180, 0.3);
        padding: 0 !important;
        line-height: 48px !important;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0d5a9e 0%, #094173 100%);
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(31, 119, 180, 0.5);
    }
    .stButton>button:active {
        transform: translateY(0px);
    }
    
    /* Remover padding extra do container do botão */
    .stButton {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Estilização do input */
    .stTextInput>div>div>input {
        height: 48px !important;
        min-height: 48px !important;
        max-height: 48px !important;
        font-size: 16px;
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        padding: 0 20px !important;
        transition: all 0.3s ease;
        background-color: #fafafa;
        line-height: 48px !important;
    }
    .stTextInput>div>div>input:hover {
        border-color: #c0c0c0;
        background-color: #ffffff;
    }
    .stTextInput>div>div>input:focus {
        border-color: #1f77b4;
        box-shadow: 0 0 0 4px rgba(31, 119, 180, 0.1);
        background-color: #ffffff;
    }
    
    /* Remover padding extra do container do input */
    .stTextInput {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Alinhar os containers das colunas */
    div[data-testid="column"] {
        display: flex;
        align-items: flex-start;
    }
    
    div[data-testid="column"] > div {
        width: 100%;
    }
    
    /* Estilização do selectbox */
    .stSelectbox>div>div>div {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    /* Card de resultado */
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 40px;
        border-radius: 20px;
        color: white;
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        margin: 30px 0;
        animation: slideUp 0.5s ease;
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .aluno-nome {
        font-size: 2.2em;
        font-weight: 700;
        margin: 20px 0;
        text-align: center;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    .nota-box {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 10px 0;
        transition: all 0.3s ease;
        border: 2px solid rgba(255,255,255,0.1);
    }
    .nota-box:hover {
        background: rgba(255,255,255,0.2);
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .nota-label {
        font-size: 1.1em;
        opacity: 0.95;
        font-weight: 500;
        margin-bottom: 10px;
    }
    .nota-valor {
        font-size: 3em;
        font-weight: 700;
        margin-top: 5px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    /* Mensagens de alerta personalizadas */
    .stAlert {
        border-radius: 8px;
        font-weight: 500;
    }
    
    /* Estilo para mensagens de aviso */
    div[data-testid="stWarning"] {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 15px;
        border-radius: 8px;
    }
    
    div[data-testid="stInfo"] {
        background-color: #d1ecf1;
        border-left: 5px solid #0dcaf0;
        padding: 15px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título da aplicação
st.markdown('<p class="main-title">📚 Sistema de Consulta de Notas</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Consulte suas notas de forma rápida e segura</p>', unsafe_allow_html=True)

# Botão para atualizar dados
col1, col2, col3 = st.columns([1, 2, 1])
with col3:
    if st.button("🔄 Atualizar Dados", help="Clique para buscar as notas mais recentes"):
        st.cache_data.clear()
        st.success("✅ Cache limpo! Os dados serão atualizados.")
        st.rerun()

st.markdown("---")

# Seleção da turma
st.markdown("### 🎓 Selecione sua turma:")
turma_selecionada = st.selectbox(
    "Turma e Disciplina",
    ["Selecione uma opção...", "2º Período C - POO", "4º Período A - ML", "4º Período B - ML", "4º Período C - ML"],
    label_visibility="collapsed"
)

# Verificar se uma turma foi selecionada
if turma_selecionada != "Selecione uma opção...":
    # Carregar dados da turma selecionada
    url = URLS.get(turma_selecionada)
    
    if url:
        data = load_data(url)
        
        if data is not None:
            # Mostrar informação de última atualização
            from datetime import datetime
            hora_atual = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
            
            col_success, col_info = st.columns([3, 1])
            with col_success:
                st.success(f"✅ Dados da turma **{turma_selecionada}** carregados!")
            with col_info:
                st.info(f"🕐 {hora_atual}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Entrada da matrícula do aluno com layout melhorado
            st.markdown("### 🔑 Digite sua matrícula:")
            st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
            
            col_input, col_btn = st.columns([4, 1], gap="medium")
            
            with col_input:
                matricula = st.text_input(
                    "Matrícula", 
                    placeholder="Digite sua matrícula (ex: 1234567)", 
                    label_visibility="collapsed",
                    key="matricula_input"
                )
            
            with col_btn:
                consultar = st.button("🔍 Consultar", use_container_width=True, type="primary")

            # Consultar quando o botão for pressionado
            if consultar:
                if matricula:
                    try:
                        # Converter matrícula para int
                        matricula_int = int(matricula)
                        
                        # Procurar pela matrícula (a coluna na planilha é 'MATRÍCULA' com acento)
                        aluno_data = data[data['MATRÍCULA'] == matricula_int]

                        if not aluno_data.empty:
                            # Extrair dados do aluno
                            nome = aluno_data.iloc[0]['Aluno']
                            av_01 = aluno_data.iloc[0]['AV. 01']
                            av_02 = aluno_data.iloc[0]['AV. 02']
                            
                            # Formatar notas para sempre ter 1 casa decimal
                            def formatar_nota(nota):
                                try:
                                    return f"{float(nota):.1f}"
                                except (ValueError, TypeError):
                                    return nota
                            
                            av_01_formatada = formatar_nota(av_01)
                            av_02_formatada = formatar_nota(av_02)
                            
                            # Verificar se o aluno fez as provas
                            av_01_faltou = pd.isna(av_01) or av_01 == 0 or str(av_01).strip() == '' or str(av_01).upper() == '#N/A'
                            av_02_faltou = pd.isna(av_02) or av_02 == 0 or str(av_02).strip() == '' or str(av_02).upper() == '#N/A'
                            
                            # Mostrar informações do aluno
                            st.markdown("<br>", unsafe_allow_html=True)
                            st.success("✅ Aluno encontrado!")
                            st.markdown(f"### 👤 {nome}")
                            st.markdown(f"**Matrícula:** {matricula_int}")
                            st.markdown("---")
                            
                            # Verificar se faltou alguma prova
                            if av_01_faltou and av_02_faltou:
                                st.error("⚠️ **Você não fez nenhuma das avaliações!**")
                                st.warning("📞 Procure seu professor ou coordenador do curso para verificar sua situação.")
                            elif av_01_faltou:
                                st.warning("⚠️ **Você não fez a Avaliação 01 (AV_01).**")
                                st.info("📞 Procure seu professor ou coordenador do curso.")
                                # Mostrar apenas AV_02
                                st.markdown(f"""
                                <div class="result-card">
                                    <div style="text-align: center;">
                                        <div class="nota-box" style="max-width: 300px; margin: 0 auto;">
                                            <div class="nota-label">📝 Avaliação 02</div>
                                            <div class="nota-valor">{av_02_formatada}</div>
                                        </div>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                            elif av_02_faltou:
                                st.warning("⚠️ **Você não fez a Avaliação 02 (AV_02).**")
                                st.info("📞 Procure seu professor ou coordenador do curso.")
                                # Mostrar apenas AV_01
                                st.markdown(f"""
                                <div class="result-card">
                                    <div style="text-align: center;">
                                        <div class="nota-box" style="max-width: 300px; margin: 0 auto;">
                                            <div class="nota-label">📝 Avaliação 01</div>
                                            <div class="nota-valor">{av_01_formatada}</div>
                                        </div>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                            else:
                                # Mostrar ambas as notas normalmente
                                st.markdown(f"""
                                <div class="result-card">
                                    <h2 style="text-align: center; margin-bottom: 5px;">✅ Suas Notas</h2>
                                    <div class="aluno-nome">{nome}</div>
                                    <div style="display: flex; gap: 20px; margin-top: 30px;">
                                        <div class="nota-box" style="flex: 1;">
                                            <div class="nota-label">📝 Avaliação 01</div>
                                            <div class="nota-valor">{av_01_formatada}</div>
                                        </div>
                                        <div class="nota-box" style="flex: 1;">
                                            <div class="nota-label">📝 Avaliação 02</div>
                                            <div class="nota-valor">{av_02_formatada}</div>
                                        </div>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                            
                        else:
                            st.error("❌ Matrícula não encontrada. Verifique se digitou corretamente.")
                            
                    except ValueError:
                        st.error("❌ Por favor, digite apenas números na matrícula.")
                    except KeyError as e:
                        st.error(f"❌ Erro ao acessar coluna: {e}")
                        st.info(f"Colunas disponíveis: {list(data.columns)}")
                    except Exception as e:
                        st.error(f"❌ Erro ao processar: {e}")
                else:
                    st.warning("⚠️ Por favor, digite sua matrícula.")
    else:
        st.warning("⚠️ Dados desta turma ainda não estão disponíveis. Por favor, selecione outra turma.")
else:
    st.info("👆 Selecione sua turma acima para começar a consulta.")
