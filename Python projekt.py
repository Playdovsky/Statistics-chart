import csv
import matplotlib.pyplot as plt
# aby matplotlib.pyplot działał należy zainstalować moduł "pip install matplotlib"

def import_danych():
    with open('zgony_niemowlat.csv', newline='') as csvfile: # Własna nazwa użytkownika!
        odczyt = csv.reader(csvfile, delimiter=';', quotechar='"')
        for x in odczyt:
            if len(x) > 5 and x[5] == "2021" and x[3] == "Ogółem" and x[2] == "Ogółem":
                suma_2021 = float(x[6].replace(",", "."))
            elif len(x) > 5 and x[5] == "2020" and x[3] == "Ogółem" and x[2] == "Ogółem":
                suma_2020 = float(x[6].replace(",", "."))
            elif len(x) > 5 and x[5] == "2019" and x[3] == "Ogółem" and x[2] == "Ogółem":
                suma_2019 = float(x[6].replace(",", "."))
            elif len(x) > 5 and x[5] == "2018" and x[3] == "Ogółem" and x[2] == "Ogółem":
                suma_2018 = float(x[6].replace(",", "."))

    print("Współczynnik zgonów niemowląt (na 1000 urodzonych) ze wszystkich województw dla poszczególnych lat:")
    print("rok 2021: ", round(suma_2021, 2))
    print("rok 2020: ", round(suma_2020, 2))
    print("rok 2019: ", round(suma_2019, 2)) # aby wykazać że program działa prawidłowo przekłamałem statystykę o +0.1
    print("rok 2018: ", round(suma_2018, 2))
    obliczenia(suma_2018, suma_2019, suma_2020, suma_2021)


def obliczenia(suma_2018, suma_2019, suma_2020, suma_2021):
    roznica1918 = suma_2019 - suma_2018
    roznica2019 = suma_2020 - suma_2019
    roznica2120 = suma_2021 - suma_2020
    roznicaproc1918 = ((suma_2019*100)/suma_2018) - 100
    roznicaproc2019 = ((suma_2020*100)/suma_2019) - 100
    roznicaproc2120 = ((suma_2021*100)/suma_2020) - 100
    print("Różnica współczynników dla lat 2018 i 2019: ", round(roznica1918, 2), "(", round(roznicaproc1918, 2), "%)")
    print("Różnica współczynników dla lat 2019 i 2020: ", round(roznica2019, 2), "(", round(roznicaproc2019, 2), "%)")
    print("Różnica współczynników dla lat 2020 i 2021: ", round(roznica2120, 2), "(", round(roznicaproc2120, 2), "%)")
    wybor(
        suma_2018, suma_2019, suma_2020, suma_2021,
        roznica1918, roznica2019, roznica2120,
        roznicaproc1918, roznicaproc2019, roznicaproc2120
    )


def wybor(
        suma_2018, suma_2019, suma_2020, suma_2021,
        roznica1918, roznica2019, roznica2120,
        roznicaproc1918, roznicaproc2019, roznicaproc2120
    ):
    print("\nCo teraz zrobić?\n1. Wykazać dane na wykresie\n2. Przepisać dane do pliku")
    w = input()
    if w == "1":
        wykres(
            suma_2018, suma_2019, suma_2020, suma_2021,
            roznica1918, roznica2019, roznica2120,
            roznicaproc1918, roznicaproc2019, roznicaproc2120
        )
    elif w == "2":
        eksport_do_pliku(
            suma_2018, suma_2019, suma_2020, suma_2021,
            roznica1918, roznica2019, roznica2120,
            roznicaproc1918, roznicaproc2019, roznicaproc2120
        )
    else:
        print("Wybór nieprawidłowy. Proszę wybrać ponownie.")
        wybor(
            suma_2018, suma_2019, suma_2020, suma_2021,
            roznica1918, roznica2019, roznica2120,
            roznicaproc1918, roznicaproc2019, roznicaproc2120
        )


