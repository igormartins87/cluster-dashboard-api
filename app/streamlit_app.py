import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Cluster Dashboard", layout="wide")

API_BASE_URL = "http://localhost:8000/api/v1"

def main():
    st.title("Cluster Dashboard")

    #sidebar para seleção dos cluster
    cluster_id = st.sidebar.selectbox(
        "Selecione o Cluster:"
        ["cluster_a","cluster_b","cluster_c"]
    )

    #botão para atualizar dados
    if st.sidebar.button("Atualizar Dados"):
        st.run()

    try:
        response = requests.get(f"{API_BASE_URL}/clusters/{cluster_id}")

        if response.status_code == 200:
            data = response.json()
            display_cluster_dashboard(data, cluster_id)
        else:

            st.error(f"Error: {response.status_code}")
    except requests. exceptions.ConnectionError:
        st.error("API não está rodando. Execute uvicorn")

    def display_cluster_dashboard(data, cluster_id):
        #Exibir os dados do dashbard

        #Informação do Cluster
        cluster_info = data['cluster_info']
        col1, col2, col3 =st.columns(3)

        with col1:
            st.metric("Cluster", f"{cluster_info['icon']} {cluster_info['name']}")
            st.metric("Status", cluster_info['status'])

        with col2:
            st.metric("Total Nodes", cluster_info['total_nodes'])
            st.metric("Available Nodes", cluster_info['available_nodes'])

        with col3:
            if cluster_info['grafana_url']:
                st.markdown(f"[Dashboard Grafana] ({cluster_info['grafana_url']})")

        #tabela de Jobs

        st.subheader("Job em Execução")
        jobs_df = pd.DataFrame(data['jobs'])
        st.dataframe(jobs_df, use_container_width=True)

        #Metrica





