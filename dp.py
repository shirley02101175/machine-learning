# -*- coding: utf-8 -*-
import string

def minus(str_a,str_b):
    sum=0
    int_a = map(int,list(str_a))
    int_b = map(int,list(str_b))
    for i in range(len(str_a)):
        sum += abs(int_a[i]-int_b[i])
    return sum
if __name__ == '__main__':
    dict_num={'12':"00",'23':"01",'45':"10",'56':"11",'78':"20",'89':"21",'*0':"30",'0#':"31"}
    str_a = "00"
    sum = 0
    value = ''
    str_num="26986"
    list_num=list(str_num)
    for i in range(len(str_num)):
        move =10
        str_b=list_num[i]
        for key in dict_num.keys():
            if str_b in key:
                if(move > minus(str_a,dict_num[key])):
                    value = dict_num[key]
                    move=minus(str_a,value)
        str_a = value
        sum += move
    print sum
        
