import streamlit as st
import math

st.set_page_config(page_title="3D-Druck Kalkulator", page_icon="💰")
st.title("💰 Profi-Druckrechner")

weight = st.number_input("Gewicht in Gramm", min_value=0.0, step=1.0)
print_time = st.number_input("Druckzeit in Minuten", min_value=0.0, step=1.0)
working_time = st.radio("Arbeitsaufwand", options=[1.0, 2.0, 3.0], format_func=lambda x: {3.0: "Selbst designt (3€)", 2.0: "Bearbeitet (2€)", 1.0: "Nur gedruckt (1€)"}[x])

multi_color_input = st.checkbox("Mehrfarbig? (+1€)")
multi_color = 1.0 if multi_color_input else 0.0

total_material_cost = 0.0
has_bought = st.toggle("Zusätzliche Materialien gekauft?")

if has_bought:
    rows = st.number_input("Anzahl verschiedener Material-Posten", min_value=1, step=1)
    for i in range(int(rows)):
        col1, col2 = st.columns(2)
        with col1:
            m_price = st.number_input(f"Preis pro Stück (Posten {i+1})", min_value=0.0, key=f"p_{i}")
        with col2:
            m_num = st.number_input(f"Anzahl (Posten {i+1})", min_value=0.0, key=f"n_{i}")
        total_material_cost += m_price * m_num

# 1. Grundkosten berechnen
base_price = weight * (25.99 / 1000) + print_time * 0.01 + working_time + total_material_cost + multi_color

# 2. 30% Gewinn aufschlagen
with_profit = base_price * 1.30

# 3. Auf den nächsten 0,50€-Schritt aufrunden
# Logik: Preis verdoppeln, auf nächste Ganzzahl runden, wieder halbieren
final_rounded = math.ceil(with_profit * 2) / 2

st.divider()

addition = st.slider("Manuelle Anpassung (Offset -2€ bis +2€)", -2.0, 2.0, 0.0, step=0.1)
end_result = final_rounded + addition

st.subheader("🧾 QUITTUNG")
c1, c2 = st.columns(2)
with c1:
    st.write(f"Material/Strom/Zeit: {base_price:.2f}€")
    st.write(f"Gewinn-Marge (30%): {(base_price * 0.30):.2f}€")
with c2:
    st.write(f"Rundungs-Differenz: {(final_rounded - with_profit):.2f}€")
    st.write(f"Manuelle Anpassung: {addition:.2f}€")

st.success(f"### ENDPREIS: {end_result:.2f}€")
