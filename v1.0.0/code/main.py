import os,sys
import builtins
import time

# if getattr(sys,'frozen',False):
#     ABS_PATH = os.path.dirname(os.path.abspath(sys.executable))
# elif __file__:
#     ABS_PATH = os.path.dirname(os.path.abspath(__file__))

# ABS_PATH = ABS_PATH.replace('\dist','')
# sys.path.append(ABS_PATH)
from TangMork import *

def main():
    original_print = builtins.print      # 保存原始的 print 函数引用
    def print_hook(*args, **kwargs):
        original_print(*args, **kwargs)  # 调用原始的 print 函数
        time.sleep(1)
    builtins.print = print_hook          # 替换 print 函数
    #====================================#
    # 在这里编写需要执行的 Python 代码
    game = TangMork()
    game.start()
    game.choice()
    #====================================#
    builtins.print = original_print      # 还原 print 函数

if __name__ == "__main__":
    main()

