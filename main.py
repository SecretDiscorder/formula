import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, simplify

import sympy as sp
import sys

import sympy as sp


def add_implicit_multiplication(expression):
    # Tambahkan operator '*' eksplisit sebelum variabel tanpa operator di antara mereka
    # Misalnya, ubah '3x+5y' menjadi '3*x+5*y'
    operators = {"x", "y"}
    new_expr = ""
    for i, char in enumerate(expression):
        new_expr += char
        if (
            char.isalpha()
            and i < len(expression) - 1
            and expression[i + 1] not in operators
        ):
            new_expr += "*"
    return new_expr


def plot_spldv(m, b, label):
    x_vals = np.linspace(-10, 10, 1000)
    y_vals = m * x_vals + b

    plt.plot(x_vals, y_vals, label=label)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)


def polinomial():
    x = sp.Symbol("x")
    f_x = sp.Function("f")(x)  # Menggunakan f(x) sebagai fungsi
    g_x = sp.Function("g")(x)  # Menggunakan g(x) sebagai fungsi

    print("Masukkan persamaan fungsi f(x) dan g(x) serta operator matematika.")
    print(
        "Contoh: 'f(x) = x**2 + 3*x - 4', 'g(x) = 2*x + 1', dan operator '+', '-', '*', '/'."
    )

    f_equation_str = input("Masukkan persamaan fungsi f(x): ")
    g_equation_str = input("Masukkan persamaan fungsi g(x): ")
    operator = input("Masukkan operator matematika (+, -, *, /): ")

    # Hitung persamaan f(x) dan g(x)
    f_x_expr = sp.sympify(f_equation_str.replace(" ", ""))
    g_x_expr = sp.sympify(g_equation_str.replace(" ", ""))

    # Perhitungan operasi antara f(x) dan g(x)
    result_expr = None
    if operator == "+":
        result_expr = f_x_expr + g_x_expr
    elif operator == "-":
        result_expr = f_x_expr - g_x_expr
    elif operator == "*":
        result_expr = f_x_expr * g_x_expr
    elif operator == "/":
        result_expr, _ = sp.div(f_x_expr, g_x_expr)
    elif operator == "%":
        quotient, remainder = sp.div(f_x_expr, g_x_expr)
        result_expr = remainder
    else:
        print(
            "Operator matematika tidak valid. Silakan gunakan '+', '-', '*', atau '/'."
        )
        return

    # Simplify the result expression
    result_expr = sp.expand(result_expr)

    # Tampilkan perhitungan persamaan fungsi dan operator matematika
    print("\nHasil Operasi:")
    print(f"f(x) = {f_x_expr}")
    print(f"g(x) = {g_x_expr}")
    print(f"Hasil (f(x) {operator} g(x)) = {result_expr}\n")

    # Persiapkan persamaan f(x) dan hasilnya untuk digambar dalam grafik SPLDV
    m_f_x = f_x_expr.as_coefficients_dict(x)[x]
    b_f_x = f_x_expr.subs(x, 0)
    m_result = result_expr.as_coefficients_dict(x)[x]
    b_result = result_expr.subs(x, 0)

    # Gambar grafik SPLDV f(x) dan hasil operasi
    plt.figure(figsize=(8, 6))
    plot_spldv(m_f_x, b_f_x, "f(x)")
    plot_spldv(m_result, b_result, f"f(x) {operator} g(x)")
    plt.legend()
    plt.title(f"Grafik SPLDV (f(x) dan f(x) {operator} g(x))")
    plt.show()


HURUF = {
    "h": "ꦲ",
    "n": "ꦤ",
    "c": "ꦕ",
    "r": "ꦫ",
    "k": "ꦏ",
    "d": "ꦢ",
    "t": "ꦠ",
    "s": "ꦱ",
    "w": "ꦮ",
    "l": "ꦭ",
    "p": "ꦥ",
    "dh": "ꦝ",
    "j": "ꦗ",
    "y": "ꦪ",
    "ny": "ꦚ",
    "m": "ꦩ",
    "g": "ꦒ",
    "b": "ꦧ",
    "th": "ꦛ",
    "ng": "ꦔ",
    ",": "꧈",
    ".": "꧉",
}

