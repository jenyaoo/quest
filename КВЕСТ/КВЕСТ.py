def dialog1(a):
    for i in range(len(a)):
        print(i+1,') ',a[i],sep='')
    b=int(input())
    while b<=0 or b>len(a):
        print("Введите число из правильного диапазона")
        b=int(input())
    return b


def fight(klass,ourh,ourstr):
    global vstr,vh,DiaWithEnemy,MyClass
    enem=randint(0,4)
    eh=EnemyHealth[enem]
    estr=EnemyStrong[enem]
    print('Вы встретили',NameOfEnemy[enem])
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
            eh=0
            print("Смертельное заклинание!")
        if MyClass==1:
            ourdam=ourdam-min(3,ourdam)
        eh-=edam
        ourh-=ourdam
        print('Враг наносит вам',ourdam,end=' ')
        if eh<=0:
            print("Вы победили врага")
        else:
            print('У врага осталось',eh,'здоровья')
        print('Вы наносите врагу',edam,end=' ')
        if ourh<=0:
            print('Вы умерли')
        else:
            print('У вас осталось',ourh,'здоровья')
        
    return ourh


def dialog2(a):
    for i in range(len(a)):
        print(i+1,') ',a[i][0],sep='')
    b=int(input())
    while b<=0 or b>len(a):
        print("Введите число из правильного диапазона")
        b=int(input())
    print('Маг: ',a[b-1][2],sep='')
    if a[b-1][1]==[]:
        return b
    return dialog2(a[b-1][1])
    

from random import randint
import sys
import time
import itertools
restart=['Да','Нет']
print('Приветствуем в игре ABOBA. Начать игру?')
start=dialog1(restart)
if start==2:
    sys.exit(0)
while True:
    EnemyStrong=[10,10,10,10,10]
    EnemyHealth=[100,100,100,100,100]
    OurStrong=[20,20,300]
    OurHealth=[800,1200,1000]
    NameOfEnemy=['aboba']*5
    DiaWithEnemy=['Уклонение','Атака','Крит атака']
    zxc=[]
    x=[['Все хорошо',zxc,'Тогда пока'],['Все плохо',zxc,'Ничем не могу помочь']]
    c=[['Плохой день',zxc,'Тогда прощаю'],['Ты страшный',zxc,'Ну все. Защищайся!!!']]
    v=[[':)',zxc,'...'],[':(',zxc,'...']]
    diawithmage1=[['Привет',x,'Как дела?'],['Пока',c,"Че такой грубый"],['Защищайся',v,'?']]
    klass=["Маг-с шансом в 10% уничтожает врага на месте","Воин-получает на 3 урона меньше","Ассасин-наносит на 10 урона больше"]
    print("Вы отправились в подзелье за древним артефактом")
    print("Выберете класс персонажа")
    MyClass=dialog1(klass)-1
    for  i in range(20):
        time.sleep(1)
        print('-----------------------------------ДЕНЬ ',i+1,'-----------------------------------',sep='')
        p=0
        if i==9:
            print("Вы встретили мага. Он говорит: 'Привет' ")
            dialog2(diawithmage1)
        else:
            if randint (1,100)<=10:
                print("Вы сегодня никого не встретили. Вам повезло!")
                p=1
            if p!=1:
                OurHealth[MyClass]=fight(MyClass,OurHealth[MyClass],OurStrong[MyClass])
            if OurHealth[MyClass]<=0:
                print("Конец. Хотите начать сначала?")
                re=dialog1(restart)
                if re==2:
                    sys.exit(0)
                else:
                    break
            print("У вас осталось",OurHealth[MyClass],"здоровья")
    if OurHealth[MyClass]>0:
        print("Вы прошли игру. Конец. Хотите начать сначала?") 
        re=dialog1(restart)
        if re==2:
            sys.exit(0)
