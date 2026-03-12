weight = float(input("Gewicht in gramm: "))
print_time = float(input("Druckzeit in min: "))
working_time = float(input("selbst designt: 3, bearbeitet: 2, nur gedruckt: 1 "))

multi_color_input = input("Mehrfarbig? (j/n) ")
multi_color = 1.0 if multi_color_input == "j" else 0.0

total_material_cost = 0
has_bought = input("Materialien gekauft? (j/n) ")

if has_bought == "j":
    while True:
        material_price = float(input("Materialpreis pro Stück: "))
        material_number = float(input("Anzahl der Materialien: "))
        total_material_cost += material_price * material_number
        more = input("Möchten Sie weitere Materialien hinzufügen? (j/n) ")
        if more == "n":
            break

price = weight * (25.99/1000) + print_time * 0.01 + working_time + total_material_cost + multi_color
print("Der aktuelle Preis beträgt: " + str(price) + "€")

addition = float(input("-2€ bis +2€ "))

print("\n" + "="*30)
print("          QUITTUNG          ")
print("="*30)
print(f"Filamentkosten:     {weight * (25.99/1000):>7.2f}€")
print(f"Druckzeit-Kosten:   {print_time * 0.01:>7.2f}€")
print(f"Arbeitszeit:        {working_time:>7.2f}€")
print(f"Zusatzmaterialien:  {total_material_cost:>7.2f}€")
print(f"Mehrfarbig-Aufschlag:{multi_color:>7.2f}€")
print(f"Manuelle Anpassung: {addition:>7.2f}€")
print("-" * 30)
print(f"GESAMTPREIS:        {price + addition:>7.2f}€")
print("="*30)