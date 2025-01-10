#导入模块和自定函数
import os
import sys
import time
import random
import msvcrt

def num(s): 
    try:
        int(s)
        return int(s)
    except ValueError:
        pass 

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

#开场和选择界面

print('='*20,'欢迎来到游戏《唐僧大战白骨精》','='*20)
time.sleep(0.5)
print('请选择你的身份:')
print('\t 1.唐僧')
print('\t 2.白骨精')
print('')

#输入和判断
inPut =  input('请选择(1-2):')
if inPut == '1':
    print('你已经选择唐僧，恭喜你将以唐僧的身份进行游戏！')
elif inPut == '2':
    print('什么你竟然选择了白骨精？太不要脸了，系统将自动分配你以唐僧的身份进行游戏!')
else:
    print('你输入的选项有误，系统自动分配你以唐僧的身份进行游戏！')
print('')

#列表和字典
dict1 = {1:'你摔倒了，你死了',        
         2:'佛祖都看不下去，一掌拍死你',
         3:'一把七星剑从天上掉了下来，你被砍死了',
         4:'太上老君看你跑的累，奖励你个蝙蝠，你染上了新冠病毒，你病死了',
         5:'你路过了一家苹果手机店，你买了一部iPhone14ProMax,但他不配充电线，你很生气，你气死了'}

list1 = ['百岁老人给了你一把桃木剑,据说一刀999',
         '你捡到了一个法杖，到底怎么用呢？',
         '一把七星剑从天上掉了下来，但你不知为何接住了',
         '经历七七 八十九天的苦练后，你得到了周星驰的真传《如来神掌》！',
         '火星人当失路，你把他带回家后他为了报答你给了你一个sb金属，据说防御99+']

list2 = ['去死吧',
         '送你个新冠病毒，能不能活下去就看你了',
         '哈哈哈哈哈哈哈哈哈哈哈哈，有肉吃了']
#武器数据
list3 = [999,50,50,50,9999]

have  = []

#预设变量
health_time = 3     #复活次数
health = 2          #生命值
attack = 0          #攻击力
level  = 1          #防御力
arm_num= 1          #我的武器的号码
isDie  = False      #是否死亡
boss_time = 0               #打boss次数

#第二次输入
while health_time >= 0:
    train  = False  #是否练秘级
    boss   = False  #是否打BOSS
    die    = False  #是否死亡
    if isDie == True:
        isDie = False
        print('='*80)
        print('神仙路过看你可怜，你复活了')
        print('')

    print(f'你的身份是-->唐僧<--，你的攻击力是:{attack}  你的生命值是:{health}  防御力是:{level}  复活次数:{health_time}')
    print('')
    print('请选择你要做的操作:')
    print('\t 1.练秘级')
    print('\t 2.打BOSS')
    print('\t 3.逃跑')
    print('\t 4.退出游戏')
    print('')
    inPut = input('请选择(1-3):')
    result = is_number(inPut)

#判断输入
    if inPut == '1':
        train = True
    elif inPut == '2':
        boss = True
    elif inPut == '3':
        isDie = True
        health_time -= 1
        print('什么？逃跑？',dict1[random.randint(1,5)])
        if health_time > 0:
            print('任意键继续...')
            msvcrt.getch()
            continue
    elif inPut == '4':
        sys.exit('byebye')
    else:
        die = True

#处理非法数据
    if die:
        health_time -= 1
        isDie = True
        print(f'让我们看看操作{inPut}是什么，哦，是自杀，你死了')
        if health_time > 0:
            print('任意键继续...')
            msvcrt.getch()
            continue

#练秘级
    repeat = False  #武器重复
    if train:
        
#判断神力是否太多
        all_finish = False
        if len(have) == 5:
            health_time -= 1
            isDie = True
            all_finish = True
            print('')
            print('都叫你别吃太饱，你看，神力太多撑死了吧')
            print('')
            if health_time > 0:
                print('任意键继续...')
                msvcrt.getch()
                continue
#开始练级
        rand_num = random.randint(0,4)          #随几抽取道具号码
        rand = list1[rand_num]                  #获得道具
        for j in have:                          #遍历列表是否重复
            if rand in have:
                repeat = True
                break
        else:
            have.append(rand)
        if repeat == True:
            if all_finish == False:
                print('='*80)
                print('')
                if len(have) >= 3:
                    print(f'\t\t 练级失败,但有古文记载‘人不可以吃太饱’')
                else:
                    print(f'\t\t 练级失败,再接再厉')
                print('')
                print('='*80)
        else:
            if rand_num >= 0 and rand_num <= 3:
                if rand_num == 0:
                    attack += 999
                else:
                    attack += 50
            else:
                level += 9999
            health += random.randint(100,350)
            print('='*80)
            print('')
            if rand_num == 1:
                print(f'\t\t 练级成功！{have[arm_num-1]}《!ejf2?》')
            else:
                print(f'\t\t 练级成功！{have[arm_num-1]}')
            print('')
            print('='*80)
            arm_num += 1

