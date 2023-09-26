def scilci_cilcist_tsifr_ta_bukv(ryadok):
    cilcist_tsifr = 0
    cilcist_bukv = 0
    for simvol in ryadok:
        if simvol.isalpha():
            cilcist_bukv += 1
        elif simvol.isdigit():
            cilcist_tsifr += 1
    return cilcist_bukv, cilcist_tsifr
ryadok = input("Введіть рядок: ")
bukvi, tsifri = scilci_cilcist_tsifr_ta_bukv(ryadok)
print(f"Кількість літер: {bukvi}")
print(f"Кількість цифр: {tsifri}")