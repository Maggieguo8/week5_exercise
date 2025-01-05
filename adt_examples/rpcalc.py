from numbers import Number
import operator
from math import sin, cos


class RPCalc:

    def __init__(self, stack=[]):
        self.stack = stack

    def push(self, n):
        if isinstance(n, Number):
            self.stack.append(n)

        elif n in ["+", "-", "*", "/"]:
            ops = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv
            }
            operand_2 = self.stack.pop(-1)
            operand_1 = self.stack.pop(-1)
            self.stack.append(ops[n](operand_1, operand_2))

        elif n in ["sin", "cos"]:
            ops = {
                'sin': sin,
                'cos': cos
            }
            operand_1 = self.stack.pop(-1)
            self.stack.append(ops[n](operand_1))

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)