PASANGAN = {
    "h": "꧀ꦲ",
    "n": "꧀ꦤ",
    "c": "꧀ꦕ",
    "r": "꧀ꦫ",
    "k": "꧀ꦏ",
    "d": "꧀ꦢ",
    "t": "꧀ꦠ",
    "s": "꧀ꦱ",
    "w": "꧀ꦮ",
    "l": "꧀ꦭ",
    "p": "꧀ꦥ",
    "dh": "꧀ꦓ",
    "j": "꧀ꦗ",
    "y": "꧀ꦪ",
    "ny": "꧀ꦚ",
    "m": "꧀ꦩ",
    "g": "꧀ꦒ",
    "b": "꧀ꦧ",
    "th": "꧀ꦛ",
    "ng": "꧀ꦔ",
}

SANDHANGAN = {
    "wulu": "ꦶ",
    "suku": "ꦸ",
    "pepet": "ꦼ",
    "taling": "ꦺ",
    "taling-tarung": "ꦺꦴ",
    "cecak": "ꦁ",
    "wignyan": "ꦃ",
    "layar": "ꦂ",
    "cakra": "ꦿ",
    "keret": "ꦽ",
    "pengkal": "ꦾ",
    "pangkon": "꧀",
}


def transliterate(hrf, isend, prv, nxt):
    ltr = ""
    dobel = ["th", "dh", "ny"]
    iskeret = False
    if hrf.find("ng") == 0:
        if len(hrf) == 2:
            ltr += SANDHANGAN["cecak"]
        else:
            ltr += HURUF["ng"]
        if len(hrf) > 3:
            if hrf[2] == "l":
                ltr += PASANGAN["l"]
            elif hrf[2] == "y":
                ltr += SANDHANGAN["pengkal"]
            elif hrf[2] == "r":
                if hrf[3] == "e":
                    ltr += SANDHANGAN["keret"]
                    iskeret = True
                else:
                    ltr += SANDHANGAN["cakra"]
    elif hrf.find("ny") == 0:
        if prv:
            if len(prv) == 1:
                ltr += PASANGAN["ny"]
            else:
                ltr += HURUF["ny"]
        else:
            ltr += HURUF["ny"]
        if len(hrf) > 3:
            if hrf[2] == "l":
                ltr += PASANGAN["l"]
            elif hrf[2] == "y":
                ltr += SANDHANGAN["pengkal"]
            elif hrf[2] == "r":
                if hrf[3] == "e":
                    ltr += SANDHANGAN["keret"]
                    iskeret = True
                else:
                    ltr += SANDHANGAN["cakra"]
    elif hrf.find("th") == 0:
        if prv:
            if len(prv) == 1:
                ltr += PASANGAN["th"]
            else:
                ltr += HURUF["th"]
        else:
            ltr += HURUF["th"]
        if len(hrf) > 3:
            if hrf[2] == "l":
                ltr += PASANGAN["l"]
            elif hrf[2] == "y":
                ltr += SANDHANGAN["pengkal"]
            elif hrf[2] == "r":
                if hrf[3] == "e":
                    ltr += SANDHANGAN["keret"]
                    iskeret = True
                else:
                    ltr += SANDHANGAN["cakra"]
    elif hrf.find("dh") == 0:
        if prv:
            if len(prv) == 1:
                ltr += PASANGAN["dh"]
            else:
                ltr += HURUF["dh"]
        else:
            ltr += HURUF["dh"]
        if len(hrf) > 3:
            if hrf[2] == "l":
                ltr += PASANGAN["l"]
            elif hrf[2] == "y":
                ltr += SANDHANGAN["pengkal"]
            elif hrf[2] == "r":
                if hrf[4] == "e":
                    ltr += SANDHANGAN["keret"]
                    iskeret = True
                else:
                    ltr += SANDHANGAN["cakra"]
    if len(hrf) == 2:
        if hrf == "ng":
            ltr += SANDHANGAN["cecak"]
        else:
            if prv:
                if len(prv) == 1:
                    if prv not in ["h", "r", "y"]:
                        ltr += PASANGAN[hrf[0]]
                    else:
                        ltr += HURUF[hrf[0]]
                else:
                    ltr += HURUF[hrf[0]]
            else:
                ltr += HURUF[hrf[0]]
    elif len(hrf) == 1:
        if hrf[0] not in [",", "."]:
            if hrf == "r":
                ltr += SANDHANGAN["layar"]
            elif hrf == "h":
                ltr += SANDHANGAN["wignyan"]
            elif hrf == ",":
                pass
            else:
                if isend:
                    ltr += HURUF[hrf[0]]
                    ltr += SANDHANGAN["pangkon"]
                else:
                    ltr += HURUF[hrf[0]]

    elif len(hrf) > 2:
        if hrf[1] == "l":
            ltr += HURUF[hrf[0]]
            ltr += PASANGAN["l"]
        elif hrf[1] == "y" and hrf[0] != "n":
            ltr += HURUF[hrf[0]]
            ltr += SANDHANGAN["pengkal"]
        elif hrf[1] == "r":
            if prv:
                if len(prv) == 1:
                    if prv not in ["h", "r", "y"]:
                        ltr += PASANGAN[hrf[0]]
                        ltr += SANDHANGAN["cakra"]
                    else:
                        ltr += HURUF[hrf[0]]
                        ltr += SANDHANGAN["cakra"]
                else:
                    ltr += HURUF[hrf[0]]
                    ltr += SANDHANGAN["cakra"]
            else:
                ltr += HURUF[hrf[0]]
                ltr += SANDHANGAN["cakra"]
    if hrf.find("u") == (len(hrf) - 1):
        ltr += SANDHANGAN["suku"]

    if "é" in hrf or "è" in hrf:
        if prv:
            ltr += SANDHANGAN["taling"]
        else:
            ltr += SANDHANGAN["taling"]
    if hrf.find("e") == (len(hrf) - 1):
        if not iskeret:
            ltr += SANDHANGAN["pepet"]
    if hrf.find("i") == (len(hrf) - 1):
        ltr += SANDHANGAN["wulu"]
    if "o" in hrf:
        ltr += SANDHANGAN["taling-tarung"]
    if nxt == ".":
        ltr += HURUF[nxt]
    return ltr


