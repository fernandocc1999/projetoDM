import streamlit as st
from streamlit_option_menu import option_menu

# Função para mostrar a descrição dos campos
def get_tooltip(field):
    tooltips = {
        'age': 'Idade do cliente',
        'job': 'Tipo de trabalho (ex: "Administrador", "Operário", etc.)',
        'marital': 'Estado civil (ex: "Solteiro", "Casado", etc.)',
        'education': 'Nível educacional (ex: "Básico 4 anos", "Ensino Médio", etc.)',
        'default': 'Tem crédito em default? (ex: "Sim", "Não")',
        'housing': 'Tem empréstimo habitacional? (ex: "Sim", "Não")',
        'loan': 'Tem empréstimo pessoal? (ex: "Sim", "Não")',
        'contact': 'Tipo de comunicação do contacto (ex: "Telefone", "Celular")',
        'month': 'Último mês do contacto do ano (ex: "Jan", "Fev", etc.)',
        'day_of_week': 'Último dia da semana do contacto (ex: "Seg", "Ter", etc.)',
        'duration': 'Duração do último contacto em segundos',
        'campaign': 'Número de contactos realizados durante esta campanha e para este cliente',
        'pdays': 'Número de dias que passaram após o cliente ter sido contactado de uma campanha anterior',
        'previous': 'Número de contactos realizados antes desta campanha e para este cliente',
        'poutcome': 'Resultado da campanha de marketing anterior (ex: "Sucesso", "Falha", etc.)',
        'emp.var.rate': 'Taxa de variação do emprego - indicador trimestral',
        'cons.price.idx': 'Índice de preços ao consumidor - indicador mensal',
        'cons.conf.idx': 'Índice de confiança do consumidor - indicador mensal',
        'euribor3m': 'Taxa EURIBOR a 3 meses - indicador diário',
        'nr.employed': 'Número de empregados - indicador trimestral'
    }
    return tooltips.get(field, '')

# Dicionários para mapeamento das opções
job_options = {
    'admin.': 'Administrador',
    'blue-collar': 'Operário',
    'entrepreneur': 'Empreendedor',
    'housemaid': 'Empregada Doméstica',
    'management': 'Gestão',
    'retired': 'Reformado',
    'self-employed': 'Trabalhador Independente',
    'services': 'Serviços',
    'student': 'Estudante',
    'technician': 'Técnico',
    'unemployed': 'Desempregado',
    'unknown': 'Desconhecido'
}

marital_options = {
    'single': 'Solteiro',
    'married': 'Casado',
    'divorced': 'Divorciado',
    'unknown': 'Desconhecido'
}

education_options = {
    'basic.4y': 'Básico 4 anos',
    'basic.6y': 'Básico 6 anos',
    'basic.9y': 'Básico 9 anos',
    'high.school': 'Ensino Médio',
    'illiterate': 'Analfabeto',
    'professional.course': 'Curso Profissional',
    'university.degree': 'Ensino Superior',
    'unknown': 'Desconhecido'
}

binary_options = {
    'yes': 'Sim',
    'no': 'Não',
    'unknown': 'Desconhecido'
}

contact_options = {
    'cellular': 'Telemóvel',
    'telephone': 'Telefone'
}

month_options = {
    'jan': 'Jan',
    'feb': 'Fev',
    'mar': 'Mar',
    'apr': 'Abr',
    'may': 'Mai',
    'jun': 'Jun',
    'jul': 'Jul',
    'aug': 'Ago',
    'sep': 'Set',
    'oct': 'Out',
    'nov': 'Nov',
    'dec': 'Dez'
}

day_of_week_options = {
    'mon': 'Seg',
    'tue': 'Ter',
    'wed': 'Qua',
    'thu': 'Qui',
    'fri': 'Sex'
}

poutcome_options = {
    'failure': 'Falha',
    'nonexistent': 'Inexistente',
    'success': 'Sucesso'
}

# Título da aplicação
st.set_page_config(page_title='Formulário de Previsão de Depósito Bancário', page_icon='📈', layout='wide')
st.title('Formulário de Previsão de Depósito Bancário')

st.image('https://www.ipleiria.pt/wp-content/themes/ipleiria/img/logo_ipl_header.png', width=200)

