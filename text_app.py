import streamlit as st
import pandas as pd

st.title('Streamlit Text Tutorials')
st.header('Coded by Sanjeev')
st.subheader('nsanjeevram@gmail.com')
st.text('Thanks for visiting!')
st.markdown('#### Bye!')
st.success('Success')
st.error('Error!')
st.warning('Please do not do this!')
st.info('Thanks again')
st.exception('This is an exception')
st.write('-' * 20)
df = pd.read_csv('iris.csv')
st.dataframe(df)
st.table(df)
code = '''def hello():
            return "hello world!"
       '''
st.code(code, language = 'python')
st.write('-' * 20)
name = 'Sanjeev'
if st.button('Upper', key = 'k1'):
  st.write(f'Hi {name.upper()}')
if st.button('Lower', key = 'k2'):
  st.write(f'Hi {name.lower()}')

status = st.radio('Are you single?', ('Yes', 'No'))
if status == 'Yes':
  st.info('Ok')
elif status == 'No':
  st.info('ok!')

if st.checkbox('Show/Hide'):
  st.write('This is a secret!')

with st.beta_expander('Reveal Secret'):
  st.write('Hi!')

choice = st.selectbox("Language", ['Python', 'C', 'Java'])
st.write(f'You have chosen {choice}')

multisel = st.multiselect('Food', ('Indian', 'Chinese', 'South Indian', 'North Indian'), default = 'South Indian')

age = st.slider('Age', 1, 100, 1)
slider = st.select_slider("Choose Slider", options = ['A', 'B', 'C', 'D', 'E'], value = ('A', 'B'))


#st.image(image_url) or
#from PIL import Image
#st.image(Image.open(local_path), use_column_width = True)

name = st.text_input('Name')
st.info(name)
message = st.text_area('Message', height = 100)
st.write(message)
age = st.number_input('Age', 1, 25)# or 1.0 to 25.0
date = st.date_input('Exam date')
time = st.time_input('Exam time')
pas = st.text_input('Password', type = 'password')
color = st.beta_color_picker('Select Color')


