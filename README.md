import os
import streamlit as st
from decimal import Decimal
from openpyxl import load_workbook

#Pfad zur excel-Datei
script_dir = os.path.dirname(__file__)
excel_path = os.path.join(script_dir, 'Liegschaftszinssatz_Tabelle.xlsx')

#Datei laden
try:
    wb = load_workbook(excel_path)
    ws = wb.active
    st.write('Wert in G6:', ws['G6'].value)
except FileNotFoundError:
    st.error('Datei nicht gefunden')

mieten = []
flaechen = []

vpi = {
    '2021': 104.3,
    '2022': 113.5,
    '2023': 117.8,
    '2024': 120.2
}

import streamlit as st

st.title("Ertragswertverfahren für Mietwohngrundstücke")

a = st.number_input("Gib a ein:", value=0.0)
b = st.number_input("Gib b ein:", value=0.0)

if st.button("Berechne Summe"):
    summe = a + b
    st.success(f"Summe: {summe}")
