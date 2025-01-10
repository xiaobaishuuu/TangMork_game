import random
from data import *

class TangMork:

    def __init__(self,health=2,attack=0,defense=1,reborn=3,boss_health=5000,boss_attack=350) -> None:
        self.health  =  health
        self.attack  =  attack
        self.defense =  defense
        self.reborn  =  reborn
        self.boss_health= boss_health
        self.boss_attack= boss_attack
        self.boss_time  = 0
        self.have_tools = []
        self.have_tools_durability = {}
        self.Ace = False

    def boss_death_detect(self):
        if self.boss_health <= 0:
            print('克拉希斯：真的，够了！')
            print('[系统]：克拉希斯释放了全部 凋零沌波 ')
            print('[我]：别！。。。啊。。咳咳。。咳咳咳。。。啊 啊 我。。的。。身。。体。。。。')
            print('克拉希斯：你是真难缠，比那家伙还难打。。啊嘶。真痛')
            print('克拉希斯：你怎么想打一位 “神” 的 哈 哈 哈 哈 哈')
            print('克拉希斯：在这里，我是永恒不朽的，是我，造就的这块大地，是我，成就了如今的你们')
            print('克拉希斯：而你，却妄想成为弑神者？哈 哈 哈 哈 别太天真了 哈 哈 哈 哈 哈 哈')
            print('克拉希斯：你永远只是我们的奴隶，而不听话的奴隶只有一个下场')
            print('克拉希斯：湮灭吧！让我赐予你的终结吧！ 哈 哈 哈')
            print('[环境]：呼 呼 呼 咚 呼呼 ')
            print('[系统]：克拉希斯引爆了傀儡孢子')
            print('[我]：啊啊啊。。。啊啊啊。啊。。啊。。。。。。。。啊。。。')
            print('[我]：。。。。。。呃。。。。。。。。。。。')
            print('[系统]：你的灵魂已经不属于你了')
            print('[低语]： 继  续  完  成  你  的  任  务  。  。 不   要。。。。轻 。 。')
            print('克拉希斯：是的，我。。。。。。')
            print('克拉希斯：去吧，去做你该做的')
            print('克拉希斯：  奴    隶')
            print('[我]：我。。要。。。。打败。。。。。。。。')
            print('[我]：。。。。是的，大人')
            print('克拉希斯：哈 哈 哈 哈 哈 哈 哈 哈 哈')
            print('克拉希斯：快去吧。')
            if self.Ace:
                print('[我]：啊 啊 啊 。 。啊 。。。啊。。我不！。。')
                print('[上帝视角]：你很艰难地从地上爬起')
                print('[系统]：你的理智战胜了腐蚀')
                print('[上帝视角]：你那快要不受控制的手掏出了在腰间的。。。')
                print('[上帝视角]：那把左轮')
                print('[我]：我\n[我]：命\n[我]：由\n[我]：我\n[我]：不\n[我]：由\n[我]：天！')
                print('[环境]：嘭！')
                print('克拉希斯：。。。额。。额。。我。。。。')
                print('[环境]：嘭！')
                print('克拉希斯：啊啊啊。。。。你！')
                print('[环境]：嘭！')
                print('克拉希斯：啊！这怎么可能！啊啊')
                print('[环境]：嘭！')
                print('[环境]：嘭！')
                print('[环境]：嘭！')
                print('克拉希斯：啊')
                print('[上帝视角]：克拉希斯倒在了地上，急促地呼吸着')
                print('克拉希斯：呵。。。。呵。。。。你。。。的。。。意志。。。怎么可能。。。。这么。。。。。坚定。。。。。。')
                print('克拉希斯：哈 哈 咳 。。。咳。。')
                print('[上帝视角]：克拉希斯吐出了黑色的血液')
                print('克拉希斯：杀了我，你 也 得 。。。陪  葬，哈 哈 哈 哈 哈 哈 哈 哈 哈 哈，哈 哈 哈 哈 哈')
                print('[上帝视角]：你闭上了眼')
                print('[环境]：嘭！')
                print('[上帝视角]：克拉希斯的手垂了下来')
                print('[环境]：哐啷哐啷')
                print('[上帝视角]：以因为克拉希斯的死去，因他的意志所筑起的时间开始崩塌')
                print('[上帝视角]：一且事物随着他的消失而腐化')
                print('[上帝视角]：而你，也永远消失在了时间的黑暗角落')
            else:
                print('[我]：尊\n[我]：命！')
                print('[上帝视角]：你的一切已经永远归属 遗落之徒之一   克拉希斯')
            TangMork.line(False)
            print('感谢你的游玩')
            input('enter退出')
            Music.sound_stop()
            os._exit(0)

    def death_detect(self,detect=False):
        if self.health <= 0 or not detect:
            if detect:
                Music.sound_stop()
                threading.Thread(target=Music.choice_music).start()
            self.reborn -= 1
            if self.reborn < 0:
                print('你已死亡')
                input('enter退出')
                Music.sound_stop()
                os._exit(0)
            print('你的光能暂时消散了')
            TangMork.line()
            print('\t\t神仙路过看你可怜，你复活了')
            TangMork.line(start=False)
            self.health = 2
            self.attack = 0
            self.defense= 1
            self.have_tools = []
            self.have_tools_durability = {}
            self.choice()

    def durability_detect(self,name):
        self.have_tools_durability[name] -= 1
        if self.have_tools_durability[name] <= 0:
            self.have_tools.remove(name)
            self.have_tools_durability.pop(name)

    @property
    def state(self):
        return f'你的攻击力是:{self.attack}  你的生命值是:{self.health}  防御力是:{self.defense}  复活次数:{self.reborn}'
    
    @property
    def boss_state(self):
        return f'白骨精的攻击力是:{self.boss_attack}  白骨精的生命值是:{self.boss_health}'

    @classmethod
    def line(cls,start=True):
        if start:
            print('='*72 +'\n')
        else:
            print('\n'+'='*72)

    @classmethod
    def start(cls):
        threading.Thread(target=Music.start_music).start()
        print('已然熟睡的你')
        print('梦见了一些，一些模糊，无法触及，且似令人熟悉的东西')
        print('这是。。。')
        print('是一条，一段')
        print('一段被遗落的时间线。。。') #7s
        print('这里面。。存在着一些被遗忘很久很久了的事情')
        print('而    他    们    正    朝    你    而    来')
        print('='*20,'欢迎来到游戏《唐僧大战白骨精》','='*20)
        print('请选择你的身份:')
        print('\t (1.唐僧')
        print('\t (2.白骨精')
        print('')
        choose =  input('请选择(1-2):')
        if choose == '1':
            print('你已经选择唐僧，恭喜你将以唐僧的身份进行游戏！',)
        elif choose == '2':
            print('什么你竟然选择了白骨精？太不要脸了，系统将自动分配你以唐僧的身份进行游戏!')
        else:
            print('你输入的选项有误，系统自动分配你以唐僧的身份进行游戏！')
        TangMork.line(start=False)
        Music.sound_stop()
        threading.Thread(target=Music.choice_music).start()

    def choice(self):
        print(f'你的身份是-->唐僧<--，{self.state}')
        print('请选择你要做的操作:')
        for i in range(len(Data.choice('name'))):
            print(f"\t ({i+1}.{Data.choice('name')[i]}")
        choose = input('\n请选择(1-3):')
        #练级
        if choose == str(Data.choice('[?(@.index==1)].index')[0]):
            self.train()
            self.choice()
        #打boss
        elif choose == str(Data.choice('[?(@.index==2)].index')[0]):
            self.boss()
            self.choice()
        #逃跑
        elif choose == str(Data.choice('[?(@.index==3)].index')[0]):
            print('什么？逃跑？',random.choice(Data.run_death))
            self.death_detect()
        #退出
        elif choose == str(Data.choice('[?(@.index==4)].index')[0]):
            Music.sound_stop()
            os._exit(0)
        #Ace
        elif choose == 'Ace':
            self.Ace = True
            TangMork.line()
            print(f"\t\t 练级成功！来自异世界的产物 --- 左轮，上面刻着“How about your sister ?”")
            TangMork.line(False)
            self.choice()
        #非法数据
        else:
            print(f'让我们看看操作{choose}是什么，哦，是自杀，你死了')
            self.death_detect()
            self.choice()

    def train(self):
        TangMork.line()
        #已有全部武器
        if len(self.have_tools) == len(Data.tools(attr="id")):
            print('\t\t 都叫你别吃太饱，你看，神力太多撑死了吧')
            TangMork.line(start=False)
            self.death_detect()
        #获取武器
        tool = random.choice(Data.tools(attr='name'))
        #练级失败
        if tool in self.have_tools:
            if len(self.have_tools) >= int(len(Data.tools(attr='id'))*0.7):
                print('\t\t 练级失败,但有古文记载‘人不可以吃太饱’')
            else:
                print('\t\t 练级失败,再接再厉')
        #练级成功
        else:
            print(f"\t\t 练级成功！{Data.extract_attr('describe',from_attr={'name':tool})[0]}")
            #增加经过算法的武器数值，生命，防御到玩家身上
            self.health  += random.randint(100,150)
            self.defense += random.randint(100,250)
            if tool in Data.tools(attr='name',form='ordinary'):
                self.attack += 50
            elif Data.extract_attr(attr ='class',from_attr={'name':tool})[0] == 'attack':
                self.attack += random.randint(int(Data.extract_attr('damage',from_attr={'name':tool})[0]*0.3),int(Data.extract_attr('damage',from_attr={'name':tool})[0]*0.7))
            else:
                self.defense += random.randint(int(Data.extract_attr('defense',from_attr={'name':tool})[0]*0.3),int(Data.extract_attr('defense',from_attr={'name':tool})[0]*0.7))
            self.have_tools.append(tool)
            self.have_tools_durability[tool] = Data.extract_attr('durability',from_attr={'name':tool})[0]
        TangMork.line(start=False)
        return None

    def boss(self):
        Music.sound_stop()
        threading.Thread(target=Music.fight_music).start()
        TangMork.line()
        print('\t\t 你即将与终级大boss战斗')
        TangMork.line(start=False)
        #是否第一次打
        if self.boss_time == 0:
            self.boss_time += 1
            print('白骨精：哈哈哈，小小唐僧就像想打败我')
        else:
            print('白骨精：想不到你还敢回来？')
        #没技能
        if len(self.have_tools) == 0:
                print('[系统]：你没技能可选\n[系统]：你的生命 -999')
                Music.sound_stop()
                threading.Thread(target=Music.choice_music).start()
                self.death_detect()
        #rush
        if self.boss_health <= 200:
            self.rush()
        #打boss
        while True:
            TangMork.line()
            print(f'\t{self.state}\n\t{self.boss_state}')
            TangMork.line(start=False)
            print('[系统](输入你要使出的技能):\n')
            for i in range(len(self.have_tools)):
                if Data.extract_attr('id',{'name':self.have_tools[i]})[0] == 409:
                    print(f"\t({i+1}.{self.have_tools[i]} \t\t  p p 值：{self.have_tools_durability[self.have_tools[i]]}")
                else:
                    print(f"\t({i+1}.{self.have_tools[i]} \t\t耐久剩余：{self.have_tools_durability[self.have_tools[i]]}")
            print(f'\t({len(self.have_tools)+1}.退出')
            #输入
            choose = input('\n[你]:')
            if Data.number(choose):
                if int(choose) == len(self.have_tools)+1:
                    TangMork.line(start=False)
                    Music.sound_stop()
                    threading.Thread(target=Music.choice_music).start()
                    return None
                elif 1 <= int(choose) <= len(self.have_tools):
                    tool = self.have_tools[int(choose)-1]
                    print(f'[系统]：你选择了‘{tool}’')
                    self.event(Data.extract_attr('id',from_attr={'name':tool})[0])
                    if self.boss_health <= 200:
                        self.rush()
                    self.death_detect(detect=True)
                    continue
            print('[系统]：你自己看看你输入了什么？')

    def event(self,tool_id,rush=False):
        boss_attack = random.randint(int(self.boss_attack*0.5),self.boss_attack)
        self.durability_detect(Data.extract_attr('name',from_attr={'id':tool_id})[0])
        if Data.extract_attr('class',from_attr={'id':tool_id})[0] == 'attack':
            #player event
            damage = int(Data.extract_attr('damage',from_attr={'id':tool_id})[0] + (self.attack*0.3))
            if not rush:
                if   tool_id == 402:
                    if input('') == '!ejf2?':
                        print('白骨精：什么？？？啊啊啊啊啊啊啊！！！好痛，好喜欢哈哈哈哈')
                    else:
                        print('白骨精：给你法杖你也不会用啊，哈哈哈哈哈哈哈哈哈哈哈')
                        damage = 0
                elif tool_id == 403:
                    print('白骨精：啊啊啊啊啊啊')
                    print('白骨精：什么？桃木剑？！？就这吗？哈哈哈哈哈哈')
                elif tool_id == 404:
                    print('[环境]：砰！嘶嘶嘶！砰！') 
                    print('白骨精：啊啊啊啊，什么xxx东西')
                    print('白骨精：不过，哈哈哈哈哈哈')
                    print('白骨精：不痛不痒，味道刚刚好') 
                elif tool_id == 406:
                    print('[环境]：滋 滋 滋滋 滋滋滋 滋滋')
                    print('白骨精：这又是什么啊')
                    print('白骨精：我去，要不是我文化比鱼蛋还高。。。这啥啊，牛子啊')
                    print('白骨精：@#&!%! 烫我屁股 @#@*! ')
                    print('白骨精：鱼蛋，干他！')
                elif tool_id == 408:
                    print('[系统]：你很帅的甩出了闪电5连挽歌')
                    print('[环境]：哗 哗 哗 哗 哗')
                    print('白骨精：干你六舅啊， 给爷干毁容啦啊！')
                    print('白骨精：你让我以后怎么找作者约会啊!')
                    print('白骨精：呜~ 呜~ 呜~')
                elif tool_id == 409:
                    print('[系统](输入你要使出的技能):\n')
                    print('\t1.龙爪')
                    print('\t2.火焰漩涡')
                    print('\t3.爆炸烈焰')
                    while True:
                        choose = input('\n[你]:')
                        if choose == '1' or choose == '2' or choose == '3':
                            print('[环境]：唰 唰')
                            print('白骨精：这龙怎么干啥都怎么烫啊！跟上次那位高人给我吃的叫，叫什么来着。。。火锅！好吃。')
                            break
                        print('[系统]：你自己看看你输入了什么？')
                elif tool_id == ' ':
                    pass
                else:
                    print('白骨精：就这？哈哈哈')
            self.boss_health -= damage
            print(f'[系统]：你造成{damage}点伤害')
            self.health,self.defense = self.boss_damage(boss_attack)
            if not rush:
                print(f'白骨精：{random.choice(Data.boss_talk)}')
                print(f'[系统]：对方使用了 *** 技能')
            else:
                print(f'克拉希斯：{random.choice(Data.Crasis_talk)}')
                print(f'[系统]：对方使用了 {random.choice(Data.Crasis_ability)} 技能')
            print(f'[系统]：你遭到{boss_attack}点伤害')

        elif Data.extract_attr('class',from_attr={'id':tool_id})[0] == 'defense':
            defense = int(Data.extract_attr('defense',from_attr={'id':tool_id})[0])
            self.defense += defense
            print(f'[系统]：防御增加了{defense}')
            self.health,self.defense = self.boss_damage(boss_attack,1.499,0.001)
            if not rush:
                print(f'白骨精：{random.choice(Data.boss_talk)}')
                print(f'[系统]：对方使用了 *** 技能')
            else:
                print(f'白骨精：{random.choice(Data.Crasis_talk)}')
                print(f'[系统]：对方使用了 {random.choice(Data.Crasis_ability)} 技能')
            if not rush:
                if   tool_id == 401:
                    print('白骨精：干！打不动？')
                    print('白骨精：可恶')
                elif tool_id == 405:
                    print('[环境]：滴 度 度 滴 滴 滴 滴 度')
                    print('[vex]：时间线不对？走吧')
                    print('白骨精：这 b 时 间 怎 么 突 然 这 么 慢 啊 ！')
                    print('白骨精：这 要 要 抱 住 你 的 节 奏 啊 ！')
                    print('[系统]：。。。我该说什么呢。。。')
                    print('白骨精：刚刚什么事也没发生。。。')
                elif tool_id == 407:
                    print('白骨精：？这又是干啥，你byd拉屎是吧')
                    print('白骨精：趋势吧！')
                    print('白骨精：卧槽？开金身了是吧，还是18铜人附身啊')
                    print('白骨精：这xxx打不动，手还贼痛')
                elif tool_id == 410:
                    print('白骨精：你那什么破盾，还想防我？哈哈哈看招')
                    print('[低语]：这此的。。。也太。。。回。。小心！。。娜！。。。')
                    print('[系统]：护盾突然发出了一股能量波')
                    print('白骨精：看不见啦！这什么东西！不就一破盾吗？怎么tm还会说话')
                elif tool_id == 411:
                    print('白骨精：。。。什么玩意儿。。。')
                    print('白骨精：你要回卵重造？')
                elif tool_id == ' ':
                    pass
            print(f'[系统]：你遭到{boss_attack}点伤害,但大多被挡下')
        
    def boss_damage(self,boss_attack,defend_pro=1.4,attack_pro=0.1):
    #伤害算法
        if self.defense <= 0:
            self.health -= boss_attack
            self.defense = 0
        else:
            self.defense-= boss_attack*defend_pro
            self.health -= boss_attack*attack_pro
            if self.defense <= 0:
                self.health += self.defense/defend_pro
                self.defense = 0
        return int(self.health),int(self.defense)

    def rush(self,health=10000):
        if self.health <= 100:
            self.health += 400
        self.reborn = 0
        self.boss_health = health
        self.boss_attack *= 3

        print('白骨精：等等，这是什么？啊啊啊啊啊啊啊啊')
        print('白骨精：为什么？？？啊啊啊啊')
        print('白骨精：/\/\/\/\^----------哈 哈 哈 哈 。 。 。')
        TangMork.line(start=False)
        sleep(3)
        Music.sound_stop()
        print('白骨精：这 场 戏 是 时 候 收 尾 了')
        print('白骨精：你 不 会 那 么 天 真 的 以 为 我 会 为 你 表 演 到 底 吧 ？')
        print('白骨精：那 些 小 玩 具 也 挺 有 意 思 的')
        print('白骨精：哈 哈 哈 哈 哈 哈 哈 哈')
        print('白骨精：这 层 皮 也 该 脱 下 了')
        print('克拉希斯：真 难 脱 啊 ，呵')
        if '法杖' in self.have_tools:
            self.have_tools_durability['法杖'] -= 100
            self.durability_detect('法杖')
            print('克拉希斯：你那个法杖确实挺有趣的，不过，是易碎品，哈哈哈哈')
            print('[环境]：呲 呲 咳 咳 呲 哐啷')
            print('[系统]：你的法杖已损坏')
        print('克拉希斯：还有你，死老头，感受腐蚀吧！哈 哈 哈 哈')
        print('神仙：吾乃仙，具不死。。。啊啊啊啊 。不。。。我的身体。。啊 啊 啊 。。。。。。')
        print('克拉希斯：现在没人，能 拯 救 你 了，哈 哈 哈 哈')
        print('[系统]：你的复活次数为 0')
        print('光能已被腐蚀殆尽')
        threading.Thread(target=Music.rush_music).start()
        TangMork.line()
        print('\t\t\t最后一搏 《遗落之徒-克拉希斯》 \n')
        temp = False
        while True:
            if temp:
                TangMork.line()
            temp = True
            boss_state = self.boss_state.replace('白骨精','遗落之徒-克拉希斯 ')
            print(f'\t{self.state}\n\t{boss_state}')
            TangMork.line(start=False)
            print('[系统](输入你要使出的技能):\n')
            for i in range(len(self.have_tools)):
                if Data.extract_attr('id',{'name':self.have_tools[i]})[0] == 409:
                    print(f"\t({i+1}.{self.have_tools[i]} \t\t  p p 值：{self.have_tools_durability[self.have_tools[i]]}")
                else:
                    print(f"\t({i+1}.{self.have_tools[i]} \t\t耐久剩余：{self.have_tools_durability[self.have_tools[i]]}")
            #输入
            choose = input('\n[你]:')
            if Data.number(choose):
                if 1 <= int(choose) <= len(self.have_tools):
                    tool = self.have_tools[int(choose)-1]
                    print(f'[系统]：你选择了‘{tool}’')
                    self.event(Data.extract_attr('id',from_attr={'name':tool})[0],True)
                    self.boss_death_detect()
                    if self.health <= 0 :
                        print('克拉希斯：忠诚激起勇敢，勇敢激起牺牲，而牺牲，导致死亡，哈 哈 哈 哈 哈 哈 哈 哈 哈 哈 。。。。')
                        print('[系统]：你的灵魂已成为克拉希斯的贡品')
                        print('你已死亡')
                        input('enter退出')
                        Music.sound_stop()
                        os._exit(0)
                    continue
            print('[系统]：你自己看看你输入了什么？')

if __name__ == '__main__':
    pass
