import streamlit as st

st.write('Test Streamlit')
st.write('Random Text')
st.title('Aplikasi Konfigurasi Elektron')
st.write('Hello, *friend* :sunglasses:')

atomic_number = st.number_input("Masukkan nomer atom:", min_value=1, value=1)
config = calculate_config(atomic_number)
st.write("Konfigurasi Elektron")
for shell, electrons in config:
    st.write(f"shell {shell}: {electrons} elektron")
if __name__ == "__main__":
    main()






         

