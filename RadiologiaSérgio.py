import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Radiologia Clínica",
    page_icon="🩻",
    layout="centered"
)

# Cabeçalho
st.title("🩻 Radiologia Clínica")
st.subheader("Apoio Educacional em Diagnóstico por Imagem")

st.write(
    "Esta aplicação tem finalidade **educacional** e **acadêmica**, "
    "não substituindo avaliação médica especializada."
)

st.divider()

# Seleção da modalidade
st.subheader("📡 Modalidade de Imagem")

modalidade = st.selectbox(
    "Selecione a modalidade radiológica:",
    [
        "Radiografia (Raio-X)",
        "Tomografia Computadorizada (TC)",
        "Ressonância Magnética (RM)",
        "Ultrassonografia (USG)",
        "Medicina Nuclear"
    ]
)

st.divider()

# Indicação clínica
st.subheader("🩺 Indicação Clínica")

indicacao = st.selectbox(
    "Selecione a principal indicação:",
    [
        "Trauma",
        "Dor crônica",
        "Suspeita de neoplasia",
        "Avaliação infecciosa",
        "Avaliação vascular",
        "Rastreamento"
    ]
)

st.divider()

# Região anatômica
st.subheader("🧠 Região Anatômica")

regiao = st.multiselect(
    "Selecione a região avaliada:",
    [
        "Crânio",
        "Coluna vertebral",
        "Tórax",
        "Abdome",
        "Pelve",
        "Membros"
    ]
)

st.divider()

# Botão de análise
if st.button("🔍 Gerar Análise Radiológica"):
    st.subheader("📄 Análise Educacional")

    # Modalidade
    if modalidade == "Radiografia (Raio-X)":
        st.write(
            "**Radiografia** é indicada como exame inicial, "
            "avaliando estruturas ósseas, pulmões e alinhamentos."
        )

    elif modalidade == "Tomografia Computadorizada (TC)":
        st.write(
            "**TC** fornece avaliação detalhada em cortes axiais, "
            "sendo amplamente utilizada em trauma, emergência e oncologia."
        )

    elif modalidade == "Ressonância Magnética (RM)":
        st.write(
            "**RM** oferece excelente contraste de partes moles, "
            "sendo ideal para sistema nervoso central, musculoesquelético e tecidos moles."
        )

    elif modalidade == "Ultrassonografia (USG)":
        st.write(
            "**USG** é método dinâmico, sem radiação ionizante, "
            "frequentemente utilizado em abdome, obstetrícia e vascular."
        )

    elif modalidade == "Medicina Nuclear":
        st.write(
            "**Medicina Nuclear** avalia função metabólica e fisiológica, "
            "auxiliando no diagnóstico funcional de diversos órgãos."
        )

    st.divider()

    # Indicação clínica
    st.subheader("🧾 Considerações Clínicas")

    if indicacao == "Trauma":
        st.write(
            "Em contexto de trauma, prioriza-se métodos rápidos e sensíveis "
            "para identificação de fraturas, hemorragias e lesões internas."
        )

    elif indicacao == "Suspeita de neoplasia":
        st.write(
            "Na investigação oncológica, a correlação entre métodos de imagem "
            "é fundamental para estadiamento e planejamento terapêutico."
        )

    elif indicacao == "Avaliação infecciosa":
        st.write(
            "Achados como coleções, edema e alterações inflamatórias "
            "devem ser avaliados em conjunto com dados laboratoriais."
        )

    elif indicacao == "Avaliação vascular":
        st.write(
            "Métodos contrastados e técnicas específicas "
            "auxiliam na análise do fluxo e integridade vascular."
        )

    else:
        st.write(
            "O exame deve ser interpretado considerando histórico clínico, "
            "sinais, sintomas e exames complementares."
        )

    st.divider()

    # Regiões anatômicas
    st.subheader("📍 Regiões Selecionadas")

    for r in regiao:
        st.write(f"• {r}")

    st.success(
        "📘 Esta análise é um **apoio educacional** e não substitui "
        "o laudo radiológico emitido por médico especialista."
    )
