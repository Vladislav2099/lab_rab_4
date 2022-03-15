#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def its_group(kurator, **students):
    print(f"Куратор группы: {kurator}")
    for students, name in students.items():
        sorted(students)
        print(f"{students}: {name}")


if __name__ == "__main__":
    its_group(
        "Гончаров Дмитрий Генадьевич",
        Rafik="Добрый, позитивный", Rostik="Крутой, клёвый, классный",
        Dima="Умный, добрый", Masha="Активная, позитивная",
        Lesha="Смешной, крутой", Katya="Умная, отзвчивая",
        Rudakov="Таинственный, потеряшка")