# Menu de Navegação com Ícones
selected = option_menu(
    menu_title=None, 
    options=["Formulário", "Sobre"], 
    icons=["pencil-square", "info-circle"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal"
)

# Mensagem introdutória
st.markdown("""
Bem-vindo ao formulário de previsão de depósito bancário. Preencha as informações abaixo para ajudar a prever se um cliente irá subscrever um depósito a prazo.
""")

# Campos do formulário organizados em seções
if selected == "Formulário":
    with st.form(key='bank_form'):
        st.header('Informações Pessoais')
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input('Idade', min_value=18, max_value=100, help=get_tooltip('age'))
            job = st.selectbox('Trabalho', list(job_options.values()), help=get_tooltip('job'))
            marital = st.selectbox('Estado Civil', list(marital_options.values()), help=get_tooltip('marital'))
            education = st.selectbox('Educação', list(education_options.values()), help=get_tooltip('education'))

        with col2:
            default = st.selectbox('Crédito em Default', list(binary_options.values()), help=get_tooltip('default'))
            housing = st.selectbox('Empréstimo Habitacional', list(binary_options.values()), help=get_tooltip('housing'))
            loan = st.selectbox('Empréstimo Pessoal', list(binary_options.values()), help=get_tooltip('loan'))
        
        st.header('Detalhes do Contacto')
        col3, col4 = st.columns(2)

        with col3:
            contact = st.selectbox('Tipo de Contacto', list(contact_options.values()), help=get_tooltip('contact'))
            month = st.selectbox('Mês de Contacto', list(month_options.values()), help=get_tooltip('month'))
            day_of_week = st.selectbox('Dia da Semana de Contacto', list(day_of_week_options.values()), help=get_tooltip('day_of_week'))
            duration = st.number_input('Duração do Contacto (segundos)', min_value=0, help=get_tooltip('duration'))

        with col4:
            campaign = st.number_input('Número de Contactos na Campanha', min_value=0, help=get_tooltip('campaign'))
            pdays = st.number_input('Dias desde o Último Contacto na Campanha', min_value=0, max_value=999, help=get_tooltip('pdays'))
            previous = st.number_input('Número de Contactos Anteriores', min_value=0, help=get_tooltip('previous'))
            poutcome = st.selectbox('Resultado da Campanha Anterior', list(poutcome_options.values()), help=get_tooltip('poutcome'))
        
        st.header('Indicadores Económicos')
        col5, col6 = st.columns(2)

        with col5:
            emp_var_rate = st.number_input('Taxa de Variação do Emprego', help=get_tooltip('emp.var.rate'))
            cons_price_idx = st.number_input('Índice de Preços ao Consumidor', help=get_tooltip('cons.price.idx'))
            cons_conf_idx = st.number_input('Índice de Confiança do Consumidor', help=get_tooltip('cons.conf.idx'))
        
        with col6:
            euribor3m = st.number_input('Taxa EURIBOR a 3 Meses', help=get_tooltip('euribor3m'))
            nr_employed = st.number_input('Número de Empregados', min_value=0, help=get_tooltip('nr.employed'))
        
        # Botão para submeter o formulário
        submit_button = st.form_submit_button(label='Submeter')

    # Ação após o formulário ser submetido
    if submit_button:
        # Mapear os valores traduzidos de volta para os valores originais
        job_value = list(job_options.keys())[list(job_options.values()).index(job)]
        marital_value = list(marital_options.keys())[list(marital_options.values()).index(marital)]
        education_value = list(education_options.keys())[list(education_options.values()).index(education)]
        default_value = list(binary_options.keys())[list(binary_options.values()).index(default)]
        housing_value = list(binary_options.keys())[list(binary_options.values()).index(housing)]
        loan_value = list(binary_options.keys())[list(binary_options.values()).index(loan)]
        contact_value = list(contact_options.keys())[list(contact_options.values()).index(contact)]
        month_value = list(month_options.keys())[list(month_options.values()).index(month)]
        day_of_week_value = list(day_of_week_options.keys())[list(day_of_week_options.values()).index(day_of_week)]
        poutcome_value = list(poutcome_options.keys())[list(poutcome_options.values()).index(poutcome)]

        st.success('Formulário submetido com sucesso!')
        st.write('### Valores fornecidos:')
        st.write('Idade:', age)
        st.write('Trabalho:', job)
        st.write('Estado Civil:', marital)
        st.write('Educação:', education)
        st.write('Crédito em Default:', default)
        st.write('Empréstimo Habitacional:', housing)
        st.write('Empréstimo Pessoal:', loan)
        st.write('Tipo de Contacto:', contact)
        st.write('Mês do Contacto:', month)
        st.write('Dia da Semana de Contacto:', day_of_week)
        st.write('Duração do Contacto (segundos):', duration)
        st.write('Número de Contactos na Campanha:', campaign)
        st.write('Dias desde o Último Contacto na Campanha:', pdays)
        st.write('Número de Contactos Anteriores:', previous)
        st.write('Resultado da Campanha Anterior:', poutcome)
        st.write('Taxa de Variação do Emprego:', emp_var_rate)
        st.write('Índice de Preços ao Consumidor:', cons_price_idx)
        st.write('Índice de Confiança do Consumidor:', cons_conf_idx)
        st.write('Taxa EURIBOR a 3 Meses:', euribor3m)
        st.write('Número de Empregados:', nr_employed)

        # Exemplo de mensagem baseada nos valores fornecidos
        if default == 'Sim' or loan == 'Sim' or housing == 'Sim':
            st.write("Com base nos valores fornecidos, o cliente provavelmente não irá subscrever um depósito a prazo. 😢")
        else:
            st.write("Com base nos valores fornecidos, o cliente tem boas chances de subscrever um depósito a prazo. 😊")


# Seção Sobre
elif selected == "Sobre":
    st.markdown("""
    ### Sobre este Formulário
    Este formulário foi criado para ajudar na previsão de depósitos bancários, com base em dados históricos de campanhas de marketing.
    """)