def eksport_do_pliku(
        suma_2018, suma_2019, suma_2020, suma_2021,
        roznica1918, roznica2019, roznica2120,
        roznicaproc1918, roznicaproc2019, roznicaproc2120
    ):
    s = input("Podaj nazwę pliku: ")
    with open('C://Users//tubix//Desktop/' + s, 'w+') as f:  # Należy zmienić nazwę użytkownika na swoją!
        f.write("Współczynnik zgonów niemowląt (na 1000 urodzonych) ze wszystkich województw dla poszczególnych lat:\n")
        f.write("rok 2021: " + str(round(suma_2021, 2)) + "\n")
        f.write("rok 2021: " + str(round(suma_2020, 2)) + "\n")
        f.write("rok 2021: " + str(round(suma_2019, 2)) + "\n")
        f.write("rok 2021: " + str(round(suma_2018, 2)) + "\n")
        f.write("Różnica współczynników dla lat 2018 i 2019: " + str(round(roznica1918, 2)) +
                " (" + str(round(roznicaproc1918, 2)) + "%)\n")
        f.write("Różnica współczynników dla lat 2019 i 2020: " + str(round(roznica2019, 2)) +
                " (" + str(round(roznicaproc2019, 2)) + "%)\n")
        f.write("Różnica współczynników dla lat 2020 i 2021: " + str(round(roznica2120, 2)) +
                " (" + str(round(roznicaproc2120, 2)) + "%)\n")

    print("\nCzy chcesz jeszcze narysować wykres? y/n")
    w = input()
    if w == "y":
        wykres(
            suma_2018, suma_2019, suma_2020, suma_2021,
            roznica1918, roznica2019, roznica2120,
            roznicaproc1918, roznicaproc2019, roznicaproc2120
        )


def wykres(
        suma_2018, suma_2019, suma_2020, suma_2021,
        roznica1918, roznica2019, roznica2120,
        roznicaproc1918, roznicaproc2019, roznicaproc2120
    ):
    lata = ["2018", "2019", "2020", "2021"]
    suma = [suma_2018, suma_2019, suma_2020, suma_2021]
    roznica = [roznica1918, roznica2019, roznica2120]
    roznicaproc = [roznicaproc1918, roznicaproc2019, roznicaproc2120]

    fig, axs = plt.subplots(2, 1, figsize=(6, 8))
    axs[0].bar(lata, suma, width=0.5, color='darkblue', edgecolor='black', linewidth=1.2, alpha=0.8)
    axs[0].set_title("Współczynniki zgonów niemowląt\n(na 1000 urodzonych)")
    axs[0].set_ylabel("Współczynnik")
    axs[0].set_ylim([0, 5])

    for i, v in enumerate(suma):
        axs[0].text(i - 0.1, v + 0.1, str(round(v, 1)), fontsize=10, color='black', fontweight='bold')

    axs[1].bar(lata[1:], roznicaproc, width=0.5, color='black', edgecolor='darkblue', linewidth=1.2, alpha=0.8,
               tick_label=lata[1:], align='center')
    axs[1].set_title("Różnica procentowa współczynników\npomiędzy latami")
    axs[1].set_ylabel("Procent %")
    axs[1].set_ylim([-10, 10])
    axs[1].axhline(y=0, color='k')

    for i, v in enumerate(roznicaproc):
        if v > 0:
            axs[1].text(i + -0.075, v + 0.5, str(round(v, 1)) + "%", fontsize=10, color='black', fontweight='bold')
        else:
            axs[1].text(i + -0.1, v + -1, str(round(v, 1)) + "%", fontsize=10, color='black', fontweight='bold')

    fig.tight_layout()
    plt.show()

    print("\nCzy chcesz jeszcze zapisać do pliku? y/n")
    w = input()
    if w == "y":
        eksport_do_pliku(
            suma_2018, suma_2019, suma_2020, suma_2021,
            roznica1918, roznica2019, roznica2120,
            roznicaproc1918, roznicaproc2019, roznicaproc2120
        )


if __name__ == '__main__':
    print("Statystyka zgonów niemowląt w latach 2018-2021")
    import_danych()