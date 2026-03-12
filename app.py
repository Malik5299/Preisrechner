import streamlit as st
import math

st.set_page_config(page_title="Preisrechner", page_icon="💰")
st.title("Preisrechner")

weight = st.number_input("Gewicht in Gramm", min_value=0.0, step=1.0)

# Zeit-Eingabe aufgeteilt in Stunden und Minuten
col_h, col_m = st.columns(2)
with col_h:
    hours = st.number_input("Druckzeit (Stunden)", min_value=0, step=1)
with col_m:
    minutes = st.number_input("Druckzeit (Minuten)", min_value=0, max_value=59, step=1)

# Umrechnung der Zeit in Gesamtminuten für die Kostenrechnung
total_minutes = (hours * 60) + minutes

aufwand = st.radio("Aufwand", options=[1.0, 2.0, 3.0], 
                   format_func=lambda x: {3.0: "Design (3,00€)", 2.0: "Bearbeitet (2,00€)", 1.0: "Nur Druck (1,00€)"}[x])

multi_color = 1.0 if st.checkbox("Mehrfarbig? (+1,00€)") else 0.0

filament_kosten = weight * (25.99 / 1000)
zeit_kosten = total_minutes * 0.01
selbstkosten = filament_kosten + zeit_kosten + aufwand + multi_color

# Berechnung mit 20% Gewinn
preis_mit_gewinn = selbstkosten * 1.20
mindestpreis = 3.00

if preis_mit_gewinn < mindestpreis:
    final_preis = mindestpreis
else:
    # Aufrunden auf den nächsten 50-Cent-Schritt
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
    st.write(f"Dauer: {hours}h {minutes}min")
    st.write(f"Netto-Selbstkosten: {selbstkosten:.2f} €")
    st.write(f"Gewinnmarge (20%): {selbstkosten * 0.20:.2f} €")
    if preis_mit_gewinn < mindestpreis:
        st.caption(f"Info: Mindestpreis von {mindestpreis:.2f} € wurde angewendet.")

with col_b:
    st.markdown(f"### **Endbetrag**")
    st.header(f"{final_preis:.2f} €")

if final_preis >= 10.0:
    st.balloons()
