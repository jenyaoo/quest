def printq(a):
    q=itertools.cycle(str(a))
    for i in range(len(str(a))):
        time.sleep(0.01)
        print(next(q),end='',flush=True)


def printw(a):
    q=itertools.cycle(str(a))
    for i in range(len(str(a))):
        time.sleep(0.01)
        print(next(q),end='',flush=True)
    print('')


def dialog1(a):
    for i in range(len(a)):
        printq(i+1)
        printq(')')
        printw(a[i])
    b=input()
    while True:
        if not(b.isdigit()):
            printw("Введите число из правильного диапазона")
            b=input()
        elif int(b)<=0 or int(b)>len(a):
            printw("Введите число из правильного диапазона")
            b=input()
        else:
            return int(b)


def fight(klass,ourh,ourstr):
    global vstr,vh,DiaWithEnemy,MyClass,out
    enem=randint(0,4)
    if out==1:
        enem=5
        out=0
    elif out==2:
        enem=6
        out=0
    eh=EnemyHealth[enem]
    estr=EnemyStrong[enem]
    printq('Вы встретили ')
    printw(NameOfEnemy[enem])
    while (ourh>0 and eh>0):
        ourj=dialog1(DiaWithEnemy)
        ej=randint(1,len(DiaWithEnemy))
        ourdam=0 
        edam=0   
        if ourj==2:
            edam+=ourstr
        elif ourj ==3:
            edam+=2*ourstr
        if ej==2:
            ourdam+=estr
        elif ej ==3:
            ourdam+=2*estr
        if ourj==1 and ej==2:
            ourdam//=3
        elif ourj==1 and ej==3:
            ourdam=0
        if ej==1 and ourj==2:
            edam//=3
        elif ej==1 and ourj==3:
            edam=0
        mage=randint(1,100)
        if ourj!=1 and mage<10 and MyClass==0:
            edam=eh
            printw("Смертельное заклинание!")
        if MyClass==1:
            ourdam=ourdam-min(3,ourdam)
        eh-=edam
        ourh-=ourdam
        printq('Вы нанесли врагу ')
        printq(edam)
        if eh<=0:
            printw(" Вы победили врага")
        else:
            printq(' У врага осталось ')
            printq(eh)
            printw(' здоровья')
        printq('Враг нанес вам ')
        printq(ourdam)
        if ourh<=0:
            printw(' Вы умерли')
        else:
            printq(' У вас осталось ')
            printq(ourh)
            printw(' здоровья') 
    return ourh


def dialog2(a):
    global out
    for i in range(len(a)):
        print(i+1,') ',a[i][0],sep='')
    b=input()
    while True:
        if not(b.isdigit()):
            printw("Введите число из правильного диапазона")
            b=input()
        elif int(b)<=0 or int(b)>len(a):
            printw("Введите число из правильного диапазона")
            b=input()
        else:
            break
    printq('Маг: ')
    printw(a[b-1][2])
    if a[b-1][1]==[1]:
        out=1
        return 1
    elif a[b-1][1]==[2]:
        out=2
        return 2
    elif a[b-1][1]==[3]:
        out=3
        return 3
    return dialog2(a[b-1][1])
    

from random import randint
import sys
import time
import itertools
restart=['Да','Нет']
printw('Приветствуем в игре ABOBA. Начать игру?')
start=dialog1(restart)
if start==2:
    sys.exit(0)
