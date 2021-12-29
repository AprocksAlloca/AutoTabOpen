import webbrowser
import streamlit as st

st.title("Open all your tabs in a click")
st.write("Add all the links in the bellow text boxs and once added, click on 'Open Tabs'")
button = st.button("Open Tabs")


link_1 = st.text_input("Enter Link #1")
link_2 = st.text_input('Enter Link #2')
link_3 = st.text_input('Enter Link #3')
link_4 = st.text_input('Enter Link #4')
link_5 = st.text_input('Enter Link #5')


if button == True:
    webbrowser.open(link_1)
    webbrowser.open(link_2)
    webbrowser.open(link_3)
    webbrowser.open(link_4)
    webbrowser.open(link_5)