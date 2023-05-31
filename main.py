import random
from graphics import *
import person
from button import *
import random_events

interface2 = GraphWin("游戏界面", 1000, 500,autoflush=False)

def interaction1():#登入界面
      interface1= GraphWin("登入界面",1000,500)
      interface1.setBackground("aqua")
      #start和end两个按钮
      start= Rectangle(Point(400,100),Point(600,200))
      start.draw(interface1)
      start = Button(interface1, Point(500, 150), 200, 100, "点此处开始游戏")
      start.activate()
      end = Rectangle(Point(400,300),Point(600,400))
      end.draw(interface1)
      end = Button(interface1, Point(500, 350), 200, 100, "点此处退出游戏")
      end.activate()

      #判断鼠标按键
      pt = interface1.getMouse()
      while not end.clicked(pt):
            if start.clicked(pt):
                  interface1.close()
                  interaction2()
            else:
                  pt = interface1.getMouse()
      else:
            interface1.close()
                  
def interaction2():#游戏界面
      #绘制界面
      Line(Point(100, 0), Point(100, 500)).draw(interface2)
      Rectangle(Point(200,50),Point(300,150)).draw(interface2)
      Line(Point(350,0),Point(350,350)).draw(interface2)
      Line(Point(0, 0), Point(999, 0)).draw(interface2)
      Line(Point(999, 0), Point(999, 500)).draw(interface2)
      Line(Point(0,500), Point(999, 500)).draw(interface2)
      Line(Point(0, 0), Point(0, 500)).draw(interface2)
      Line(Point(700,350),Point(700,500)).draw(interface2)
      Line(Point(100, 350), Point(999, 350)).draw(interface2)
      Line(Point(350, 280), Point(1000, 280)).draw(interface2)
      Text(Point(150,25), "姓名：").draw(interface2)
      pt = interface2.getMouse()
      inputtext = Entry(Point(200,25),5)
      inputtext.draw(interface2)
      name = inputtext.getText()
      inputtext.undraw()
      #定义角色
      time = 1
      character = person.Person('eason', random.randint(5, 15), random.randint(5, 15), hp = random.randint(5, 15), ml = random.randint(5, 15))#character代替user1

      #绘制界面
      Text(Point(190, 25), 'eason').draw(interface2)
      Text(Point(150,120),"回合").draw(interface2)
      Text(Point(150,180), "精力：").draw(interface2)
      Text(Point(150,200), "智力：").draw(interface2)
      Text(Point(150,240), "情商：").draw(interface2)
      Text(Point(150,280), "体魄：").draw(interface2)
      Text(Point(150,320), "魅力：").draw(interface2)
      Text(Point(625, 50), "你选择了:").draw(interface2)
      Text(Point(150,375),"所修课程：").draw(interface2)
      Text(Point(250, 100), "点击上传图片").draw(interface2)
      Text(Point(775, 375), "备选对象与交互值：").draw(interface2)
      Text(Point(875, 375), character.friend).draw(interface2)
      Text1 =Text(Point(660, 120), "")
      Text2 =Text(Point(660, 160), "")
      Text3 =Text(Point(660, 200), "")
      Text4 =Text(Point(660, 240), "")
      Text1.draw(interface2)
      Text2.draw(interface2)
      Text3.draw(interface2)
      Text4.draw(interface2)
      choiceA = Button(interface2, Point(420, 320), 100, 50, "A")
      choiceA.activate()
      choiceB = Button(interface2, Point(580, 320), 100, 50, "B")
      choiceB.activate()
      choiceC = Button(interface2, Point(740, 320), 100, 50, "C")
      choiceC.activate()
      choiceD = Button(interface2, Point(900, 320), 100, 50, "D")
      choiceD.activate()
      exit = Button(interface2, Point(50, 450), 100, 100, "退出游戏")
      exit.activate()
      timetext = Text(Point(175, 120), "1")
      jltext = Text(Point(185, 180), "")
      iqtext = Text(Point(185, 200), "")
      eqtext = Text(Point(185, 240), "")
      hptext = Text(Point(185,280),"")
      mltext = Text(Point(185, 320), "")
      course1text = Text(Point(400,380),"高等代数")
      course2text = Text(Point(400, 380), "高等代数")
      course3text = Text(Point(400, 380), "高等代数")
      course1text.draw(interface2)
      course2text.draw(interface2)
      course3text.draw(interface2)
      timetext.draw(interface2)
      jltext.draw(interface2)
      iqtext.draw(interface2)
      eqtext.draw(interface2)
      hptext.draw(interface2)
      mltext.draw(interface2)
      choice = Text(Point(675, 50), "")
      choice.draw(interface2)
      print('end')
      
      #更新数据
      #回合数
      def changetime(time):
            timetext.setText(time)
      #精力
      def changejl(jl):
            jltext.setText(jl)
      #iq
      def changeiq(iq):
            iqtext.setText(iq)
      #eq
      def changeeq(eq):
            eqtext.setText(eq)
      #体魄
      def changehp(hp):
            hptext.setText(hp)
      #魅力
      def changeml(ml):
            mltext.setText(ml)

          
      #判断ABCD按钮
      def click(value):
            pt = interface2.getMouse()
            while not exit.clicked(pt):
                  if choiceA.clicked(pt):
                     value = "A"
                     choice.setText("A")
                  elif choiceB.clicked(pt):
                     value = "B"
                     choice.setText("B")
                  elif choiceC.clicked(pt):
                     value = "C"
                     choice.setText("C")
                  elif choiceD.clicked(pt):
                     value = "D"
                     choice.setText("D")
                  return value
            else:
                  interface2.close()

      #显示数值
      def show(jl,iq,eq,hp,ml,time):
          changejl(jl)
          changeiq(iq)
          changeeq(eq)
          changehp(hp)
          changeml(ml)
          changetime(time)

      #正式循环
      show(character.jl,character.iq,character.eq,character.hp,character.ml,time)
      while time != 9:
            Text1.setText("请选择四种消耗精力值的大学活动：A 修习课程 B：随机事件 C：约会 D：摆烂")
            while character.jl != 0:
                  choice1 = click(0)#按钮——选择行动
                  if choice1 == "A":
                        Text1.setText("请选择要花精力修习的课程类型: A:加智商  B:加情商  C:加体魄  D:加魅力")
                        Text2.setText("")
                        Text3.setText("")
                        Text4.setText("")
                        cour1 = {"A": "线性代数", "B": "政治经济学", "C": "拳击格斗", "D": "古典音乐鉴赏"}
                        cour2 = {"A": "经济学原理", "B": "UTJS", "C": "中国近代史纲要", "D": "高等数学"}
                        cour3 = {"A": "中级微观经济学", "B": "工程体验与创新", "C": "养生太极拳", "D": "摄影艺术"}
                        cour4 = {"A": "回归分析", "B": "计量经济学", "C": "划龙舟", "D": "游戏哲学"}
                        cour5 = {"A": "博弈论", "B": "公共经济学", "C": "棒球", "D": "性别、亲密关系与社会"}
                        cour6 = {"A": "泛函分析", "B": "行为经济学", "C": "网球", "D": "论文选题"}
                        cour7 = {"A": "写论文！", "B": "还是写论文！", "C": "实习", "D": "实习"}
                        cour8 = {"A": "论文还没写完？", "B": "快滚去写论文！", "C": "实习", "D": "实习"}
                        course = [cour1, cour2, cour3, cour4, cour5, cour6, cour7, cour8]
                        xz = {"A": "智商", "B": "情商", "C": "体魄", "D": "魅力"}
                        choice2 = click(0)#按钮——选择课程

                        #根据课程增加属性
                        if choice2 == "A":
                              Text2.setText("你学习了 {}".format(course[time - 1]["A"]))
                              character.learn(course[time - 1]["A"])
                              inc = 5 + random.randint(0, 3)
                              Text3.setText("你的 {} 加 {}".format(xz["A"], inc))
                              character.iq += inc
                              changeiq(character.iq)
                              dec = 1 + random.randint(0, 2)
                              Text4.setText("你的 {} 减 {}".format(xz["C"], inc))
                              character.hp += inc
                              changehp(character.hp)
                              
                        elif choice2 == "B":
                              Text2.setText("你学习了 {}".format(course[time - 1]["B"]))
                              character.learn(course[time - 1]["B"])
                              inc = 3 + random.randint(0, 3)
                              Text3.setText("你的 {} 加 {}".format(xz["B"], inc))
                              character.eq += inc
                              changeeq(character.eq)
                              Text4.setText("你的 {} 加 {}".format(xz["D"], inc))
                              character.ml += inc
                              changeml(character.ml)
                              
                        elif choice2 == "C":
                              Text2.setText("你学习了 {}".format(course[time-1]["C"]))
                              character.learn(course[time-1]["C"])
                              inc = 3 + random.randint(0, 3)
                              Text3.setText("你的 {} 加 {}".format(xz["C"], inc))
                              character.hp += inc
                              changehp(character.hp)
                              Text4.setText("你的 {} 减 {}".format(xz["D"], inc))
                              character.ml += inc
                              changeml(character.ml)
                        elif choice2 == "D":
                              Text2.setText("你学习了 {}".format(course[time-1]["D"]))
                              character.learn(course[time-1]["D"])
                              inc = 5 + random.randint(0, 5)
                              Text3.setText("你的 {} 加 {}".format(xz["D"], inc))
                              character.ml += inc
                              changeml(character.ml)
                              dec = 1 + random.randint(0, 2)
                              Text4.setText("你的 {} 减 {}".format(xz["B"], dec))
                              character.eq -= dec
                              changeeq(character.eq)
                  
                  elif  choice1 == "B":
                        Text1.setText("请选择随机事件类型: A：智商 B：情商 C：体魄 D：魅力")
                        Text2.setText("")
                        Text3.setText("")
                        Text4.setText("")
                        course = {"A": "智商", "B": "情商", "C": "体魄", "D": "魅力"}
                        choice2 = click(0)#按钮——选择随机事件
                        
                        #根据事件增加属性
                        if choice2 == "A":
                              movement = random_events.random_zhishang(character.iq,character.jl)
                              Text2.setText(movement[2])
                              Text3.setText(movement[3])
                              Text4.setText(movement[4])
                              character.iq = movement[0]
                              character.jl = movement[1]
                              changeiq(character.iq)
                              changejl(character.jl)
                              
                        elif choice2 == "B":
                              movement = random_events.random_qingshang(character.eq, character.ml)
                              Text2.setText(movement[2])
                              Text3.setText(movement[3])
                              Text4.setText(movement[4])
                              character.eq = movement[0]
                              character.ml = movement[1]
                              changeeq(character.eq)
                              changeml(character.ml)
                              
                        elif choice2 == "C":
                              movement = random_events.random_tipo(character.hp,character.iq)
                              Text2.setText(movement[2])
                              Text3.setText(movement[3])
                              Text4.setText(movement[4])
                              character.hp = movement[0]
                              character.iq = movement[1]
                              changehp(character.hp)
                              changeiq(character.iq)
                              
                        elif choice2 == "D":
                              movement = random_events.random_meili(character.eq, character.ml)
                              Text2.setText(movement[2])
                              Text3.setText(movement[3])
                              Text4.setText(movement[4])
                              character.eq = movement[0]
                              character.ml = movement[1]
                              changeeq(character.eq)
                              changeml(character.ml)

                  character.jl =character.jl - 1
                  changejl(character.jl)
            else:
                  time += 1
                  changetime(time)
                  character.jl += 10
      else:
            Text1.setText("你的大学生活结束了")
            Text2.setText("你的大学生活结束了")
            Text3.setText("你的大学生活结束了")
            Text4.setText("你的大学生活结束了")


                  
                        


interaction1()
interaction2()
print('show')
show(character.jl, character.iq, character.eq, character.shp, character.ml, time)