def translate(word):
    ltr = []
    start = 0
    consonant = ["c", "k", "s", "w", "l", "p", "j", "m", "b"]
    specials = ["t", "d"]
    dobel = ["th", "dh", "ny", "ng"]
    insrt = ["h", "y", "g", "n"]
    vowels = "AaEeÈèÉéIiOoUuÊêĚěĔĕṚṛXxôâāīūō"
    for dob in dobel:
        if word.find(dob) == 0:
            if len(word) >= 3:
                if word[2] in vowels:
                    ltr.append(dob + word[2])
                    start = 3
            elif len(word) >= 4:
                if word[2] == "r":
                    if word[3] in vowels:
                        ltr.append(dob + "r" + word[3])
                        start = 4
    for ins in insrt:
        if word.find(ins) == 0:
            if len(word) >= 2:
                if word[1] in vowels:
                    ltr.append(ins + word[1])
                    start = 2
                elif word[1] in ["l", "r", "y"]:
                    if word[2] in vowels:
                        ltr.append(ins + word[1] + word[2])
                        start = 3
    if word[0] in vowels:
        ltr.append("h" + word[0])
        start = 1
    for i in range(start, len(word)):
        if word[i] in consonant:
            try:
                if len(word[i:]) > 1:
                    if word[i + 1] in vowels and word[i] != "l":
                        ltr.append(word[i] + word[i + 1])
                        i = i + 2
                    else:
                        if word[i + 1] in ["l", "r", "y"]:
                            if len(word[i:]) > 2:
                                if word[i + 2] in vowels:
                                    ltr.append(word[i] + word[i + 1] + word[i + 2])
                                    i = i + 3
                                else:
                                    ltr.append(word[i] + word[i + 1])
                                    i = i + 2
                            else:
                                if (i - 2) >= 0:
                                    if len(word[i:]) > 1:
                                        if word[i] not in word[i - 2] + word[i - 1]:
                                            ltr.append(word[i] + word[i + 1])
                                            i = i + 2
                        else:
                            if word[i] != "l":
                                ltr.append(word[i])
                                i = i + 1
                            else:
                                if len(word[i:]) > 1:
                                    if word[i + 1] in vowels:
                                        if len(ltr) > 0:
                                            if (
                                                not word[i] + word[i + 1]
                                                in ltr[len(ltr) - 1]
                                            ):
                                                ltr.append(word[i] + word[i + 1])
                                                i = i + 2
                                        else:
                                            ltr.append(word[i] + word[i + 1])
                                            i = i + 2
                else:
                    ltr.append(word[i])
                    i = i + 1
            except:
                ltr.append(word[i])
                i = i + 1
        elif word[i] in specials:
            try:
                if len(word[i:]) >= 2:
                    if word[i + 1] == "h" and word[i + 2] in vowels:
                        ltr.append(word[i] + word[i + 1] + word[i + 2])
                        i = i + 3
                    elif word[i + 1] in ["l", "r"]:
                        if len(word[i:]) > 2:
                            if word[i + 2] in vowels:
                                ltr.append(word[i] + word[i + 1] + word[i + 2])
                                i = i + 3
                            else:
                                ltr.append(word[i] + word[i + 1])
                                i = i + 2
                        else:
                            ltr.append(word[i] + word[i + 1])
                            i = i + 2
                    elif word[i + 1] in vowels:
                        ltr.append(word[i] + word[i + 1])
                        i = i + 2
                elif len(word[i:]) == 1:
                    if word[i + 1] == "h":
                        ltr.append(word[i] + word[i + 1])
                        i = i + 2
                    elif word[i + 1] in vowels:
                        ltr.append(word[i] + word[i + 1])
                        i = i + 2
            except:
                ltr.append(word[i])
                i = i + 1
        elif word[i] == "n":
            if len(word[i:]) > 2:
                if word[i + 1] in ["g", "y"] and word[i + 2] in vowels:
                    ltr.append(word[i] + word[i + 1] + word[i + 2])
                    i = i + 3
                elif word[i + 1] in ["g", "y"] and word[i + 2] not in vowels:
                    ltr.append(word[i] + word[i + 1])
                    i = i + 2
                else:
                    if word[i + 1] in vowels:
                        ltr.append(word[i] + word[i + 1])
                        i = i + 2
                    else:
                        ltr.append(word[i])
                        i = i + 1
            else:
                try:
                    nxt = word[i + 1]
                except:
                    nxt = None
                if nxt:
                    if nxt in vowels:
                        ltr.append(word[i] + nxt)
                        i = i + 2
                    elif nxt == "g":
                        ltr.append(word[i] + nxt)
                        i = i + 2
                    else:
                        ltr.append(word[i])
                        i = i + 1
                else:
                    ltr.append(word[i])
                    i = i + 1
        elif word[i] in ["r", "y"]:
            if i == 0:
                if len(word[i:]) > 1:
                    if word[i + 1] in vowels:
                        ltr.append(word[i] + word[i + 1])
                        i = i + 2
            else:
                if len(word[i:]) > 1:
                    if word[i + 1] in vowels:
                        if word[i - 1] not in vowels:
                            if (i - 2) >= 0:
                                if (word[i - 2] + word[i - 1]) in dobel:
                                    ltr.append(
                                        word[i - 2]
                                        + word[i - 1]
                                        + word[i]
                                        + word[i + 1]
                                    )
                                    i = i + 2
                                else:
                                    if not (word[i] + word[i + 1]) in ltr[len(ltr) - 1]:
                                        ltr[len(ltr) - 1] = (
                                            ltr[len(ltr) - 1] + word[i] + word[i + 1]
                                        )
                                        i = i + 1
                        else:
                            ltr.append(word[i] + word[i + 1])
                            i = i + 2
                    else:
                        ltr.append(word[i])
                        i = i + 1
                else:
                    ltr.append(word[i])
                    i = i + 1
        elif word[i] == "g":
            if "g" in ltr[len(ltr) - 1] and len(ltr[len(ltr) - 1]) >= 2:
                pass
            else:
                if len(word[i:]) > 1:
                    if word[i + 1] in vowels:
                        ltr.append(word[i] + word[i + 1])
                        i = i + 2
                    else:
                        if (i - 2) > 0:
                            if (word[i - 2] + word[i - 1]) == "ng":
                                pass
                        else:
                            if ltr[len(ltr) - 1] != "ng":
                                ltr.append(word[i])
                                i = i + 1
                            else:
                                i = i + 1
                else:
                    if (i - 2) > 0:
                        if (word[i - 2] + word[i - 1]) == "ng":
                            pass
                        elif (word[i - 1] + word[i]) == "ng":
                            pass
                        else:
                            ltr.append(word[i])
                            i = i + 1
                    else:
                        ltr.append(word[i])
                        i = i + 1
        elif word[i] == "h":
            if "h" in ltr[len(ltr) - 1] and len(ltr[len(ltr) - 1]) > 2:
                pass
            else:
                if len(word[i:]) > 1:
                    if word[i + 1] in vowels:
                        ltr.append(word[i] + word[i + 1])
                        i = i + 2
                    else:
                        ltr.append(word[i])
                        i = i + 1
                else:
                    ltr.append(word[i])
                    i = i + 1
    return ltr


