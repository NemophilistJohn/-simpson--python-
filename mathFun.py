import time
from math import sin, cos, log, e, pi, sqrt,tan,asin,atan,acos
from sympy import symbols, integrate


class MathFunction(object):
    """代码逻辑中此类为一‘虚拟层’，为后续主类的父类，也是开发中预留的接口"""
    """数学方法类，其中包含辛普森公式、梯形公式、复化梯形公式、复化辛普森公式等法"""

    def __init__(self, func_str, min_line, max_line, cut_num='100'):
        """:param:func_str : <str.> function string in pyhton type;
                  min_line : <float/int.> min_line for function class
                  max_ling : <float/int.> ...
        """
        self.func_str = func_str
        self.min_line = min_line
        self.max_line = max_line
        self.cut_num = cut_num

    def __calculate_functions_value(self, parm):
        """隐方法，类中调用以得到函数值"""
        fun_str = str(self.func_str)
        value_funStr = fun_str.replace('x', str(parm))
        res = eval(value_funStr)
        return res

    def simpson_func(self):
        """辛普森公式
        :param : self
        :return result by use the simpson func
        """
        min_line, max_line = tuple(map(eval, [self.min_line, self.max_line]))
        res = (max_line - min_line) * (
                self.__calculate_functions_value(min_line)
                + 4 * self.__calculate_functions_value((min_line + max_line) / 2)
                + self.__calculate_functions_value(max_line)) / 6.0
        return res

    def trapezium_func(self):
        """梯形公式
        :param : self
        :return result by use the trapezium func
        """
        min_line, max_line = tuple(map(eval, [self.min_line, self.max_line]))
        res = 0.5 * (max_line - min_line) * (self.__calculate_functions_value(max_line)
                                             + self.__calculate_functions_value(min_line))
        return res

    def compound_trapezium(self):
        """复化梯形公式"""
        min_line, max_line, n = tuple(map(eval, [self.min_line, self.max_line, self.cut_num]))
        init_num = 0.0
        pa_m = (max_line - min_line) / n
        init_num = self.__calculate_functions_value(max_line) + self.__calculate_functions_value(min_line)
        for k in range(1, int(n)):
            xk = min_line + k * pa_m
            init_num = init_num + 2 * self.__calculate_functions_value(xk)
        res = init_num * pa_m / 2
        return res

    def compound_simpson(self):
        """复化辛普森公式"""
        min_line, max_line, n = tuple(map(eval, [self.min_line, self.max_line, self.cut_num]))
        si = 0.0
        h = (max_line - min_line) / (2 * n)
        si = self.__calculate_functions_value(min_line) + self.__calculate_functions_value(max_line)
        for k in range(1, int(n)):
            xk = min_line + k * 2 * h
            si = si + 2 * self.__calculate_functions_value(xk)
        for k in range(int(n)):
            xk = min_line + (k * 2 + 1) * h
            si = si + 4 * self.__calculate_functions_value(xk)
        res = si * h / 3
        return res


class MathEncapsulation(MathFunction):
    __slots__ = ('func_str', 'min_line', 'max_line', 'cut_num')

    def __init__(self, func_str, min_line, max_line, cut_num='20'):
        super().__init__(func_str, min_line, max_line, cut_num='20')
        self.mode = []

    def __info_inputer(self):
        mode_dict = {'1': '辛普森', '2': '梯形', '3': '复化辛普森', '4': '复化梯形'}
        self.func_str = input('请输入python格式的函数表达式：')
        self.max_line, self.min_line = input('区间上限 区间下限（空格隔开）：').split()
        print('请输入需要计算的模式，不输入默认全部计算：\n'
              '（可选模式 ： 1=辛普森，2=梯形，3=复化辛普森，4=复化梯形\n')
        while True:
            mode_single = input(f'你已选择{self.mode},请继续编辑，或按回车结束：')
            if mode_single in self.mode:
                self.mode.remove(mode_single)
                print(f'{mode_dict[mode_single]}模式成功移除计算队列')

            elif mode_single == '':
                if '3' in self.mode or '4' in self.mode:
                    self.cut_num = input('模式选择完毕，由于选择了复化方法，请输入区间等分数n = ')
                else:
                    print('模式输入完毕')
                    time.sleep(1)
                    print('正在计算...')
                    time.sleep(1.5)
                print('\n... ...')
                break
            elif mode_single not in {'1', '2', '3', '4'}:
                print('输入不合法，可选模式 ： 1=辛普森，2=梯形，3=复化辛普森，4=复化梯形')
            else:
                self.mode.append(mode_single)

    def main_cul(self):
        self.__info_inputer()
        if self.mode == []:
            self.mode = ['1', '2', '3', '4']
        for i in self.mode:
            if i == '1':
                print(f'辛普森法计算结果 ：{self.simpson_func()}')
            elif i == '2':
                print(f'梯形法计算结果：{self.trapezium_func()}')
            elif i == '3':
                print(f'复化辛普森计算结果：{self.compound_simpson()}')
            elif i == '4':
                print(f'复化梯形计算结果{self.compound_trapezium()}')
        print('===============计算完毕=================\n重新输入，以开始新的计算')


def main():
    print('\n====================================================================\n\n'
          '本程序代码已开源，开源地址：https://github.com/czb2002/-simpson--python-.git\n'
          '\n====================================================================\n')
    while True:
        A = MathEncapsulation(1, 2, 3, 4)
        A.main_cul()

if __name__ == '__main__':
    main()