while True:
    EnemyStrong=[10,10,10,10,10,20,15]
    EnemyHealth=[100,100,100,100,100,200,250]
    OurStrong=[30,30,45]
    out=0
    OurHealth=[550,650,600]
    MageStrong=20
    MageHealth=200
    NameOfEnemy=['Скелета','Зомби','Вампира','Гоблина','Мимика','Мага','ГЛАВНОГО БОССА']
    DiaWithEnemy=['Уклонение','Атака','Крит атака']
    fi=[1]
    witha=[2]
    withouta=[3]
    klass=["Маг-с шансом в 10% уничтожает врага на месте","Воин-получает на 3 урона меньше","Ассасин-наносит на 10 урона больше"]
    asd=[0]*6
    z1=['Слабая твоя некромантия, даже любой новичок справится!',fi,'Ты заплатишь за свои слова!!! \nМаг нападает на тебя']
    z2=['...',asd[0],'Немой что-ли?!']
    z3=['...',asd[1],'Если ничего не ответишь, я тебя убью!!!']
    z4=['Да, я немой',asd[2],'Ого!']
    z5=['Вот такой фокус!',asd[3],'Смешной ты']
    z6=['Извини за мертвецов, не нарочно',asd[4],'Ну ничего, новых сделаю. Ну раз ты извинился, хочешь загадку? Если угадаешь, получишь приз']
    z7=['Да',asd[5],'Угадай мой любимый овощь!']
    z8=['Нет',withouta,'Тогда проваливай']
    z9=['Лук!',withouta,'Не угадал. Проваливай!']
    z10=['Огурец!',withouta,'Не угадал. Проваливай!']
    z11=['Помидор!',witha,'Вау! Держи артефакт! Не знаю что он делает, но тебе он точно поможет']
    z12=['...',fi,'Надоел!!! \nМаг нападает на тебя']
    x1=[z1,z2,z6]
    x2=[z3,z4]
    x3=[z12,z4]
    x4=[z5,z1]
    x5=[z1,z6]
    x6=[z7,z8]
    x7=[z9,z10,z11]
    z2[1]=x2
    z3[1]=x3
    z4[1]=x4
    z5[1]=x5
    z6[1]=x6
    z7[1]=x7
    artefact=0
    printw("Вы отправились в подземелье за древним артефактом")
    printw("Выберете класс персонажа")
    MyClass=dialog1(klass)-1
    for  i in range(20):
        time.sleep(1)
        print('-'*50,'ДЕНЬ ',i+1,'-'*50,sep='')
        p=0
        if i==9:
            printw("Вы встретили мага. Он говорит: 'Зачем ты моих мертвецов убиваешь!? Я тут вообще-то некромантией пытаюся заниматься!!!' ")
            dialog2(x1)
            if out==1:
                fight(MyClass,OurHealth[MyClass],OurStrong[MyClass])
                out=0
            elif out==2:
                artefact=1
                printw('Вы получили древний артефакт!!!')
                out=0
        elif i==19:
            printw('Вы заходите в большой зал и встречаете ГЛАВНОГО БОССА ИГРЫ!!!(!)')
            out=2
            fight(MyClass,OurHealth[MyClass],OurStrong[MyClass])
            if OurHealth[MyClass]<=0:
                printw("Конец. Хотите начать сначала?")
                re=dialog1(restart)
                if re==2:
                    sys.exit(0)
                else:
                    break
            elif artefact==0:
                printw('Вы выходите из зала, но вдруг слышите хруст над головой')
                printw('НА ВАС ПАДАЕТ ОГРОМНЫЙ КАМЕНЬ!!!')
                printw('Вот незадача. Вы умерли...')
                printw("Конец. Хотите начать сначала?")
                OurHealth[MyClass]=-1
                re=dialog1(restart)
                if re==2:
                    sys.exit(0)
                else:
                    break
            else:
                printw('Вы выходите из зала, но вдруг слышите хруст над головой')
                printw('НА ВАС ПАДАЕТ ОГРОМНЫЙ КАМЕНЬ!!!')
                printw('Но...')
                printw('Вы получаете божественный щит, который появляется из артефакта мага и камень отскакивает от вас')
                printw('Вы dидите свет сокровищь в глубине пещеры...')
                printw('Вы нашли их! Поздровляем! Вы выйграли!!!')
                print()
                print()
                printw("Конец. Хотите начать сначала?")
                OurHealth[MyClass]=-1
                re=dialog1(restart)
                if re==2:
                    sys.exit(0)
                else:
                    break
        else:
            if randint (1,100)<=10:
                printw("Вы сегодня никого не встретили. Вам повезло!")
                p=1
            if p!=1:
                OurHealth[MyClass]=fight(MyClass,OurHealth[MyClass],OurStrong[MyClass])
            if OurHealth[MyClass]<=0:
                printw("Конец. Хотите начать сначала?")
                re=dialog1(restart)
                if re==2:
                    sys.exit(0)
                else:
                    break
            print("У вас осталось",OurHealth[MyClass],"здоровья")
    if OurHealth[MyClass]>0:
        printw("Вы прошли игру. Конец. Хотите начать сначала?") 
        re=dialog1(restart)
        if re==2:
            sys.exit(0)
