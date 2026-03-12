import streamlit as st

st.set_page_config(page_title="3D-Druck Kalkulator", page_icon="🖨️")
st.title("🖨️ 3D-Druck Preisrechner")

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

price = weight * (25.99 / 1000) + print_time * 0.01 + working_time + total_material_cost + multi_color

st.divider()
addition = st.slider("Manuelle Anpassung (Offset -2€ bis +2€)", -2.0, 2.0, 0.0, step=0.1)
final_price = price + addition

st.subheader("🧾 QUITTUNG")
c1, c2 = st.columns(2)
with c1:
    st.write(f"Filament: {weight * (25.99/1000):.2f}€")
    st.write(f"Druckzeit: {print_time * 0.01:.2f}€")
    st.write(f"Arbeit: {working_time:.2f}€")
with c2:
    st.write(f"Zusatzmaterial: {total_material_cost:.2f}€")
    st.write(f"Mehrfarbig: {multi_color:.2f}€")
    st.write(f"Anpassung: {addition:.2f}€")

st.success(f"### GESAMTPREIS: {final_price:.2f}€")
