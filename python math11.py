def oyednatu_slova_z_probilami(kilkist_sliv):
    slova = []
    for _ in range(kilkist_sliv):
        slovo = input("Введіть слово: ")
        slovo_z_probilami = ' '.join(simvol for simvol in slovo)
        slova.append(slovo_z_probilami)
    rezultat_ryadka = ', '.join(slova)
    return rezultat_ryadka
kilkist_sliv = int(input("Введіть кількість слів: "))
rezultat_ryadka = oyednatu_slova_z_probilami(kilkist_sliv)
print("Результат:", rezultat_ryadka)