def translatethis(text):
    if "," in text:
        trslt = translate(text.replace(",", "")) + [","]
    elif "." in text:
        trslt = translate(text.replace(",", "")) + ["."]
    else:
        trslt = translate(text)
    return trslt


def dotranslate(word):
    trslt = []
    for wrds in word.split():
        if "-" in wrds:
            for wrd in wrds.split("-"):
                trslt = trslt + translatethis(wrd.lower())
        else:
            trslt = trslt + translatethis(wrds.lower())

    return trslt


def dotransliterate(word):
    litr = ""
    if "." in word:
        for ijk, wrd in enumerate(word.split(".")):
            if "," in wrd:
                for idx, wr in enumerate(wrd.split(",")):
                    ltr = dotranslate(wr)
                    isend = False
                    for index, lt in enumerate(ltr):
                        if index == len(ltr) - 1:
                            isend = True
                            nxt = None
                        else:
                            nxt = ltr[index + 1]
                        if (index - 1) >= 0:
                            prv = ltr[index - 1]
                        else:
                            prv = None

                        litr += transliterate(lt, isend, prv, nxt)
                    if idx < (len(wrd.split(",")) - 1):
                        litr += HURUF[","]
            else:
                ltr = dotranslate(wrd)
                isend = False
                for index, lt in enumerate(ltr):
                    if index == len(ltr) - 1:
                        isend = True
                        nxt = None
                    else:
                        nxt = ltr[index + 1]
                    if (index - 1) >= 0:
                        prv = ltr[index - 1]
                    else:
                        prv = None

                    litr += transliterate(lt, isend, prv, nxt)
            if ijk < (len(word.split(".")) - 1):
                litr += HURUF["."]
    else:
        ltr = dotranslate(word)
        isend = False
        for index, lt in enumerate(ltr):
            if index == len(ltr) - 1:
                isend = True
                nxt = None
            else:
                nxt = ltr[index + 1]
            if (index - 1) >= 0:
                prv = ltr[index - 1]
            else:
                prv = None

            litr += transliterate(lt, isend, prv, nxt)
    print(ltr)
    return litr


