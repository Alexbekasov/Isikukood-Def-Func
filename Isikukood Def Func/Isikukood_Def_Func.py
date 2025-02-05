def proverka_kontrolnoy_tsifry(kod):
   


# Первый коэффициент 
    case1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    # Второй коэффициент
    case2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    
    # Вычисляем контрольную сумму по первому набору весов
    summa1 = sum(int(kod[i]) * case1[i] for i in range(10))
    check1 = summa1 % 11
    if check1 != 10:
        return check1  # Если остаток не 10, возвращаем его. Сумма делится на 11, и если остаток не 10, то он становится контрольным числом.
    
    # Vi4islaem kontrollnuju summu
    summa2 = sum(int(kod[i]) * case2[i] for i in range(10))
    check2 = summa2 % 11
    
    return check2 if check2 != 10 else 0  # Если остаток снова 10, возвращаем 0

def poluchit_bolnitsu(kod):
    """Определяем больницу по номерам в личном коде."""
    nomer = int(kod[7:10])
    if 1 <= nomer <= 10:
        return "Kuressaare Haigla"
    elif 11 <= nomer <= 19:
        return "Tartu Ülikooli Naistekliinik"
    elif 21 <= nomer <= 220:
        return "Ida-Tallinna Keskhaigla"
    elif 221 <= nomer <= 270:
        return "Ida-Viru Keskhaigla"
    elif 271 <= nomer <= 370:
        return "Maarjamõisa Kliinikum"
    elif 371 <= nomer <= 420:
        return "Narva Haigla"
    elif 421 <= nomer <= 470:
        return "Pärnu Haigla"
    elif 471 <= nomer <= 490:
        return "Pelgulinna Sünnitusмаja"
    elif 491 <= nomer <= 520:
        return "Järvamaa Haigla"
    elif 521 <= nomer <= 570:
        return "Rakvere, Tapa haigla"
    elif 571 <= nomer <= 600:
        return "Valga Haigla"
    elif 601 <= nomer <= 650:
        return "Viljandi Haigla"
    elif 651 <= nomer <= 700:
        return "Lõuna-Eesti Haigla"
    return "Ma kardan, et ma ei tea mis koht see on nüüd..."
def proverka_koda():
    """Основная функция проверки личного кода."""
    pravilnye_kody = []  # tut spisok pravilnih kodov
    nepravilnye_kody = []  # tut spisok ne pravilnih kodov stobi vi videli :)
    while True:
        kod = input("Введите ваш isikukood (или напишите 'stop' чтобы закончить вас мучать): ")
        if kod.lower() == 'stop': # tut kod stobi ostanovitj
            break  
        
        # Tut proverka na koli4estvo zifr i kak zapisanno
        if len(kod) != 11 or not kod.isdigit():
            print("Если ты не знал конечно, но личный КОД пишем цифрами! На этот раз прощаю")
            nepravilnye_kody.append(kod)
            continue
        
        # Pervaja cifra proveraetsja
        if kod[0] not in '123456':
            print("Первая цифра не правильная! Не пытайся меня обмануть :)")
            nepravilnye_kody.append(kod)
            continue
        
        # uznaem god rozdenija
        god_prefix = {'1': '18', '2': '18', '3': '19', '4': '19', '5': '20', '6': '20'}[kod[0]]
        data_rozhdeniya = f"{kod[5:7]}.{kod[3:5]}.{god_prefix}{kod[1:3]}"
        
        # Proveraem kontr. 4islo
        if proverka_kontrolnoy_tsifry(kod) != int(kod[-1]):
            print("Эхххх не правильная контрольная цифра......")
            nepravilnye_kody.append(kod)
            continue
        
        # Kto po polu
        pol = "Mees" if kod[0] in '135' else "Naine"
        
        # Gde rodilsja
        bolnitsa = poluchit_bolnitsu(kod)
        print(f"See on {pol}, sünnipäev on {data_rozhdeniya}, ja of course sünnikoht on: {bolnitsa}.")
        pravilnye_kody.append(kod)
    
    
    print("\nPravilnye kody:")
    for kod in sorted(pravilnye_kody, key=lambda x: (x[0] in '135', x)): # Мы сортируем список pravilnye_kody, в котором находятся правильные личные коды. key=lambda x: (x[0] in '135', x) – это специальная функция сортировки.
        print(kod)
    
    print("\nNepravilnye kody:")
    for kod in sorted(nepravilnye_kody):
        print(kod)

if __name__ == "__main__":
    proverka_koda()
