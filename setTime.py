# -*- coding:utf-8 -*-

import sys
import os
import datetime,calendar

#######################以下是要用到的日期处理函数##############################
def addZero(n): 
    '''
    传来一个整数,如果小于10则补零,返回字符串
    '''
    nabs = abs(int(n)) 
    if(nabs < 10): 
        return "0" + str(nabs) 
    else: 
        return nabs

def getOneMonthDays(year,mon): 
    '''
    返回一个月有多少天
    ''' 
    return calendar.monthrange(year, mon)[1]

def addDay(dt,d=0):
    '''
    d > 0:加上d天
    d < 0:减去d天
    dt:字典类型,从这个日期基础上加上或者减去d天,例子:
    dt = {              
            'year':2016,    
            'month':8,      
            'day':15        
        }
    返回值:一个由年,月,日组成的元组,如:(year,month,day),其实最终的结果也会保存在dt里面
    '''
    if 0 == d:
        return (dt['year'],dt['month'],dt['day'])    #不需要做任何事情

    num = 0
    mon = 0
    tolday = 0                                #总天数,用来计算有多少个月
    curday = dt['day']                        #当前日期
    if d > 0:
        mday = getOneMonthDays(dt['year'],dt['month'])
        if d <= mday :
            tolday = d + dt['day']
            mon = int(tolday / mday)
            dt['day'] = int(tolday % mday)
            if 0 == dt['day']:
                dt['day'] = mday
                if mon > 0:
                    mon -= 1
        else:                               #由于getOneMonthDays每次都是取到当月的天数,如果d大于30多会漏掉一些情况,需要重新计算dt['day']和mon
            i = 0
            d -= getOneMonthDays(dt['year'],dt['month']) - curday                    #填满第一个月,以后的都是整月
            while d > getOneMonthDays(dt['year'] + int((dt['month'] + i) / 12),((dt['month'] + i) % 12) + 1):             
                d -= getOneMonthDays(dt['year'] + int((dt['month'] + i) / 12),((dt['month'] + i) % 12) + 1)        #如果天数超过一个月,就划掉一个月,月数加1,这里主要是保证一个月的天数是准确的
                i += 1
            dt['day'] = d                             #算出不足一个月的天数
            mon = i + 1                               #算出需要加多少个月,现在i是满整月的数量
    else:
        tolday = d + dt['day']
        if 0 == tolday :
            dt['day'] = getOneMonthDays(dt['year'] + int((dt['month'] - 2) / 12),((dt['month'] - 2) % 12) + 1)
            mon = -1
        elif tolday > 0:
            dt['day'] = tolday
            mon = 0
        else:
            i = -2                                     #由于为了避免出现getOneMonthDays(year,0)月份等于0的情况,只好取余后加1,所以这里要等于-2
            mon -= 1
            tolday += getOneMonthDays(dt['year'] + int((dt['month'] + i) / 12),((dt['month'] + i) % 12) + 1)     #一直加,直到tolday为大于等于0为止
            while tolday < 0:
                i -= 1
                tolday += getOneMonthDays(dt['year'] + int((dt['month'] + i) / 12),((dt['month'] + i) % 12) + 1)
            if 0 == tolday:
                i -= 1
                dt['day'] = getOneMonthDays(dt['year'] + int((dt['month'] + i) / 12),((dt['month'] + i) % 12) + 1)
                mon = i + 1
            else:
                dt['day'] = tolday
                mon = i + 1
    return addMonth(dt,mon)

def addMonth(dt,mon=0):
    '''
    m > 0:加上m月
    m < 0:减去m月
    dt:字典类型,从这个日期基础上加上或者减去m月,例子:
    dt = {              
            'year':2016,    
            'month':8,      
            'day':15        
        }
    返回值:一个由年,月,日组成的元组,如:(year,month,day)
    '''
    if 0 == mon:
        return (dt['year'],dt['month'],dt['day'])

    if mon > 0:
        mon += dt['month']
        year = int(mon / 12)
        dt['month'] = int(mon % 12)
        if 0 == dt['month']:
            dt['month'] = 12
            if year > 0:
                year -= 1
        dt['year'] += year
    else:
        mon += dt['month']
        if mon > 0 and mon < 12:
            dt['month'] = mon
        else:
            year = int(mon / 12)
            dt['month'] = int(mon % 12)
            if 0 == dt['month']:
                dt['month'] = 12
                year -= 1
            dt['year'] += year
    return (dt['year'],dt['month'],dt['day'])

def addYear(dt,y=0):
    '''
    y > 0:加上y年
    y < 0:减去y年
    dt:字典类型,从这个日期基础上加上或者减去y年,例子:
    dt = {              
            'year':2016,    
            'month':8,      
            'day':15        
        }
    返回值:一个由年,月,日组成的元组,如:(year,month,day)
    '''
    if 0 == y:
        return (dt['year'],dt['month'],dt['day'])
    dt['year'] += y
    return (dt['year'],dt['month'],dt['day'])

#######################以上是要用到的日期处理函数##############################
