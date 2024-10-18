#streamlit run app.py
import streamlit as st
import numpy as np
import pandas as pd
import time

#Como escrever + criar tabela basica
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


#Usando np para cria uma grande tabela
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)



#estilizando os maiores valores da tabela
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=("col %d" %i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(color='red',axis=0))
    
    
    
#Criando tabela chart(com linhas que sobem e descem)
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



#Usa data set de 100 linhas 3 2 colunas, divide o valor aleatorio por 50 (para que seja proximo das cordenadas passadas) e soma as cordenadas
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-23.621387, -46.686359],
    columns=['lat', 'lon'])

st.map(map_data)



#Cria barra slider com valor(default) de 0 a 100 em que voce pode indicar função para alterar resultado
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'ao quadrado', x * x)



#Cria input e retorna sei valor 
i1 = st.text_input("Your name", key="name")
i1
# You can access the value at any point with:
st.session_state.name
i2 = st.text_input("Your age", key="age")
i2
st.session_state.age



#Cria checkbox que realiza alguma ação
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
    
    
# Cria caixa selecionavel
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['second column'])

'You selected: ', option



#Cria sidebar e adiciona input e slider
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider('Select a range of values',0.0, 100.0, (25.0,75.0)) # slider -> label, min value, max value, value



#Cria colunas, adiciona botao e radio para escolher opcoes
left_column, middle_collum,right_column = st.columns(3)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

middle_collum.write(123)
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
# chosen = right_column.radio('Sorting hat',("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
# st.write(f"You are in {chosen} house!") -> desta forma o erite não fica identado dentro da coluna da direita
    
    
    
#
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty() # -> label/placeholder
bar = st.progress(0) # -> cria barra

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

'...and now we\'re done!' # -> Tudo que vem apos o progresso da barra, so aparece dpois que terminada 

#Cache utiliza de api e datasets grandes
# @st.cache_data / st.cache_resource
# def long_running_function(param1, param2):
#     return …



#Session state cria variaveis como diconarios, onde se da para criar chaves e salvar na sessao
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)


#Se quiser uma img:
# your-project/
# ├── static/
# │   └── my_hosted-image.png
# └── streamlit_app.py
#st.image(<path-to-image>)


#
st.session_state.saas = False
@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.session_state.saas = True
        st.rerun()
        
@st.dialog("Resposta")    
def response():
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
    
st.sidebar.write("Vote for your favorite")
if st.sidebar.button("A"):
    vote("A") 
if st.sidebar.button("B"):
    vote("B")
    
if st.session_state.saas == True:
    response()
    st.session_state.saas = False
    
    
#
data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)
