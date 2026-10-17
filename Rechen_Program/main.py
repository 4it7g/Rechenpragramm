anfang = input("Willst du den Flächeninhalt oder das Volumen berechnen?\n")

if anfang == "Volumen":
        print("iuasdfhui")

elif anfang == "Flächeninhalt":
        rechenweg = input("Was willst du berechnen?\n1.Quadrat\n2.Rechteck\n3.Dreieck\n4.Trapez\n")

        if rechenweg == "Quadrat":
                print("Gebe jetzt den Wert von einer Seite in cm an.")
                seite_Q = input("Seite = ")
                seite_Q = seite_Q.replace(',', '.')
                seite_Q = float(seite_Q)
                ergebnis_Q = eval(f"{seite_Q} * {seite_Q}")
                ergebnis_Q = round(ergebnis_Q, 2)
                print(f"Der Flächeninhalt beträgt {ergebnis_Q} cm^2.")

        elif rechenweg == "Rechteck":
                print("Gebe jetzt den Wert von Seite a und b in cm an.")
                seite_1_R = input("Seite a = ")
                seite_1_R = seite_1_R.replace(',', '.')
                seite_2_R = input("Seite b = ")
                seite_2_R = seite_2_R.replace(',', '.')
                seite_1_R = float(seite_1_R) #float erst hier da sonst replace nicht geht.
                seite_2_R = float(seite_2_R) 
                ergebnis_R = eval(f"{seite_1_R} * {seite_2_R}")
                ergebnis_R = round(ergebnis_R, 2)
                print(f"Der Flächeninhalt beträgt {ergebnis_R} cm^2.")

        elif rechenweg == "Dreieck":
                print("Gebe jetzt den Wert von allen Seiten also a, b und c in cm an.")
                seite_1_D = input("Seite 1 = ")
                seite_1_D = seite_1_D.replace(',', '.')
                seite_2_D = input("Seite 2 = ")
                seite_2_D = seite_2_D.replace(',', '.')
                seite_3_D = input("Seite 3 = ")
                seite_3_D = seite_3_D.replace(',', '.')
                seite_1_D = float(seite_1_D)
                seite_2_D = float(seite_2_D)
                seite_3_D = float(seite_3_D)
                halber_umfang = eval(f"({seite_1_D} + {seite_2_D} + {seite_3_D}) / 2")
                fläche_Heron = eval(f"({halber_umfang} * ({halber_umfang} - {seite_1_D}) * ({halber_umfang} - {seite_2_D}) * ({halber_umfang} - {seite_3_D})) ** 0.5")
                höhe_D = eval(f"2 * {fläche_Heron} / seite_1_D")
                ergebnis_D = eval(f"({seite_1_D} * {höhe_D}) / 2")
                ergebnis_D = round(ergebnis_D, 2)
                print(f"Der Flächeninhalt beträgt {ergebnis_D} cm^2.")

        elif rechenweg == "Trapez":
                print("Trapez also.")

        else:
                print("Hast du vieleicht was falsch geschrieben?")

else:
        print("Hast du vieleicht was falsch geschrieben?")
