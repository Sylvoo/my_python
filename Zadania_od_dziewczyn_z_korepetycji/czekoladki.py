w1 = int(input("Liczba kostek w poziomie 1 dziecka: "))
w2 = int(input("Liczba kostek w pionie 1 dziecka: "))
k1 = int(input("Liczba kostek w poziomie 2 dziecka: "))
k2 = int(input("Liczba kostek w pionie 2 dziecka: "))

print(w1, w2, k1, k2)

kostki_Antka = 0
kostki_Zuzi = 0

kostki_Antka = w1 * w2
kostki_Zuzi = k1 * k2

sumaryczny = kostki_Antka + kostki_Zuzi

print(f'Calkowita liczba kostek to: {sumaryczny}')
