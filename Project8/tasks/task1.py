#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    teams_and_points = [
        ("Команда1", 30),
        ("Команда2", 25),
        ("Команда3", 20),
    ]

    n = int(input("Введите количество очков: "))

    sorted_teams = sorted(teams_and_points, key=lambda x: x[1], reverse=True)

    place = sorted_teams.index(next(filter(lambda x: x[1] == n, sorted_teams))) + 1

    print(f"Команда, набравшая {n} очков, заняла {place} место.")
