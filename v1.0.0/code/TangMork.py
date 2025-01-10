import random
from data import Data

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

    def boss_death_detect(self):
        if self.boss_health <= 0:
            print('白骨精：等等，这是什么？啊啊啊啊啊啊啊啊')
            print('白骨精：为什么？？？啊啊啊啊')
            print('白骨精：/\/\/\/\^----------嘟嘟嘟---')
            print('李信华：我去你么的')
            print('[系统]：你已成功打败白骨精，恭喜')
            input('enter退出')
            exit(1)

    def death_detect(self,detect=False):
        if self.health <= 0 or not detect:
            self.reborn -= 1
            if self.reborn < 0:
                print('你已死亡')
                input('enter退出')
                exit(1)
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
        if self.have_tools_durability[name] == 0:
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
            exit(1)
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
            self.health  += random.randint(50,100)
            self.defense += random.randint(100,300)
            if tool in Data.tools(attr='name',form='ordinary'):
                self.attack += 50
            elif Data.extract_attr(attr ='class',from_attr={'name':tool})[0] == 'attack':
                self.attack += random.randint(150,int(Data.extract_attr('damage',from_attr={'name':tool})[0]*0.3))
            else:
                self.defense += random.randint(150,int(Data.extract_attr('defense',from_attr={'name':tool})[0]*0.3))
            self.have_tools.append(tool)
            self.have_tools_durability[tool] = Data.extract_attr('durability',from_attr={'name':tool})[0]
        TangMork.line(start=False)
        return None

    def boss(self):
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
                self.death_detect()
        #打boss
        while True:
            TangMork.line()
            print(f'\t{self.state}\n\t{self.boss_state}')
            TangMork.line(start=False)
            print('[系统](输入你要使出的技能):\n')
            for i in range(len(self.have_tools)):
                print(f"\t({i+1}.{self.have_tools[i]} \t\t耐久剩余：{self.have_tools_durability[self.have_tools[i]]}")
            print(f'\t({len(self.have_tools)+1}.退出')
            #输入
            choose = input('\n[你]:')
            if Data.number(choose):
                if int(choose) == len(self.have_tools)+1:
                    TangMork.line(start=False)
                    return None
                elif 1 <= int(choose) <= len(self.have_tools):
                    tool = self.have_tools[int(choose)-1]
                    print(f'[系统]：你选择了‘{tool}’')
                    self.event(Data.extract_attr('id',from_attr={'name':tool})[0])
                    self.boss_death_detect()
                    self.death_detect(detect=True)
                    continue
            print('[系统]：你自己看看你输入了什么？')

    def event(self,tool_id):
        boss_attack = random.randint(int(self.boss_attack*0.5),self.boss_attack)
        self.durability_detect(Data.extract_attr('name',from_attr={'id':tool_id})[0])
        if Data.extract_attr('class',from_attr={'id':tool_id})[0] == 'attack':
            #player event
            damage = int(Data.extract_attr('damage',from_attr={'id':tool_id})[0] + (self.attack*0.3))
            if   tool_id == 402:
                if input('') == '!ejf2?':
                    print('白骨精：什么？？？啊啊啊啊啊啊啊！！！好痛，好喜欢哈哈哈哈')
                else:
                    print('白骨精：给你法杖你也不会用啊，哈哈哈哈哈哈哈哈哈哈哈')
                    damage = 0
            elif tool_id == 403:
                print('白骨精：啊啊啊啊啊啊')
                print('白骨精：什么？桃木剑？！？就这吗？哈哈哈哈哈哈')
            elif tool_id == ' ':
                pass
            else:
                print('白骨精：就这？哈哈哈')
            self.boss_health -= damage
            print(f'[系统]：你造成{damage}点伤害')
            #boss event
            self.health,self.defense = self.boss_damage(boss_attack)
            print(f'白骨精：{random.choice(Data.boss_talk)}')
            print(f'[系统]：对方使用了 *** 技能')
            print(f'[系统]：你遭到{boss_attack}点伤害')
        elif Data.extract_attr('class',from_attr={'id':tool_id})[0] == 'defense':
            #boss event
            defense = int(Data.extract_attr('defense',from_attr={'id':tool_id})[0])
            self.defense += defense
            self.health,self.defense = self.boss_damage(boss_attack,1.499,0.001)
            print(f'[系统]：防御增加了{defense}')
            print(f'白骨精：{random.choice(Data.boss_talk)}')
            print(f'[系统]：对方使用了 *** 技能')
            print(f'[系统]：你遭到{boss_attack}点伤害,但大多被挡下')
            if   tool_id == 401:
                print('白骨精：干！打不动？')
                print('白骨精：可恶')
            elif tool_id == ' ':
                pass

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

if __name__ == '__main__':
    pass
