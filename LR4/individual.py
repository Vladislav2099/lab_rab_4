# Сумму аргументов, расположенных до последнего положительного аргумента.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def summ(*args):
    if args:
        values = [int(arg) for arg in args]

        end = 0
        for i in values:
            if i > 0:
                end = i
        total = sum(values[:end])
        return total


if __name__ == "__main__":
    print(summ(1, 2, 3, -1, 6))
