import jsonpath,json
import os,sys

class Data:
    # if getattr(sys,'frozen',False):
    #     ABS_PATH = os.path.dirname(os.path.abspath(sys.executable))
    # elif __file__:
    #     ABS_PATH = os.path.dirname(os.path.abspath(__file__))
    # ABS_PATH = ABS_PATH.replace('\code\dist','\data')

    # obj = json.load(open(f'{ABS_PATH}'r'\data.json',encoding='utf-8'))

    path = os.path.dirname(__file__).replace('code','data') + '\\data.json'
    obj = json.load(open(path,encoding='utf-8'))

    run_death = jsonpath.jsonpath(obj,"$..run_death")[0]
    boss_talk = jsonpath.jsonpath(obj,"$..boss_talk")[0]
    
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
    
if __name__ == "__main__":
    pass