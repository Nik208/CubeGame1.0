# Функции и т.д. (Короче всё для использования в коде игры)
import random
MaxEnemyHP = 10
MaxPlayerHP = 35
PlayerHP = MaxPlayerHP
kubecheck4 = False
kubecheck5 = False
Wunlock3 = False
Potion = 0
PotionDoubleCD = 24
UpperHand = 0
EnemyHP = MaxEnemyHP
Blindness = False
TotalUpperHand = 0
PlayerStats = [MaxPlayerHP, PlayerHP, EnemyHP, MaxEnemyHP, Blindness]
def Tutorial(EnemyHP, MaxEnemyHP, PlayerHP, MaxPlayerHP):
    TutorCheck = 0
    kTutorCheck = 0
    kTutorUse1 = False
    kTutorUse2 = False
    kTutorUse3 = False
    print("Битва!")
    print("(Добро пожаловать в Обучение! Начнём же с основ!)")
    input("Нажимте Enter чтобы продолжить")
    print()
    print("Значение кубиков:")
    print("кубик 1: 6")
    print("кубик 2: 5")
    print("кубик 3: 5")
    print()
    print("(Кубики, кубики. кубики.. Это ваш боевой потенциал! Чем больше значение тем больше урона вы нанесёте!.. или нет! Сейчас все объясню)")
    input("Нажимте Enter чтобы продолжить")
    print()
    print("Ваше снаряжение:")
    print()
    print("1. Меч (нанести X урона)")
    print("2. Боевой топор (нанести X*2 урона, максимум 4 на кубике)")
    print()
    print("(Ваше снаряжение - ваш главный путь к победе. Их урон напрямую зависит от значения кубика! Не бойтесь забыть что снаряжение делает, Описание всегжа будет рядом!)")
    print("Пока что вы можете использовать только ваш меч, чтобы его выбрать, напишите его номер! (1)")
    while True:
        try:
            print("Выберите снаряжение:")
            TutorCheck = int(input())
            if TutorCheck == 1:
                print("Выберите кубик")
                print()
                print("(Теперь выбери кубик, значение которого будет использовано для атаки! (1-3))")
                kTutorCheck = int(input())
                while True:
                    if kTutorCheck == 1:
                        print("6 Урона!")
                        EnemyHP -= 6
                        print("Здоровье противника:", EnemyHP, "/", MaxEnemyHP)
                        kTutorUse1 = True
                        break
                    elif kTutorCheck == 2:
                        print("5 Урона!")
                        EnemyHP -= 5
                        print("Здоровье противника:", EnemyHP, "/", MaxEnemyHP)
                        kTutorUse2 = True
                        break
                    elif kTutorCheck == 3:
                        print("5 Урона!")
                        EnemyHP -= 5
                        print("Здоровье противника:", EnemyHP, "/", MaxEnemyHP)
                        kTutorUse3 = True
                        break
                    else:
                        print("У тебя нет такого кубика.")
                break
            elif TutorCheck == 2:
                print("(Я же сказал выбрать Меч. У тебя нет кубиков для того чтобы использовать Топор, давай-ка ещё раз)")
            else:
                print("У тебя нет оружия с этим номером, давай по-новой.")
        except ValueError:
            print("(Ты что-то не то вписал, давай вообще по новой!)")
    print()
    print("(Отлично! Продолжим ход!)")
    input("Нажимте Enter чтобы продолжить")
    print("(Я тебе забыл сказать, Твое снаряжение и кубики, одноразовые! Используемое только раз за Ход! (Если только оно не особенное))")
    print("(Давай помогу, я подкину тебе кубик 4)")
    print()
    print("Значение кубиков:")
    if kTutorUse1 == False:
        print("кубик 1: 6")
    if kTutorUse2 == False:
        print("кубик 2: 5")
    if kTutorUse3 == False:
        print("кубик 3: 5")
    print("кубик 4: 3")
    input("Нажимте Enter чтобы продолжить")
    print()
    print("Ваше снаряжение:")
    print()
    print("2. Боевой топор (нанести X*2 урона, максимум 4 на кубике)")
    print()
    print("(Ну чтож, выбирай Топор!)")
    while True:
        try:
            print("Выберите снаряжение:")
            TutorCheck = int(input())
            if TutorCheck == 2:
                print("Выберите кубик")
                print()
                print("(Теперь выбери кубик, который я подкинул! не благодори)")
                while True:
                    kTutorCheck = int(input())
                    if kTutorCheck == 4:
                        print("6 Урона!")
                        EnemyHP = 0
                        print("Здоровье противника:", EnemyHP, "/", MaxEnemyHP)
                        break
                    elif kTutorCheck == 3 or kTutorCheck == 2 or kTutorCheck == 1:
                        print("Кубик больше 4 (Либо ты его использовал. Я уже забыл)")
                    else:
                        print("У тебя нет такого кубика.")
                break
            elif TutorCheck == 1:
                print("(ты его использовал! он Одноразовый!)")
            else:
                print("У тебя нет оружия с этим номером, давай по-новой.")
        except ValueError:
            print("(Ты что-то не то вписал, давай вообще по новой!)")
    print("Победа!")
    print()
    print("(Поздравляю! Вот и твоё время обучения закончилось. Теперь давай сам! Удачи! Тебе она понадобится..)")
