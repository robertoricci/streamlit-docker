import streamlit as st
import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

def main():
    st.write(os.getenv())
    print(os.getenv('DATABASE_URL'))
    database_url = os.getenv('DATABASE_URL')
    st.title('Aplicativo Simples com Streamlit')

    user_input = st.text_input("Digite algo:")
    
    if user_input:
        st.write(f'Você digitou: {user_input}')
        st.write(f'valor: {database_url}')

if __name__ == "__main__":
    main()
