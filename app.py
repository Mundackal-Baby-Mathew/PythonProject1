import streamlit as st
st.title("Hello Streamlit")
st.write("Click a button below")
if st.button("Say Hello"):
	st.success("Hello World")
if st.button("Say Good Bye"):
	st.warning("Good Bye")
