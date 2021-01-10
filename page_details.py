import streamlit as st
from PIL import Image
#icon = Image.open(path)
st.set_page_config(page_title = 'Sanjeev', 
page_icon = ':)', layout = 'wide',
initial_sidebar_state = 'auto') #collapsed or expanded

def main():
  st.title('Hi All!')
  st.sidebar.success('Menu')
  #st.plotly_chart(fig) to display the plotly chart

if __name__ == '__main__':
  main()