#打Boss
    boss_life   = 5000            #boss生命值
    boss_attack = 150             #boss攻击力
    again       = True
    dura        = 100             
    if boss:
        print('='*80)
        print('')
        print('\t\t 你即将与终级大boss战斗')
        print(f'\t你的攻击力是:{attack}  你的生命值是:{health}  防御力是:{level}  复活次数:{health_time}')
        print('')
        print('='*80)
        print('')
        time.sleep(1.5)
#台词
        if boss_time == 0:
            print('白骨精：哈哈哈，小小唐僧就像想打败我')
        else:
            print('白骨精：想不到你还敢回来？')
        time.sleep(1.5)
        print(f'白骨精：{list2[random.randint(0,2)]}')       #抽出随即台词
#当重新来
        while again == True:
            arm_len = len(have)                             #提取道具号码
            time.sleep(1.5)
            print('='*80)
            print('')
            print(f'\t你的攻击力是:{attack}  你的生命值是:{health}  防御力是:{level}  复活次数:{health_time}')
            print(f'\t白骨精的攻击力是:{boss_attack}  白骨精的生命值是:{boss_life}')
            print('')
            print('='*80)
            time.sleep(1.5)
            print('[系统]：对方使用了 *** 技能')
            time.sleep(1.5)
            if arm_len > 0:
                print('[系统](输入你要使出的技能):')
                print('')
#遍历拥有的道具列表
                for k in range(arm_len):                    
                    print(f'\t {k+1}.{have[k]}')
                    time.sleep(0.5)
                print(f'\t {k+2}.退出')
                time.sleep(1.5)
#输入和判断是否数字
                inPut = input('[你]:')
                time.sleep(1.5)
                print('')
                result = is_number(inPut)
                if result == True:
                    if num(inPut) == True:                  
                        inPut = int(inPut)
                    else:
                        inPut = int('%d'%float(inPut))
#如果正确输入           
                    if inPut >= 1 and inPut <= arm_len+1:
                        if inPut == k + 2:                  ##退出
                            again = False
                            boss_time += 1
                            break

                        if have[inPut-1] == list1[4] and dura > 0:
                            dura -= 50
                            boss_life -= attack
                            print(f'[系统]：你选择了‘{have[inPut-1]}’')
                            time.sleep(1.5)
                            print('')
                            print(f'[系统]：你使用了sb金属，耐久度剩下{dura}%')
                            time.sleep(1.5)
                            if dura == 0:
                                print('sb金属已损坏')
                                time.sleep(1.5)
                                print('')
                                del have[inPut-1]
                            print('白骨精：可恶')
                            time.sleep(1.5)

                        elif have[inPut-1] in list1[2:4]:
                            boss_life -= attack
                            health    -= boss_attack
                            print(f'[系统]：你选择了‘{have[inPut-1]}’')
                            time.sleep(1.5)
                            print('白骨精：就这？哈哈哈')
                            time.sleep(1.5)
                            print(list2[random.randint(0,1)])

                        elif have[inPut-1] == list1[0]:
                            boss_life -= 999
                            health    -= boss_attack
                            print(f'[系统]：你选择了‘{have[inPut-1]}’')
                            time.sleep(1.5)
                            print('白骨精：啊啊啊啊啊啊')
                            time.sleep(1.5)
                            print('白骨精：什么？桃木剑？！？')
                            time.sleep(1.5)
                            print(f'不管了{list2[0]}!!!')
                            time.sleep(1.5)
                            attack -= 999
                            del have[inPut-1]

                        else:
                            newInput = input('')
                            health -= boss_attack
                            if newInput == '!ejf2?':
                                boss_life -= 3000
                                print(f'[系统]：你选择了‘{have[inPut-1]}’')
                                time.sleep(1.5)
                                print('白骨精：什么？？？啊啊啊啊啊啊啊！！！')
                                time.sleep(1.5)
                                del have[inPut-1]
                            else:
                                print('白骨精：给你法杖你也不会用啊，哈哈哈哈哈哈哈哈哈哈哈')
                                time.sleep(1.5)
                                print(list2[0])

                        boss_time += 1

                        if boss_life < 0:
                            print('白骨精：等等，这是什么？啊啊啊啊啊啊啊啊')
                            print('为什么？？？啊啊啊啊')
                            print('/\/\/\/\^----------嘟嘟嘟---')
                            print('[系统]：你已成功打败白骨精，恭喜')
                            ###
                            break
                        elif health < 0:
                            health_time -= 1
                            isDie = True
                            if health_time > 0:
                                print('任意键继续...')
                                msvcrt.getch()
                                break
#处理非法数据           
                    else:
                        again = True
                        print('[系统]：你自己看看你输入了什么？')
                        continue
                else:
                    again = True
                    
                    print('[系统]：你自己看看你输入了什么？')
                    continue
#没有道具
            else:
                again = False
                isDie = True
                health_time -= 1
                print('[系统]：你没技能可选')
                time.sleep(1.5)
                print('[系统]：你的生命 -999')
                time.sleep(1.5)
                print('你死了')
                time.sleep(1.5)
                print('')
                break
        else:
            boss_time += 1
            time.sleep(1.5)
            print('')
            continue

#游戏结束(死了)
else:
    print('你死了')
    os.system('pause')