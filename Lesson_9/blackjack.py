import random
is_g = "y"
while is_g == "y":
    c = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    h_p = [random.choice(c)]
    h_c = [random.choice(c)]
    s_p = 0
    s_c = 0
    g_c = "y"

    while g_c == "y":
        h_p.append(random.choice(c))
        if sum(h_p) > 21 and 11 in h_p:
            for i in range(0,len(h_p)):
                if h_p[i] == 11:
                    h_p [i] = 1
                    break
        s_p = sum(h_p)
        
        print(f"Твоя рука: {h_p}. Очков {s_p}")
        print(f"Первая карта компутера: {h_c[0]}")
        if s_p > 21:
            g_c = "n"
        else:
            g_c = input("берём карты? y - да, n - нет:")


    while sum(h_c) < 17:
        h_c.append(random.choice(c))

        if sum(h_c) > 21 and 11 in h_c:
            for i in range(0, len(h_c)):
                if h_c[i] == 11:
                    h_c[i] = 1
                    break

    s_c  = sum(h_c)
    print("="*25)
    print(f"Твоя рука:{h_p}. Очков:{s_p}")
    print(f"Рука компьютера:{h_c}. Очков:{s_c}")


    if s_p > 21 and s_c >21:
        print("!!!Ничья!!!")
    elif s_c > 21:
        print("!!!Пабеда!!!")
    elif s_p > 21:
        print("!!!Проигрыш!!!")
    elif s_p == s_c:
        print("!!!Ничья!!!")
    elif s_p > s_c:
        print("!!!Пабеда!!!")
    elif s_p == 21:
        print("!!!Пабеда!!!")
    else:
        print("!!!Проигрыш!!!")


    is_g = input("продолжаем? y - да, n - нет")