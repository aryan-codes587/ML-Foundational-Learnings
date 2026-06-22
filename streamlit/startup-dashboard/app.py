import streamlit as st
import pandas as pd
st.title('Startup Dashboard')
st.header('I am learning streamlit')
st.subheader("And I'm loving it!")

st.write('This is normal Text')

st.markdown(""""
### My Favourite Movies :- 
- Interstaller
- Prestige
- John Wick
- Rocky Handsome
- Creed 
""")

st.code("""
def foo(input)
    return foo**2

x = foo(2)
""")

st.latex('x^2 + y^2 + 2 = 0')


df = pd.DataFrame({
    'name' : ["Nitish","Ankit","Anupam"],
    'marks' : [50,60,70],
    'package' : [10,12,14]
})

st.dataframe(df)

st.metric('Revenue','Rs 3L','+3%')

st.json({
    'name' : ["Nitish","Ankit","Anupam"],
    'marks' : [50,60,70],
    'package' : [10,12,14]
})