if __name__ == "__main__":
    print("Menu:")
    print("1. Aksara Jawa")
    print("2. Polinomial")
    print("3. Jenis Segtiga")
    choice = input("Masukkan pilihan Anda: ")

    if choice == "1":
        question = input("> ")
        while question != "quit":
            try:
                print(dotransliterate(question).lower())
                question = input("> ")
            except:
                sys.exit(1)
    elif choice == "2":
        polinomial()
    elif choice == "3":
        a = int(input("Masukan bilangan a"))
        b = int(input("Masukan bilangan b"))
        c = int(input("Masukan bilangan c"))
        d = math.sqrt(a**2 + b**2)

        if a == b == c:
            print("merupakan segitiga sama sisi")
        elif a == b != c:
            print("merupakan segitiga sama kaki")
        elif a != b != c == int(d):
            print("merupakan segitiga sembarangan")
        else:
            print("bukan segitiga")
    elif choice == "4":

        print("ordo axb")
        input_a = int(input("masukan  matriks ordo a: "))
        input_b = int(input("masukan 1 matriks ordo b: "))
        input_a2 = int(input("masukan  matriks ordo a: "))
        input_b2 = int(input("masukan 1 matriks ordo b: "))

        matriks_a_2 = []
        for i in range(input_a2):
            baris_a_2 = []
            for j in range(input_b2):
                elemen_a = int(input(f"masukan elemen a[{i+1}][{j+1}]: "))
                baris_a_2.append(elemen_a)
            matriks_a_2.append(baris_a_2)

        matriks_b_2 = []
        for i in range(input_a2):
            baris_b_2 = []
            for j in range(input_b2):
                elemen_b = int(input(f"masukan elemen b[{i+1}][{j+1}]: "))
                baris_b_2.append(elemen_b)
            matriks_b_2.append(baris_b_2)

        print("\nMatriks 2 a:")
        for baris_a_2 in matriks_a_2:
            print(baris_a_2)

        print("\nMatriks 2 b:")
        for baris_b_2 in matriks_b_2:
            print(baris_b_2)

        matriks_a = []
        for i in range(input_a):
            baris_a = []
            for j in range(input_b):
                elemen_a = int(input(f"masukan elemen a[{i+1}][{j+1}]: "))
                baris_a.append(elemen_a)
            matriks_a.append(baris_a)

        matriks_b = []
        for i in range(input_a):
            baris_b = []
            for j in range(input_b):
                elemen_b = int(input(f"masukan elemen b[{i+1}][{j+1}]: "))
                baris_b.append(elemen_b)
            matriks_b.append(baris_b)

        print("\nMatriks 1 a:")
        for baris_a in matriks_a:
            print(baris_a)

        print("\nMatriks 1 b:")
        for baris_b in matriks_b:
            print(baris_b)

        arr = np.array(matriks_a)
        arr2 = np.array(matriks_b)
        sumi = np.add(arr, arr2)
        print("\nPenjumlahan:")
        print(sumi)

        subtra = np.subtract(arr, arr2)
        print("\nPengurangan:")
        print(subtra)

        multi = np.multiply(arr, arr2)
        print("\nPerkalian:")
        print(multi)

        trans = np.transpose(arr)
        print("\nTranspose matriks 1 a:")
        print(trans)

        trans2 = np.transpose(arr2)
        print("\nTranspose matriks 1 b:")
        print(trans2)

        div = np.divide(arr2, arr)
        print("Pembagian matriks 1 a: ")
        print(div)

    else:
        print("Pilihan tidak valid")
