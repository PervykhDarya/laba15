#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def show_perimeter(func):
    def wrapped(*args):
        print(f"Периметр фигуры равен = {func(args)}")

    return wrapped


@show_perimeter
def count_perimeter(sides):
    perimeter = sum(side for side in sides)
    return perimeter


if __name__ == "__main__":
    sides_tuple = tuple(int(side) for side in input().split())
    count_perimeter(*sides_tuple)