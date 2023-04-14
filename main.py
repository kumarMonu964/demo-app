#import the streamlit library as st
import streamlit as st
import pandas as pd
import numpy as np
# from matplotlib import pyplot as plt
table=pd.DataFrame({"Sr.NO":[1,2,3,4,5],"Age":[23,34,54,12,32]})
#create title of the page
st.title(" Welcome to STREAMlit(Title)")
st.header('This is my "Header"')
st.subheader("This is my the 'Subheader'")
st.text("Hi,This is the text area")

# for markdown(like in Jupyter)
st.markdown('---') # to mark a horizontal line
st.markdown('**bold** word')
st.markdown('*italic* word')
st.markdown('> ### Introduction to ML')  #block quote

# to provide a link
st.markdown('[Google](https://www.google.co.in/)')

# for captions
st.caption('this is a caption')

# latex(meaning ..mathematical functions ,matrics, vectors,formulas etc.)
st.latex(r"\begin{pmatrix}10&12\\-12&-23\end{pmatrix}")
# the code above creates a 2 by 2 matrix

#json function
json={"a":"1,2,3","b":"a,q,x"}
st.json(json)

# code function
code="""
print('hello world)
def fun():
    return 0; 
"""
st.code(code,language="python")

#write function 
st.write(" ## header2")

#matrix function
st.metric(label="wind speed", value="120ms⁻¹",delta="1.4ms⁻¹")

# create a table using pandas
st.table(table) # this is a static table

# to create interactive table 
st.dataframe(table)  # can change the order of the values in the table

# # fixing images and videos to the app
# st.image("image.png",caption="Riots took place on Ram Navmi as Hindus were peacefully performing their processions.",width=500)

# st.audio("audio.m4a")

# st.video("video.mp4")

# to remove the top-right button from streamlit app and the watermark
st.markdown("""
<style>
.css-1rs6os.edgvbvh3
{
    visibility: hidden;
}
.css-cio0dv.egzxvld1
{
    visibility: hidden;
}
</style>
""",unsafe_allow_html=True)

# making a checkbox
state=st.checkbox("checkbox",value=True)
if state :
    st.write("Box,is ticked")
else:
    st.write("please,tick the box")

def change():
    print(st.session_state.checker)
state=st.checkbox("Tickbox",value=True,on_change=change,key="checker")

#radio button
radio_btn= st.radio("Describe yourself:",options=("Student","Fresher","Employeed","Businessman"))
print(radio_btn)

#implementing BUTTON
def fun1():
    print("Button was clicked!")
btn=st.button("CLICK ME!",on_click=fun1)

#implementing selectbox (dropdown selecting)
select = st.selectbox("Which place would you like to visit?",options=("Paris","UK",'USA','Bahamas','Bali'))

#implementing multiselect (can choose multiple selectboxes)
mult = st.multiselect("Which social media app do you use?",options=("Snap_chat","Facebook",'Instagram','Tinber','Bumble','Telegram','WhatsApp'))
print(mult)
st.write(mult)

#-------------------------------------------------
# uploading files
st.title("Uploading Files...")
image=st.file_uploader("Please upload an image",type=["png",'jpeg','jpg'])
if image is not None:
    st.image(image)

#can also upload multiple files
images = st.file_uploader("Please upload multiples images",type=['png','jpeg','jpg'],accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)

#adding the Flourish link
st.markdown("[Floursh_BAR-CHART_RACE](https://public.flourish.studio/visualisation/13209394/)")

# implementing Slider
# slide=st.slider("This is a slider",min_value=18,max_value=58)
# print(slide)

st.select_slider("this is a select_slider",options=('1','2','3','4','5'))

#implementing text input
# val = st.text_input("Enter your name",max_chars=20
# )
# print(val)

st.text_area("Describe Yourself:")

# date input
st.date_input("Date of Birth:")

# time input
from datetime import time
import time as ts

def converter(value):
    m,s,ms =value.split(":")
    t_s=int(m)*60+int(ms)/1000
    return t_s

val=st.time_input("set timer!",value=time(0,0,0))
if str(val) == "00:00:00":
    st.write("set time!")
else:
    sec=converter(str(val))
    print(sec)
    bar=st.progress(0)
    per=sec/100
    stat=st.empty()
    for i in range(100):
        bar.progress(1+i)
        stat.write(str(i+1)+'%')
        ts.sleep(1)


# the forms widget
# for application

st.markdown(" --- ")
st.markdown("<H1> The application form: </H1>",unsafe_allow_html=True)
st.markdown("<i>> Please fill the following application form carefully</i>",unsafe_allow_html=True)

#create a form object
# form=st.form("form1")
# first=form.text_input('First Name:')
# last=form.text_input("Last Name:")
# print(f"First_name: {first}\nLast_name: {last}")
# form.form_submit_button('Submit')


# create a column widget(type of form)
with st.form("form2"):
    col1,col2=st.columns(2)
    col1.text_input("First Name:",max_chars=10)
    col2.text_input("Last Name:",max_chars=10)
    st.text_input("Email address:")
    col3,col4=st.columns(2)
    code1=col3.text_input("Password:")
    code2=col4.text_input("Confirm Password:")
    if (code1 != "") and (code2 != "") and code1 != code2:
        st.write("Passwords didn't match. Please try again.")

    st.form_submit_button("Submit")

st.markdown(" --- ")
    
with st.form("form3",clear_on_submit=True):
    st.markdown("<h1 style='text-align:center;'>Largest Number Calculator</h1>",unsafe_allow_html=True)
    st.markdown("><i>  This calculator outputs the greatest of the 3 numbers.</i>",unsafe_allow_html=True)
    col5,col6,col7=st.columns(3)
    a=col5.number_input("Enter first number:",step=1)
    b=col6.number_input("Enter second number:",step=1)
    c=col7.number_input("Enter third number:",step=1)
    state=st.form_submit_button("Find the largest Number")
    res=max(a,b,c)
    st.write(f"The largest number is {res} .")
    

# implementing sidebar
st.sidebar.radio('select',options=("line",'bar','hist'))


st.header("---End of the page---")

