"""
在python中，对于全局变量的修改需要声明global，不然会产生 未声明就引用 的错误；
官方文档中是这么写的：
  It would be impossible to assign to a global variable without global,
  although free variables may refer to globals without being declared global.
大致意思：尽管不是用global声明也可以引用全局变量，但是如果要赋值不用就不行。
特此记录下来，防止掉坑里。
"""


GLOBAL_VARIABLE = 'global_variable'


# ==============Wrong==============
def change_variable1():
    print(GLOBAL_VARIABLE)
    GLOBAL_VARIABLE = 'change_global_variable'
    print(GLOBAL_VARIABLE)
# ==============Wrong==============


# ==============True==============
def change_variable2():
    global GLOBAL_VARIABLE
    print(GLOBAL_VARIABLE)
    GLOBAL_VARIABLE = 'change_global_variable'
    print(GLOBAL_VARIABLE)
# ==============True==============
