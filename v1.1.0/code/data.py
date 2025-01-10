import jsonpath,json
import os,sys
import threading
from time import sleep
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

#====================定位exe文件=====================
# if getattr(sys,'frozen',False):
#     ABS_PATH = os.path.dirname(os.path.abspath(sys.executable))
# elif __file__:
#     ABS_PATH = os.path.dirname(os.path.abspath(__file__))
#===================================================

class Data:
    # #=====================定位py文件======================
    path = os.path.dirname(__file__).replace('code','data') + '\\data.json'
    obj = json.load(open(path,encoding='utf-8'))
    # #=====================================================

    #======================定位exe文件=====================
    # path = ABS_PATH.replace(r'\code\dist','\data')
    # obj = json.load(open(f'{path}'r'\data.json',encoding='utf-8'))
    #===================================================

    run_death      = jsonpath.jsonpath(obj,"$..run_death")[0]
    boss_talk      = jsonpath.jsonpath(obj,"$..boss_talk")[0]
    Crasis_talk    = jsonpath.jsonpath(obj,"$..Crasis_talk")[0]
    Crasis_ability = jsonpath.jsonpath(obj,"$..Crasis_ability")[0]
    @classmethod
    def number(cls,string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    @classmethod
    def choice(cls,attr):
        return jsonpath.jsonpath(Data.obj,f"$..choice..{attr}")

    @classmethod
    def tools(cls,attr:str,form:str='tools') -> list:
        result = jsonpath.jsonpath(Data.obj,f"$..{form}..{attr}")
        if not result:
            exit(f"attribute '{attr}' not found")
        return result

    @classmethod
    def extract_attr(cls,attr:str,from_attr:dict,form:str='tools') -> list:
        key = list(from_attr.keys())[0]
        if type(from_attr[key]) == str:
            from_attr[key] = f'"{from_attr[key]}"'
        result = jsonpath.jsonpath(Data.obj,f"$..{form}..[?(@.{key}=={from_attr[key]})].{attr}")
        if not result:
            exit(f"attribute '{attr}' not found")
        return result

class Music:
    #=====================定位exe文件======================
    # path = ABS_PATH.replace(r'\code\dist','\data')
    #=====================================================
    # #=====================定位py文件======================
    path = os.path.dirname(__file__).replace('code','data')
    # #=====================================================

    stop = False
    pygame.mixer.init()
    start  = pygame.mixer.Sound(f'{path}'r'\music_start.ogg')
    rush_1 = pygame.mixer.Sound(f'{path}'r'\music_rush_1.ogg')
    rush_2 = pygame.mixer.Sound(f'{path}'r'\music_rush_2.ogg')
    choice = pygame.mixer.Sound(f'{path}'r'\music_choice.ogg')
    fight  = pygame.mixer.Sound(f'{path}'r'\music_fight.ogg')

    @staticmethod
    def sound_stop():
        Music.stop = True
        sleep(1)
        Music.stop = False

    @staticmethod
    def start_music():
        Music.start.set_volume(0.5)
        Music.start.play()
        for i in range(int(Music.start.get_length())):
            if not Music.stop:
                sleep(1)
            else:
                break
        Music.start.fadeout(1500)
        sleep(1.5)

    @staticmethod
    def choice_music():
        while True:
            if not pygame.mixer.get_busy():
                Music.choice.play()
                sleep(1)
            elif not Music.stop:
                sleep(1)
            else:
                break
        Music.choice.fadeout(1000)
        sleep(1)

    @staticmethod
    def fight_music():
        while True:
            if not pygame.mixer.get_busy():
                Music.fight.play()
                sleep(1)
            elif not Music.stop:
                sleep(1)
            else:
                break
        Music.fight.fadeout(1000)
        sleep(1)
        
    @staticmethod
    def rush_music():
        temp = True
        Music.rush_1.play()
        for i in range(int(Music.rush_1.get_length())-3):
            if not Music.stop:
                sleep(1)
            else:
                temp = False
                Music.rush_1.fadeout(1000)
                sleep(1)
        while True and temp:
            Music.rush_2.play()
            for j in range(int(Music.rush_2.get_length())-3):
                if not Music.stop:
                    sleep(1)
                else:
                    Music.rush_2.fadeout(1000)
                    sleep(1)

if __name__ == "__main__":
    pass


    

