import random

def random_zhishang(iq,jl):
    events1 = {
        "知识竞赛":0.25,
        "期中来临":0.25,
        "中期大创":0.25，
        "难题深究":0.25,
    }

    event1 = random.choices(list(events1.keys()), list(events1.values()), k=1)[0]
    
    if event1 == "知识竞赛":
        iq = iq + 3
        t1 = "在学期中，你积极参加了学院组织的知识竞赛，凭借充足的知识储备和勤奋的学习备战，你成功夺得了第一名的桂冠。")
        t2 = "智力加 3 目前智力为 "
        t3 = None
    elif event1 == "期中考试":
        iq = iq + 3
        t2 = "智力加 3 目前智力为 "
        if jl <= 2 and 
        if (iq / random.randint(10,40)) >= 1:
            t1 = '
    
    elif event1 == "中期大创":
        iq = iq + 2
        t1 = "在学期中，你参加了大创，通过和老师同学们的合作，你顺利完成了任务，也学到了很多知识。"
        t2 = "智力加 2 目前智力为 "
        t3 = None
    elif event1 == "难题深究":
        iq = iq + 1
        t1 = "做作业时，你遇到了一道难题，虽然耗费了很多时间，但最终解决了它，你很满意。"
        t2 = "智力加 1 目前智力为 "
        t3 = None
    return iq, jl, t1, t2, t3
    
def random_qingshang(eq,ml):
    events2 = {
        "室友分手":0.25,
        "班级事务":0.25,
        "投递实习":0.25,
        "院级联谊":0.25,
    }

    event2 = random.choices(list(events2.keys()), list(events2.values()), k=1)[0]

    print("随机事件： ", event2)
    if event2 == "室友分手":
        qs_shiyou(eq)
    if event2 == "班级事务":
        qs_banji(eq)
    if event2 == "投递实习":
        qs_shixi(eq)
    if event2 == "院级联谊":
        qs_lianyi(eq,ml)

def random_tipo(tp):
    events3 = {
        "校运会":0.25,
        "伤风寒":0.25,
        "刷跑时间":0.25,
        "每日撸铁":0.25,
    }

    event3 = random.choices(list(events3.keys()), list(events3.values()), k=1)[0]

    print("随机事件： ", event3)
    if event3 == "校运会":
        tp_xiaoyun(tp)
    if event3 == "伤风寒":
        tp_fenghan(tp)
    if event3 == "刷跑时间":
        tp_shuapao(tp)
    if event3 == "每日撸铁":
        tp_lutie(tp)

def random_meili(eq,ml):
    events4 = {
        "院级联谊":0.25,
        "歌手大赛":0.25,
        "表白墙":0.25,
        "网友面基":0.25,
    }

    event4 = random.choices(list(events4.keys()), list(events4.values()), k=1)[0]

    print("随机事件： ", event4)
    if event4 == "院级联谊":
        qs_lianyi(eq,ml)
    if event4 == "歌手大赛":
        ml_geshou(ml)
    if event4 == "表白墙":
        ml_biaobai(ml)
    if event4 == "网友面基":
        ml_wangyou(ml)



def qs_shiyou(eq):
    eq = eq + 1
    print("你的室友失恋了，你看着他失魂落魄的样子，决定帮他一把。在你的劝说宽慰下，室友终于走出了失恋的阴影，得以继续正常的学习和生活。")
    print("情商加 2 目前情商为 ",eq)

def qs_banji(eq):
    eq = eq + 3
    print("班级团日活动，你作为班干部为活动出谋划策，与各位同学联系，取得了满意的成果。")
    print("情商加 3 目前情商为 ",eq)

def qs_shixi(eq):
    eq = eq + 2
    print("你打算接下来的假期前往公司实习，并因此准备了简历和面试。面对HR，你侃侃而谈，展现了优秀的综合素养。")
    print("情商加 2 目前情商为 ",eq)

def qs_lianyi(eq,ml):
    eq = eq + 2
    ml = ml + 2
    print("学期中段，你所在的学院与其他学院举行了联谊活动。作为社交达人，你理所当然地在联谊晚会上表演了节目，赢得了阵阵喝彩。")
    print("联谊结束后，你的微信收到了很多人的好友申请，你与他们交谈甚欢。")
    print("情商加 2 目前情商为 ",eq)
    print("魅力加 2 目前魅力为 ",ml)

def tp_xiaoyun(tp):
    tp = tp + 3
    print("学校举办了校运会，你积极参加，虽然名次没有很高，但在准备校运会的过程中，你得到了身体与意志的锻炼。")
    print("体魄加 3 目前体魄为 ",tp)

def tp_fenghan(tp):
    tp = tp - 1
    print("或许是不适应骤变的天气，你得了风寒，不得不在宿舍养病。几天后你康复了，但感觉自己比以前虚了不少。")
    print("体魄减 1 目前体魄为 ",tp)

def tp_shuapao(tp):
    print("校园跑即将截止，你还有将近一半路程没有完成，你选择： ")
    print("A 每天跑圈 坚持锻炼")
    print("B 骑上单车 享受凉风")
    if :
        tp = tp + 1
        print("体魄加 1 目前体魄为 ", tp)
    else :
        tp = tp - 1
        print("体魄减 1 目前体魄为 ", tp)

def tp_lutie(tp):
    tp = tp + 2
    print("最近你迷上了健身，天天泡在健身房享受撸铁的快乐，那挥洒汗水的滋味让你难以拒绝。")
    print("体魄加 2 目前体魄为 ",tp)

def ml_geshou(ml):
    ml = ml + 2
    print("天赋的音色和持续的训练，让你在歌手大赛的舞台上一鸣惊人，闯入十佳。你对歌曲传神的演绎，让众多观众为之着迷。")
    print("魅力加 2 目前魅力为 ",ml)

def ml_biaobai(ml):
    ml = ml + 3
    print("某天晚上，刷手机的你突然发现自己的名字出现在了十点物语中，有人在表白墙上抒发了对你的爱慕之情。面对室友们的起哄，你却邪魅一笑，摆摆手，深藏功与名。")
    print("魅力加 3 目前魅力为 ",ml)

def ml_wangyou(ml):
    ml = ml - 2
    print("今天你很激动，因为你要和聊了很久的网友见面了！你们虽然都在交大，但却未曾见过面，只是一个偶然的机会让你们互加了微信。")
    print("初次见面，见到她害羞的样子，你也有些不知所措。两个人你看我我看你，气氛尬到了冰点。")
    print("魅力减 2 目前魅力为 ",ml)

def random_events(iq,eq,tp,ml):
# 定义事件字典，键为事件名称，值为该事件出现的概率
    events = {
        "智商": 0.25,
        "情商": 0.25,
        "体魄": 0.25,
        "魅力": 0.25,

    }

    # 随机选择一个事件
    event = random.choices(list(events.keys()), list(events.values()), k=1)[0]

    if event == "智商":
        random_zhishang(iq)
    if event == "情商":
        random_qingshang(eq,ml)
    if event == "体魄":
        random_tipo(tp)
    if event == "魅力":
        random_meili(eq,ml)

