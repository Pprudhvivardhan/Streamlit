import streamlit as st
import pandas as pd

#title
st.title('Prudhvi VardhanStartup')
#header
st.header('Guy with Patence')

#subheader
st.subheader('Yeah i know')

#write
st.write('always be calm in life so that everything will happen')

#markdown
st.markdown("""

### Things i like Most
- Food
- Alone
- cars
- Datascience

""")

# for displaying code
st.code("""
def foo(input):
    return foo*2

x= foo(2)
""")

#for any mathamatical formula
st.latex('x^2 + y^3 = 4')


# displaying dataframes
df =pd.DataFrame({
    'NAME':['Jack','sai','akbar'],
    'Marks':[10,30,20],
    'package':[90,80,40]
})

st.dataframe(df)


#displaying metrics
st.metric('revenue_PROFIT','Rs 3L' ,'93%')

st.metric('revenue_LOSS','Rs 3L' ,'-0.3%')


# displaying json
st.json(
{
    'NAME':['Jack','sai','akbar'],
    'Marks':[10,30,20],
    'package':[90,80,40]
}
)

#displaying media
st.image('AAPC.jpg')

st.video('roadmap.mp4')

# creating layouts
#sidebar
st.sidebar.title('side bar')

#columns
col1,col2=st.columns(2)
with col1 :
    st.image('AAPC.jpg')
with col2:
    st.image('AAPC.jpg')

#showing status

st.error('login failed')
st.success('login successful')
st.info('info')
st.warning('warning')

#progress bar

bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

# Taking user input

# Text input
email = st.text_input('Enter mail')

# number input
number = st.number_input('Enter_age')

# date input
date =st.date_input('enter date')


# some functionality
email =st.text_input('Enter_email')
password =st.text_input('Enter_password')
gender= st.selectbox('select gender',['male','female'])

btn = st.button('Login')

if btn:
    if email == 'prudhviperumandla@gmail.com'and password =='1234':
        st.success('login Successful')
        st.balloons()
        st.write(gender)
        st.image('img.png')

    else:
        st.error('login Failed')
file = st.file_uploader('Upload a csv file')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())

