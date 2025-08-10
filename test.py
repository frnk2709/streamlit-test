import streamlit as st

st.title("Ertragswertverfahren für Mietwohngrundstücke")

a = st.number_input("Gib a ein:", value=0.0)
b = st.number_input("Gib b ein:", value=0.0)

if st.button("Berechne Summe"):
    summe = a + b
    st.success(f"Summe: {summe}")
