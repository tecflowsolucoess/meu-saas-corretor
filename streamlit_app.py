import streamlit as st

st.set_page_config(page_title="BrokerAI - O Braço Direito do Corretor", layout="wide")

st.title("🏠 BrokerAI: Gestão e Vendas")
st.sidebar.title("Menu de Ferramentas")
opcao = st.sidebar.radio("O que vamos fazer agora?", 
                         ["Gerador de Anúncios", "Qualificador de Leads", "Catálogo Rápido"])

# --- 1. GERADOR DE ANÚNCIOS ---
if opcao == "Gerador de Anúncios":
    st.header("✍️ Gerador de Anúncios Magnéticos")
    detalhes = st.text_area("Descreva o imóvel (ex: 2 quartos, suite, varanda gourmet, Moema)")
    tom = st.selectbox("Tom de voz", ["Luxo/Sofisticado", "Urgência/Oportunidade", "Familiar/Aconchegante"])
    
    if st.button("Gerar Texto para Instagram/Zap"):
        # Aqui no futuro conectamos a API do Gemini/GPT
        st.success("Texto Sugerido:")
        st.write(f"**{tom}**: Viver em Moema nunca foi tão exclusivo! Este 2 quartos com suíte e varanda gourmet é o refúgio que sua família merece. Agende sua visita agora! 🚀 #ImoveisDeLuxo")

# --- 2. QUALIFICADOR DE LEADS ---
elif opcao == "Qualificador de Leads":
    st.header("🎯 Qualificador de Clientes (Filtro de Curiosos)")
    st.info("Envie este link para o cliente antes de atender no WhatsApp.")
    
    nome = st.text_input("Nome do Cliente")
    renda = st.select_slider("Renda mensal aproximada", options=["Até 5k", "5k a 10k", "10k a 20k", "Acima de 20k"])
    pretensao = st.date_input("Pretende comprar em quanto tempo?")
    
    if st.button("Enviar Dados para o Corretor"):
        st.write(f"Análise: Cliente {nome} tem perfil de compra para {pretensao}. Status: ✅ LEAD QUENTE")

# --- 3. CATÁLOGO RÁPIDO ---
elif opcao == "Catálogo Rápido":
    st.header("📋 Meus Imóveis")
    # Exemplo de mini banco de dados
    imoveis = [
        {"ref": "AP001", "valor": "R$ 500.000", "status": "Disponível"},
        {"ref": "CA002", "valor": "R$ 1.200.000", "status": "Reservado"}
    ]
    st.table(imoveis)
