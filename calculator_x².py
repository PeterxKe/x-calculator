import streamlit as st

st.sidebar.title("Menü")
wahl = st.sidebar.selectbox("Option wählen", ["x²", "x³", "x*2", "Über diese APP"])

if wahl == "Über diese APP":
    st.header("Mitwirkende")
    st.markdown("[• Peter Kemmeter (peterxke) – Entwickler](https://github.com/PeterxKe)")
    st.write("• Copilot – KI‑Support")

    st.divider()

    st.header("Über diese App")
    st.write("Version 1.0.0")
    st.write("Erstellt 05.06.2026")
    st.write("Hochgeladen 06.06.2026")

    st.divider()

    st.header("Weitere APPs")
    st.markdown("[• Lotto-web](https://lotto-web.streamlit.app)")

else:
    if wahl == "x²":
        st.title("x²")
    elif wahl == "x³":
        st.title("x³")
    elif wahl == "x*2":
        st.title("x*2")
    else:
        st.title("x²")

    zahl = st.number_input("Zahl eingeben", 1,)
    if st.button("Berechnen"):
        if wahl == "x²":
            st.write("Ergebnis:", zahl ** 2)
        elif wahl == "x³":
            st.write("Ergebnis:", zahl ** 3)
        elif wahl == "x*2":
            st.write("Ergebnis:", zahl * 2)