def TurnCheck(Player):
    while True:
                print("Продолжить ход? (Да/Нет)")
                Tcheck = input().lower()
                if Tcheck == "да":
                    return True
                elif Tcheck == "нет":
                    print()
                    print("Ход окончен!")
                    input("Нажмите Enter чтобы продолжить")
                    return False
                else:
                    print("Невалидный ввод, попробуйте ещё раз")
def pTurn(EnemyHP, MaxEnemyHP, PlayerHP, MaxPlayerHP, Blindness):
        print("Ваш Ход!")
        print()
        Player = True
        UsageK1 = False
        UsageK2 = False
        UsageK3 = False
        UsageK4 = False
        UsageK5 = False
        Weapon1Usage = False
        Weapon2Usage = False
        k1 = random.randint(1,6)
        k2 = random.randint(1,6)
        k3 = random.randint(1,6)
        if kubecheck4 == True:
            k4 = random.randint(1,6)
        if kubecheck5 == True:
            k5 = random.randint(1,6)
        if Blindness == True:
            print("Вы ослеплены! Значения кубов неизвестно!")
            input("Нажмите Enter чтобы продолжить")
            print()
        while EnemyHP != 0 and Player == True:
            try:
                print("Ваше Здоровье:", PlayerHP, "/", MaxPlayerHP)
                if Blindness == True:
                    print("Значения кубиков:")
                    print()
                    if UsageK1 == False:
                        print("кубик 1: ???")
                    if UsageK2 == False:
                        print("кубик 2: ???")
                    if UsageK3 == False:
                        print("кубик 3: ???")
                    if kubecheck4 == True and UsageK4 == False:
                        print("кубик 4: ???")
                    if kubecheck5 == True and UsageK5 == False:
                        print("кубик 5: ???")
                else:
                    print("Значения кубиков:")
                    print()
                    if UsageK1 == False:
                        print("кубик 1:", k1)
                    if UsageK2 == False:
                        print("кубик 2:", k2)
                    if UsageK3 == False:
                        print("кубик 3:", k3)
                    if kubecheck4 == True and UsageK4 == False:
                        print("кубик 4:", k4)
                    if kubecheck5 == True and UsageK5 == False:
                        print("кубик 5:", k5)
                input("Нажмите Enter чтобы продолжить")
                print()
                print("Ваше снаряжение:")
                print()
                if Weapon1Usage == False:
                    print("1. Меч (нанести X урона)")
                if Weapon2Usage == False:
                    print("2. Боевой топор (нанести X*2 урона, максимум 4 на кубике)")
                if Wunlock3 == True:
                    print("3. Кинжал (Нанести 3 урона, многоразовое)")
                print()
                print("Ваш Ход.")
                print("Выберите номер снаряжение")
                Wcheck = int(input())
                if Wcheck == 1 and Weapon1Usage == False:  
                    print() 
                    print("Выберите номер кубика")
                    while True:
                        Kcheck = int(input())
                        if Kcheck == 1:
                            if UsageK1 == False:
                                EnemyHP -= k1
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print(k1, "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK1 = True
                                Weapon1Usage = True
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё раз")
                        elif Kcheck == 2:
                            if UsageK2 == False:
                                EnemyHP -= k2
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print(k2, "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK2 = True
                                Weapon1Usage = True
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё раз")
                        elif Kcheck == 3:
                            if UsageK3 == False:
                                EnemyHP -= k3
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print(k3, "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK3 = True
                                Weapon1Usage = True
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё раз")
                        elif Kcheck == 4 and kubecheck4 == True:
                            if UsageK4 == False:
                                EnemyHP -= k4
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print(k4, "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK4 = True
                                Weapon1Usage = True
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё раз")
                        elif Kcheck == 5 and kubecheck5 == True:
                            if UsageK5 == False:
                                EnemyHP -= k5
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print(k5, "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK5 = True
                                Weapon1Usage = True
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё раз")
                        else:
                            print("Такого кубика у вас нет!")
                            print("Выберите кубик ещё раз")
                elif Wcheck == 2 and Weapon2Usage == False:
                    print()
                    print("Выберите номер кубика")
                    while True:
                        Kcheck = int(input())
                        if Kcheck == 1:
                            if UsageK1 == False and k1 <= 4:
                                EnemyHP -= (k1*2)
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print((k1*2), "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK1 = True
                                Weapon2Usage = True
                                break
                            elif UsageK1 == False and k1 > 4:
                                print("Значение кубика больше 4x!")
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё раз")
                        elif Kcheck == 2 and UsageK2 <= 4:
                            if UsageK2 == False and k2 <= 4:
                                EnemyHP -= (k2*2)
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print((k2*2), "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK2 = True
                                Weapon2Usage = True
                                break
                            elif UsageK1 == False and k2 > 4:
                                print("Значение кубика больше 4x!")
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё раз")
                        elif Kcheck == 3:
                            if UsageK3 == False and k3 <= 4:
                                EnemyHP -= (k3*2)
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print((k3*2), "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK3 = True
                                Weapon2Usage = True
                                break
                            elif UsageK1 == False and k3 > 4:
                                print("Значение кубика больше 4x!")
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё раз")
                        elif Kcheck == 4 and kubecheck4 == True:
                            if UsageK4 == False and k4 <= 4:
                                EnemyHP -= (k4*2)
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print((k4*2), "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK4 = True
                                Weapon2Usage = True
                                break
                            elif UsageK1 == False and k4 > 4:
                                print("Значение кубика больше 4x!")
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё рах")
                        elif Kcheck == 5 and kubecheck5 == True:
                            if UsageK5 == False and k5 <= 4:
                                EnemyHP -= (k5*2)
                                if EnemyHP < 0:
                                    EnemyHP = 0
                                print((k5*2), "Урона!")
                                print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                                UsageK5 = True
                                Weapon2Usage = True
                                break
                            elif UsageK1 == False and k5 > 4:
                                print("Значение кубика больше 4x!")
                                break
                            else:
                                print("Кубик уже использован!")
                                print("Выберите кубик ещё рах")
                        else:
                            print("Такого кубика у вас нет!")
                            print("Выберите кубик ещё рах")
                elif Wcheck == 3 and Wunlock3 == True:
                    print()
                    print("Выберите номер кубика:")
                    while True:
                        Kcheck = int(input())
                        if Kcheck == 1:
                            EnemyHP -= 3
                            if EnemyHP < 0:
                                EnemyHP = 0
                            print("3 Урона!")
                            print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                            UsageK1 = True
                            break
                        if Kcheck == 2:
                            EnemyHP -= 3
                            if EnemyHP < 0:
                                EnemyHP = 0
                            print("3 Урона!")
                            print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                            UsageK2 = True
                            break
                        if Kcheck == 3:
                            EnemyHP -= 3
                            if EnemyHP < 0:
                                EnemyHP = 0
                            print("3 Урона!")
                            print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                            UsageK3 = True
                            break
                        if Kcheck == 4 and kubecheck4 == True:
                            EnemyHP -= 3
                            if EnemyHP < 0:
                                EnemyHP = 0
                            print("3 Урона!")
                            print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                            UsageK4 = True
                            break
                        if Kcheck == 5 and kubecheck5 == True:
                            EnemyHP -= 3
                            if EnemyHP < 0:
                                EnemyHP = 0
                            print("3 Урона!")
                            print("Здоровье врага: ", EnemyHP,"/",MaxEnemyHP)
                            UsageK5 = True
                            break
                else:
                    print("У вас такого нет, или не осталось!")
            except ValueError:
                print("Абсолютно некорректный ввод.. Перезапуск хода..")
            if (UsageK1 == True and UsageK2 == True and UsageK3 == True) or (Weapon1Usage == True and Weapon2Usage == True and Wunlock3 == False):
                if EnemyHP == 0:
                    print("Победа!")
                    return EnemyHP
                if kubecheck4 == True and UsageK4 == True:
                    if kubecheck5 == True and UsageK5 == False:
                        Player = TurnCheck(Player)
                        if Player == False:
                            return EnemyHP
                    else:
                        print("Ход окончен")
                        Player = False
                        return EnemyHP
                elif kubecheck4 == True and UsageK4 == False:
                    Player = TurnCheck(Player)
                    if Player == False:
                        return EnemyHP
                else:
                    print("Ход окончен")
                    Player = False
                    return EnemyHP
            elif EnemyHP == 0:
                print("Победа!")
                return EnemyHP
            else:
                Player = TurnCheck(Player)
                if Player == False:
                    return EnemyHP
def ERob_bo_botTurn(PlayerHP, MaxPlayerHP):
    Ek1 = random.randint(1,6)
    Ek2 = random.randint(1,6)
    Ek3 = random.randint(1,6)
    if Ek1 > 2:
        print("Робобот использует ЛазерГан!")
        PlayerHP -= 4
        print("4 Урона!")
        if PlayerHP < 0:
            PlayerHP = 0
        print("Ваше Здоровье:", PlayerHP, "/", MaxPlayerHP)
        input("Нажмите Enter чтобы продолжить")
    if PlayerHP != 0:
        if Ek2 > 2:
            print("Робобот использует ЛазерГан!")
            PlayerHP -= 4
            print("4 Урона!")
            if PlayerHP < 0:
                PlayerHP = 0
            print("Ваше Здоровье:", PlayerHP, "/", MaxPlayerHP)
            input("Нажмите Enter чтобы продолжить")
    else:
        print("Вы проиграли..")
    if PlayerHP != 0:
        if Ek3 > 2:
            print("Робобот использует ЛазерГан!")
            PlayerHP -= 4
            print("4 Урона!")
            if PlayerHP < 0:
                PlayerHP = 0
            print("Ваше Здоровье:", PlayerHP, "/", MaxPlayerHP)
            input("Нажмите Enter чтобы продолжить")
    else:
        print("Вы проиграли..")
    print("Ход окончен!")
    return PlayerHP
def ECursedPotTurn(Potion, PotionDoubleCD):
    if Potion != 0:
        Potion -= 1
    PotionInflict = 0
    PotionDouble = False
    Ek1 = random.randint(1,6)
    Ek2 = random.randint(1,6)
    Ek3 = random.randint(1,6)
    if (Ek1 < 4):
        print("Чаша использует Ядовитое облако!")
        Potion += Ek1
        print(Ek1, "Яда!")
        Ek1 = 0
        PotionInflict += 1
        input("Нажмите Enter чтобы продолжить")
    if (Ek2 < 4):
        print("Чаша использует Ядовитое облако!")
        Potion += Ek2
        print(Ek2, "Яда!")
        Ek2 = 0
        PotionInflict += 1
        input("Нажмите Enter чтобы продолжить")
    if (Ek3 < 4) and (PotionInflict < 2):
        print("Чаша использует Ядовитое облако!")
        Potion += Ek3
        print(Ek3, "Яда!")
        Ek3 = 0
        PotionInflict += 1
        input("Нажмите Enter чтобы продолжить")
    print("Чаша Заряжает Массивное отравление...")
    PotionDoubleCD -= (Ek1 + Ek2 + Ek3)
    if PotionDoubleCD <= 0:
        PotionDoubleCD = 24
        PotionDouble = True
    if PotionDouble == True:
        print("Чаша использует Массивное отравление!")
        print("Яд удвоен!")
        Potion *= 2
        input("Нажмите Enter чтобы продолжить")
    print("Ход окончен!")
    input("Нажмите Enter чтобы продолжить")
    return Potion
def EKrakenTurn(UpperHand, Ek1, Ek2, Ek3, Ek4):
    if (Ek1 % 2) != 0:
        UpperHand += 1
    if (Ek2 % 2) != 0:
        UpperHand += 1
    if (Ek3 % 2) != 0:
        UpperHand += 1
    if (Ek4 % 2) != 0:
        UpperHand += 1
    return UpperHand





# Новела (Активный код)
    
print("Добро пожаловать в подземелье случайностей! Готовы ли вы покорить непобедимое подземелье? А кто вас спашивал! Вы уже здесь и пути назад нет! Так что готовтесь и вперёд!")
print()
input("Нажимте Enter чтобы продолжить")
print("Стоп! А ты уверен что помнишь как оружем махать вообще? Весь такой серьёзный и уверенный, а погибнет на первом же слабачке. Хочешь попрактиковатся пока ещё можно?")
print()
print("(Необходимо ли вам обучение? (Да/Нет))")
TutorCheck = input().lower()
while True:
    if TutorCheck == "да":
        print()
        Tutorial(EnemyHP, MaxEnemyHP, PlayerHP, MaxPlayerHP)
        break
    elif TutorCheck == "нет":
        print("Как знаешь, Воин! Дальше ты сам, Удачи! Она тебе явно пригодится!")
        input("Нажимте Enter чтобы продолжить")
        break
    else:
        print("Неправильный ввод, попробуйте ещё раз!")
print()
print("Проходя сквозь темные коридоры, вы находите сокровище! Однако, в порыве спешки за сокровищем, вы замечаете робота, который его охраняет")
print("Ну, как вас и учили, если в подземелье вам не дают сокровище, надо его отнять! Вперёд в бой!")
MaxEnemyHP = 25
EnemyHP = 25
input("Нажимте Enter чтобы продолжить")
print("В бой!")
while EnemyHP != 0 and PlayerHP != 0:     # Робобот
    EnemyHP = pTurn(EnemyHP, MaxEnemyHP, PlayerHP, MaxPlayerHP, Blindness)
    if EnemyHP != 0:
        PlayerHP = ERob_bo_botTurn(PlayerHP, MaxPlayerHP)
if PlayerHP == 0:
    print("Похоже, поход в подземелья было не вашим призванием..")
    print("Игра окончена")
else:
    input("Нажмите Enter чтобы продолжить")
    print("Вы чуствуете себя сильнее! (Уровень 2!)")
    print("Вы получаете ещё 1 кубик! Макс. Здоровье увеличено на 10!")
    kubecheck4 = True
    MaxPlayerHP += 10
    PlayerHP = MaxPlayerHP
    input("Нажмите Enter чтобы продолжить")
    print()
    print("Преодолев робота, наконец можно насладится заслуженным сокровищем.. Вы открываете сундук")
    print("Вы нашли Кинжал! - Многоразовый слабый удар! (Добавлено в снаряжение)")
    Wunlock3 = True
    input("Нажмите Enter чтобы продолжить")
    print()
    print("Вы проходите несколько длинных корридоров, пустых. Вскоре вы видете ещё одну сокровищнецу! Но пока вы туда шли, Чаша Рядом с входом трясётся.. похоже это мимик!")
    MaxEnemyHP = 41
    EnemyHP = 41
    input("Нажмите Enter чтобы продолжить")
    print()
    print("В бой!")
    while EnemyHP != 0 and PlayerHP != 0:     # Чаша
        EnemyHP = pTurn(EnemyHP, MaxEnemyHP, PlayerHP, MaxPlayerHP, Blindness)
        if EnemyHP != 0:
            Potion = ECursedPotTurn(Potion, PotionDoubleCD)
        if Potion != 0:
                print("На вас наложено", Potion,  "Яда!")
                PlayerHP -= Potion
                print(Potion, "Урона!")
                if PlayerHP <= 0:
                    PlayerHP = 0
                if PlayerHP == 0:
                    print("Ваше Здоровье:", PlayerHP, "/", MaxPlayerHP)
                    print("Вы проиграли..")
                input("Нажмите Enter чтобы продолжить")
    if PlayerHP == 0:
        print("Похоже, поход в подземелья было не вашим призванием..")
        print("Игра окончена")
    else:
        input("Нажмите Enter чтобы продолжить")
        print()
        print("Новый уровень!")
        print("Вы получаете ещё 1 кубик!")
        kubecheck5 = True
        PlayerHP = MaxPlayerHP
        print()
        print("Наконец.. Спокойно можно посмотреть в сокровищницу.. а нет. Это была не настоящая сокровищница..")
        print("Вы проходите дольше комнат.. вы устали.. как то пусто для подземельяю.. И тут вы замечаете выход!юю За кракеном..")
        MaxEnemyHP = 70
        EnemyHP = 70
        input("Нажмите Enter чтобы продолжить")
        print("В бой!")
        while EnemyHP != 0 and PlayerHP != 0:     # Кракен
            EnemyHP = pTurn(EnemyHP, MaxEnemyHP, PlayerHP, MaxPlayerHP, Blindness)
            Blindness = False
            if EnemyHP != 0:
                Ek1 = random.randint(1,6)
                Ek2 = random.randint(1,6)
                Ek3 = random.randint(1,6)
                Ek4 = random.randint(1,6)
                if Ek1 == 4:
                    Ek1 = 0
                    Blindness = True
                    print("Кальмар использует Чернила!")
                    print("Вы ослеплены!")
                    input("Нажмите Enter чтобы продолжить")
                elif Ek2 == 4:
                    Ek1 = 0
                    Blindness = True
                    print("Кальмар использует Чернила!")
                    print("Вы ослеплены!")
                    input("Нажмите Enter чтобы продолжить")
                elif Ek3 == 4:
                    Ek1 = 0
                    Blindness = True
                    print("Кальмар использует Чернила!")
                    print("Вы ослеплены!")
                    input("Нажмите Enter чтобы продолжить")
                elif Ek4 == 4:
                    Ek1 = 0
                    Blindness = True
                    print("Кальмар использует Чернила!")
                    print("Вы ослеплены!")
                    input("Нажмите Enter чтобы продолжить")
                UpperHand = EKrakenTurn(UpperHand, Ek1, Ek2, Ek3, Ek4)
                while (TotalUpperHand < UpperHand):
                    print("Кальмар использует Преймущество!")
                    TotalUpperHand += 1
                    PlayerHP -= TotalUpperHand
                    print(TotalUpperHand, "Урона!")
                    if PlayerHP < 0:
                        PLayerHP = 0
                    if PlayerHP == 0:
                        print("Ваше Здоровье:", PlayerHP, "/", MaxPlayerHP)
                        print("Вы проиграли..")
                        break
                    input("Нажмите Enter чтобы продолжить")
                print("Ход окончен!")
                input("Нажмите Enter чтобы продолжить")
        if PlayerHP == 0:
            print("А ведь почти получилось!")
            print("Игра окончена")
        else:
            print("Вы стремитесь к выходу, но вместо земли, в видете только свет..")
            input("Нажмите Enter чтобы продолжить")
            print("Отсюда никто не сбегал по причине!.. Выхода нет.. Увиимся в новой петле хаоса!")
            print("Продолжение следует..")
    input("Нажмите Enter чтобы Закончить")