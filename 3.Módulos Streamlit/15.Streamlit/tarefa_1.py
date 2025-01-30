

""""

Acesse os links abaixo, leia o conteúdo e crie uma aplicação com streamlit
reproduzindo pelo menos 20 códigos extraídos das páginas.
•https://docs.streamlit.io/en/stable/getting_started.html
•https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html
•https://docs.streamlit.io/en/stable/advanced_concepts.html
•https://docs.streamlit.io/en/stable/caching.html
•https://docs.streamlit.io/en/stable/api.html
•https://docs.streamlit.io/en/stable/session_state_api.html
•https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py


""""


import streamlit as st
import pandas as pd


st.title('Tarefa 1 de Streamlit - EBAC')


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

#4
import numpy as np

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


#5
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

#6
x = st.slider(':0:')  #  this is a widget
st.write(x, 'squared is', x * x)

#7
x = st.slider('x')  # this is a widget
st.write(x, 'squared is', x * x)


#8
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#9
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#10
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

#11
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

#12

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

#13
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

#14
df = pd.DataFrame({
  'first column': [10, 20, 30, 40],
  'second column': [1, 2, 3, 4]
})

df

#15
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

#16
st.markdown("# Main page 🎈")

#17
st.sidebar.markdown("# Main page 🎈")

#18
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

#19
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

#20
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")