# -*- coding: utf-8 -*-
import random
dic = {"智商=":"iq","情商":"eq","体魄":"hp","魅力":"ml"}


def add(person, aspect, inc):#属性值改变
    if aspect == "智商":
        person.iq += inc
    if aspect == "情商":
        person.eq += inc
    if aspect == "体魄":
        person.hp += inc
    if aspect == "魅力":
        person.ml += inc

class Person:
    def __init__(self, name, iq, eq, hp, ml):
        self.name = name # 玩家姓名
        self.iq = random.randint(5,15) # 玩家智商
        self.eq = random.randint(5,15) # 玩家情商
        self.hp = random.randint(5,15) # 玩家体魄
        self.ml = random.randint(5,15) # 玩家魅力
        self.jl = 10
        self.friend = dict() # 玩家好友姓名及好感度
        self.course = list() # 玩家学习的课程

    def learn(self, course): #学习课程
        self.course.append(course)
        return
    
    def make_friend(self, friend):
        if friend not in self.friend:
            self.friend[friend] = 0
        return
    
    def change_friendship(self, friend, inc)
        self.friend[friend] += inc
       




