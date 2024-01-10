import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='projeto | dash', layout='wide')

# data = pd.read_csv('./dados.csv', sep=',', encoding='utf-8')
data = pd.read_csv('./dados.csv', sep=',', encoding='utf-8')[['numero_processo', 'nome_ofertante', 'valor_total', 'data_abertura_processo']]

data['data_abertura_processo'] = pd.to_datetime(data['data_abertura_processo'])

data = data.sort_values('data_abertura_processo')

data['year'] = data['data_abertura_processo'].apply(lambda x: str(x.year))

# data['year'].append('todos')

year = st.sidebar.selectbox('Ano', data['year'].unique())

data = data.sort_values('nome_ofertante')

data['ofertante'] = data['nome_ofertante'].apply(lambda x: str(x)[:15] + ' ... ' + str(x)[len(str(x))-5:])

ofertante = st.sidebar.selectbox('Ofertante', data['nome_ofertante'].unique())


data_filered = data[data['year'] == year]

data_filered = data[data['nome_ofertante'] == ofertante]

data_filered

fig = px.line(data_filered, x="data_abertura_processo", y="valor_total", color="data_abertura_processo", line_group="data_abertura_processo", hover_name="data_abertura_processo",  line_shape="spline", render_mode="svg")
fig

bar_increase_chart = px.bar(data, x='valor_total', y='ofertante', orientation='h')
bar_increase_chart
