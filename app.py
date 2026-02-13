import streamlit as st

st.title("Avaliador Estratégico de Currículo")

st.write("App em construção 🚀")

nome = st.text_input("Seu nome")
email = st.text_input("Seu email")
vaga = st.text_area("Descrição da vaga")

if st.button("Gerar análise"):
    st.success("Análise gerada com sucesso!")
    st.write("Nome:", nome)
    st.write("Email:", email)
    st.write("Vaga:", vaga)
