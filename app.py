import streamlit as st
import math

st.set_page_config(page_title="Preisrechner", page_icon="💰")
st.title("3D-Druck Preisrechner")

weight = st.number_input("Gewicht in Gramm", min_value=0.0, step=1.0)
print_time = st.number_input("Druckzeit in Minuten", min_value=0.0, step=1.0)

aufwand = st.radio("Aufwand", options=[0.5, 1.5], 
                   format_func=lambda x: {1.5: "Design/Bearbeitung (1,50€)", 0.5: "Nur Druck (0,50€)"}[x])

multi_color = 0.5 if st.checkbox("Mehrfarbig? (+0,50€)") else 0.0

filament_kosten = weight * (25.99 / 1000)
zeit_kosten = print_time * 0.01
selbstkosten = filament_kosten + zeit_kosten + aufwand + multi_color

preis_mit_gewinn = selbstkosten * 1.30
mindestpreis = 3.00

if preis_mit_gewinn < mindestpreis:
    final_preis = mindestpreis
else:
    final_preis = math.ceil(preis_mit_gewinn * 2) / 2

st.divider()

st.subheader("🧾 Zusammenfassung")

col1, col2, col3 = st.columns(3)
col1.metric("Material", f"{filament_kosten:.2f} €")
col2.metric("Zeit/Strom", f"{zeit_kosten:.2f} €")
col3.metric("Aufwand", f"{aufwand + multi_color:.2f} €")

st.markdown("---")

col_a, col_b = st.columns(2)
with col_a:
    st.write("**Details zur Kalkulation:**")
    st.write(f"Netto-Selbstkosten: {selbstkosten:.2f} €")
    st.write(f"Gewinnmarge (30%): {selbstkosten * 0.30:.2f} €")
    if preis_mit_gewinn < mindestpreis:
        st.caption(f"Info: Mindestpreis von {mindestpreis:.2f} € wurde angewendet.")

with col_b:
    st.markdown(f"### **Endbetrag**")
    st.header(f"{final_preis:.2f} €")

if final_preis >= 10.0:
    st.balloons()
