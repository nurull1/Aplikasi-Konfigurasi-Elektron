import streamlit as st

st.write('Test Streamlit')
st.write('Random Text')
st.title('Aplikasi Konfigurasi Elektron')
st.write('Hello, *friend* :sunglasses:')

st.header('Aplikasi Penjumlahan Bilangan Numerik' , divider='rainbow')

angka_pertama = st.number_input('Masukan angka pertama')
st.write('The first number is ', angka_pertama)

angka_kedua = st.number_input('Masukan angka kedua')
st.write('The second number is ', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f"Angka pertama {angka_pertama} x Angka kedua {angka_kedua} = {operasi_matematika}")
         

