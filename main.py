import webbrowser
import streamlit as st
from datetime import datetime, timedelta
from threading import Timer


st.title("Open all your tabs in a click")
st.write("Add all the links in the bellow text boxs and once added, click on 'Open Tabs'")
button = st.button("Open Tabs")


#link_1 = st.text_input("Enter Link #1")
#link_2 = st.text_input('Enter Link #2')
#link_3 = st.text_input('Enter Link #3')
#link_4 = st.text_input('Enter Link #4')
#link_5 = st.text_input('Enter Link #5')

link_1 = "https://my.kis.in/"
link_2 = "https://mail.google.com/mail/u/0/#inbox"
link_3 = "https://classroom.google.com/u/0/h"
link_4 = "https://docs.google.com/document/u/0/?tgif=c"
link_5 = "https://www.instagram.com/direct/inbox/?hl=en"



#if button == True:
def openlinks():    
    webbrowser.open(link_1)
    webbrowser.open(link_2)
    webbrowser.open(link_3)
    webbrowser.open(link_4)
    webbrowser.open(link_5)
  
x=datetime.today()
y = x.replace(day=x.day, hour=8, minute=20, second=0, microsecond=0) + timedelta(days=0)
delta_t=y-x

secs=delta_t.total_seconds()

t = Timer(secs, openlinks)
t.start()

st.write("Time until tabs open: (H:M:S:MM)" , delta_t)

