# -*- coding: utf-8 -*-
import interactions

def check_role(role_1, role_2, role_3, role_4, role_5):
    flag_top = 0
    flag_mid = 0
    flag_les = 0
    flag_adk = 0
    flag_sup = 0

    for i in role_1, role_2, role_3, role_4, role_5:
        if i == 'Топ':
            flag_top = 1
        if i == 'Мид':
            flag_mid = 1
        if i == 'Лес':
            flag_les = 1
        if i == 'Бот':
            flag_adk = 1
        if i == 'Саппорт':
            flag_sup = 1
    if flag_top and flag_mid and flag_les and flag_adk and flag_sup:
        return 1
    else:
        return 0

def add_member_role():
    return 0