# -*- coding: utf-8 -*-
import random
dic={"智商=":"iq","情商":"eq","体魄":"hp","魅力":"ml"}


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
        
    def date(self, friend): #约会
        fri_now = self.friend.get(friend, 0)#目前与该好友的好感度
        fri_inc = random.randint(-10 + int(self.ml * 0.2) + int(fri_now * 0.2), 0 + int(self.ml * 0.2) + int(fri_now * 0.2))#好感度的变化量
        self.friend[friend] = fri_inc + fri_now
        print("你尝试与",friend,"约会...")
        if fri_inc > 0:
            print("成功了！好感度加",data,"目前好感度为",self.friend[friend])
        else:
            print("失败了-_-||好感度减",abs(data),"目前好感度为",self.friend[friend])
        if self.friend[friend] >= 90:
            print("你向",friend,"表露了你的心意...你们在一起了")
        if self.friend[friend] <= -50:
            print("”家人们！谁懂啊？",self.name,"真下头~“",friend,"大叫着跑开了")




