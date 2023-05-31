import math
import re, copy ,json
from pathlib import Path
import pygame
import sys
import base64
# from pgu import gui
from io import BytesIO
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkfilebrowser
import threading
from PIL import Image, PngImagePlugin, ImageDraw, ImageFont
import time,os
import glob
import pandas as pd
from datafill import once
import datetime
from dataprocess import preprocess

# 获得当前时间

import imageio
global ys
global flag#实现线程2的监控
global imagecount
global flag1#播放完动画的标志
global flag2#记录当前选定的up池
global count#记录当前抽数
global dm,new,df

ys=0
flag=1
flag1=1
flag2=0#默认胡桃
count=0
# 设置主窗口
pd.set_option("display.max_colwidth", 300)
pd.set_option('expand_frame_repr',False)
pd.options.display.max_rows=None  # 显示最多行数
pd.options.display.max_columns=None # 显示最多列数
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
cache_item = {}
# assets_dir = Path(__file__) .parent / 'gacha_res'
root=Tk()
root.wm_withdraw()
filename=tkfilebrowser.askopenfilename(initialdir=r'E:/code/genshin/dataset/data')
# if filename=='':
#     print(filename)
print(filename)
# f = open(filename, 'r', encoding='gbk')
# lines = f.readlines()  # 读取全部内容
assets_dir = Path(__file__) .parent /'dataset/10draws'
# 设置窗口标题

#上传文件
new=pd.DataFrame(columns=['时间','名称','类别','星级','总次数'])
dm=pd.read_csv(r'E:/code/genshin/dataset/result/dict.csv',sep=r'\s+',encoding='utf-8',dtype=object)
df=pd.read_csv(r'E:/code/genshin/dataset/transfer.csv',sep=r'\s+',encoding='utf-8',dtype=object)
#开始预测
#弹出提示，正在分析
cache_img = {}
def rank_icon(rank):
    return get_assets('%s_star.png' % str(rank))
def demo1():
    print("2")
    time.sleep(1)
    print("3")

def demo2():
    while flag:
        print(1)
        preprocess(filename)
    # image_surface.fill((0, 0, 255), rect=(100, 100, 100, 50), special_flags=0)
    # image_surface.scroll(100, 60)  # 移动图片
def item_bg(rank):
    return get_assets('%s_background.png' % str(rank)).resize((143, 845))
def get_assets(path) -> PngImagePlugin.PngImageFile:
    base_path = assets_dir
    cache = cache_img.get(path)
    if cache:
        return copy.deepcopy(cache)
    else:
        cache_img[path] = Image.open(str(base_path/path)).convert("RGBA")
    return get_assets(path)

def create_item(rank, item_type, name):
    if item_type == 'a' or item_type == 'b' or item_type == 'c' or item_type == 'd' or item_type == 'e':
        item_type1='武器'
    else:
        item_type1='角色'
    bg = item_bg(rank)
    item_img = get_assets(Path(item_type1) / (str(name) + '.png'))
    rank_img = rank_icon(rank).resize((119, 30))
    if item_type1 == '角色':
        item_img = item_img.resize((item_img.size[0] + 12, item_img.size[1] + 45))
        item_img.alpha_composite(rank_img, (4, 510))

        item_type_icon = get_assets(Path('元素') / (item_type + '.png')).resize((80, 80))
        item_img.alpha_composite(item_type_icon, (25, 420))
        bg.alpha_composite(item_img, (3, 125))

    else:
        bg.alpha_composite(item_img, (3, 240))
        bg.alpha_composite(rank_img, (9, 635))
        # item_type_icon = type_json.get(name)
        # if item_type_icon:
        item_type_icon = get_assets(Path('类型') / (item_type + '.png')).resize((100, 100))
        bg.alpha_composite(item_type_icon, (18, 530))
    # if rank == 5:
    #     draw = ImageDraw.Draw(bg)
    #     if len(str(count)) == 2:
    #         draw.text((22,750),('['+str(count)+'抽]'), font=countfont, fill='white')
    #     else:
    #         draw.text((27,750),('['+str(count)+'抽]'), font=countfont, fill='white')
    return bg

def tenimage(dh,flag2,new,dm):
    gacha_list = []
    # curr_time = datetime.datetime.now()
    # time_str = datetime.datetime.strftime(curr_time, '%m-%d %H:%M')
    # dh=dh.sort_values(by='num',ascending=False)
    for i in range(10):
        role = once(dh.iloc[i][0],flag2).copy()
        # gacha_list.append(role)
        nowtime = datetime.datetime.now()
        other_StyleTime = nowtime.strftime("%Y-%m-%d %H:%M:%S")
        # print(role[0])
        n = dm.loc[dm['id'] == str(role[0])]
        # print(n)
        if role[1] == 3 or role[1] == 40:
            ntype = '武器'
        else:
            ntype = '角色'
        s = pd.Series([other_StyleTime, n.iloc[0][1], ntype, role[2], count+1], index=new.columns)
        new = new.append(s, ignore_index=True)
        gacha_list.append(role)
    gacha_list.sort(key=lambda x: x[2], reverse=True)
    # print(gacha_list)
    # print(t1)
    # gacha_list = sorted(d.items(), key=lambda x: x[1], reverse=False)  # 按字典集合中，每一个元组的第二个元素排列。
    # x相当于字典集合中遍历出来的一个元组。
    # print(d_order)  # 得到: [('a', 1), ('b', 2), ('c', 3)]
    # sorted(gacha_list.keys()key=lambda x: x["star"], reverse=True)
    img: PngImagePlugin.PngImageFile
    img = get_assets(r'E:/code/genshin/dataset/10draws/background.png')
    i = 0
    for l in gacha_list:
        i += 1
        rank = l[2]
        item_type = l[1]
        name = l[0]
        # element = wish.get('item_attr') or type_json[name]
        # count = wish['count']
        # print(l)
        i_img = create_item(rank, item_type, name)
        img.alpha_composite(i_img, (105 + (i_img.size[0] * i), 123))
    img.thumbnail((1024, 768))
    img2 = Image.new("RGB", img.size, (255, 255, 255))
    img2.paste(img, mask=img.split()[3])
    # draw = ImageDraw.Draw(img2)
    # draw.text((27, 545), ('@%s %s  Created By CMHopeSunshine' % (str(sd['nickname']), time_str)), font=timefont,
    #           fill="#8E8E8E")
    return img2

def pil2b64(data):
    bio = BytesIO()
    data = data.convert("RGB")
    data.save(bio, format='JPEG', quality=75)
    base64_str = base64.b64encode(bio.getvalue()).decode()
    return 'base64://' + base64_str
pygame.init()
if __name__ == "__main__":
    start = time.time()
    log = open(r'E:/code/genshin/dataset/result/result.csv', mode='w')
    t1 = threading.Thread(target=demo1)
    t2 = threading.Thread(target=demo2)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    # 加载图片
    # 填写原石数
    while ys == 0 or ys > 14400:
        ys = simpledialog.askinteger('原石', '请输入原石数量：不得超过14400')
        if ys == 0 or ys > 14400:
            messagebox.showwarning(title='提示！', message='请重新输入')
    screen = pygame.display.set_mode((1080, 578))
    pygame.display.set_caption('原神抽卡')
    # 加载图片
    image_surface1 = pygame.image.load(r'E:/code/genshin/background2.jpg')
    image_surface = pygame.image.load(r'E:/code/genshin/background1.jpg')
    screen.blit(image_surface, (0, 0))
    flag2=0
    font = pygame.font.SysFont('方正粗黑宋简体', 18)
    # ys = ys.render(ys, True, (255, 255, 255))
    # screen.fill('white')
    # screen.blit(ys, (880, 36.5))
    ys1 = "{}".format(ys)
    ys1 = font.render(ys1, True, (255, 255, 255))
    screen.blit(ys1, (880, 36.5))
    messagebox.showwarning(title='提示！', message='正在加载~')
    t2.start()
    t1.join()
    flag=0
    messagebox.showwarning(title='提示！', message='欢迎使用')
    root.destroy()
    # os.environ['SDL_VIDEO_CENTERED'] = '1'  # 居中显示
    # screen.fill('white')
    df=pd.read_csv(r'E:/code/genshin/dataset/result/test.csv',sep=r'\s+',encoding='utf-8',dtype=object)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(new, file=log)
                pygame.quit()
                sys.exit()
        # 更新屏幕内容
            pygame.display.flip()
            imagecount = 0
            if event.type == pygame.MOUSEBUTTONDOWN and flag1==1:
                # pos 获取鼠标当前位置
                # event.type == pygame.MOUSEBUTTONUP
                print('鼠标按下', event.pos)
                mx, my = event.pos
                if mx > 3 and mx < 125 and my > 180 and my < 237:
                    # image_surface1 = pygame.image.load(r'E:/code/genshin/background2.jpg')
                    # 处理完，更新显示
                    screen.blit(image_surface1, (0, 0))
                    flag2=1
                    ys1 = "{}".format(ys)
                    ys1 = font.render(ys1, True, (255, 255, 255))
                    screen.blit(ys1, (880, 36.5))
                    pygame.display.flip()
                elif mx > 3 and mx < 125 and my > 86 and my < 147:
                    # image_surface = pygame.image.load(r'E:/code/genshin/background1.jpg')
                    # 处理完，更新显示
                    screen.blit(image_surface, (0, 0))
                    flag2=0
                    ys1 = "{}".format(ys)
                    ys1 = font.render(ys1, True, (255, 255, 255))
                    screen.blit(ys1, (880, 36.5))
                    pygame.display.flip()
                elif mx > 492 and mx < 722 and my > 465 and my < 525:
                    # 单抽
                    if ys<160:
                        font = pygame.font.SysFont('方正粗黑宋简体', 30)
                        # ys = ys.render(ys, True, (255, 255, 255))
                        # screen.fill('white')
                        # screen.blit(ys, (880, 36.5))
                        text = font.render("原石不足", True, (0, 0, 0))
                        screen.blit(text, (870, 46.5))
                        continue
                    ys-=160
                    role=once(df.iloc[count][0],flag2).copy()
                    nowtime = datetime.datetime.now()
                    other_StyleTime = nowtime.strftime("%Y-%m-%d %H:%M:%S")
                    n=dm.loc[dm['id'] == str(role[0])]
                    if role[1]==3 or role[1]==40:
                        ntype='武器'
                    else:
                        ntype = '角色'
                    s = pd.Series([other_StyleTime, n.iloc[0][1], ntype, role[2],count+1], index=new.columns)
                    new = new.append(s, ignore_index=True)
                    count+=1
                    if role[2]==4:
                        dir ='singlepurple'
                    elif role[2]==5:
                        dir='singlegolden'
                    else:
                        dir='singleblue'
                    dir1=str(role[0])
                    filenames = glob.glob('E:/code/genshin/dataset/png/' + dir + '/*')
                    filenames1 = glob.glob('E:/code/genshin/dataset/png/' + dir1 + '/*')
                    # # print(filenames)
                    # filenames.sort(key=os.path.getmtime)
                    # print(filenames)
                    # print(filenames)
                    now=0
                    images=[]
                    imagecount=0
                    for filename in filenames:
                        images.append(pygame.image.load(filename))
                        imagecount+=1
                    print(2)
                    for filename in filenames1:
                        images.append(pygame.image.load(filename))
                        imagecount+=1
                    while now< imagecount-1:
                        # 画面每次刷新更新gif的下一帧
                        now +=0.04
                        screen.blit(images[math.floor(now)],(0,0))
                        pygame.display.flip()
                        event1 = pygame.event.get()
                        # print(event1)
                        # print(len(event1))
                        if len(event1) > 0:
                            if event1[0].type == pygame.MOUSEBUTTONDOWN:
                                print('jump')
                                now = imagecount - 2
                    flag1 = 0
                    continue
                elif mx > 778 and mx < 1007 and my > 465 and my < 525:
                    if ys<1600:
                        font = pygame.font.SysFont('方正粗黑宋简体', 30)
                        # ys = ys.render(ys, True, (255, 255, 255))
                        # screen.fill('white')
                        # screen.blit(ys, (880, 36.5))
                        text = font.render("原石不足", True, (0, 0, 0))
                        screen.blit(text, (870, 46.5))
                        continue
                    ys-=1600
                    images = []
                    dh = df.loc[count:count + 10]
                    print(dh)
                    if any(dh['num'] == '50') or any(dh['num']  == '51'):
                        dir = 'tengolden'
                    else:
                        dir = 'tenpurple'
                    # dir1 = '40'
                    print(dir)
                    filenames = glob.glob('E:/code/genshin/dataset/png/' + dir + '/*')
                    # filenames1 = glob.glob('E:/code/genshin/dataset/png/' + dir1 + '/*')
                    # # print(filenames)
                    # filenames.sort(key=os.path.getmtime)
                    # print(filenames)
                    # print(filenames)
                    now = 0
                    imagecount=0
                    for filename in filenames:
                        images.append(pygame.image.load(filename))
                        imagecount += 1
                    print(2)
                    # for filename in filenames1:
                    #     images.append(pygame.image.load(filename))
                    #     imagecount += 1
                    while now < imagecount - 1:
                        # 画面每次刷新更新gif的下一帧
                        now += 0.04
                        screen.blit(images[math.floor(now)], (0, 0))
                        pygame.display.flip()
                        event1=pygame.event.get()
                        print(event1)
                        # print(len(event1))
                        if len(event1)>0:
                            if event1[0].type==pygame.MOUSEBUTTONDOWN:
                                now=imagecount-2
                        #可以尝试加回车事件跳过
                    image=tenimage(dh,flag2,new,dm)
                    count+=10
                    pil2b64(image)
                    image.save(r'E:/code/genshin/dataset/image.jpg')
                    image_surface2 = pygame.image.load(r'E:/code/genshin/dataset/image.jpg')
                    picture = pygame.transform.scale(image_surface2, (1080, 579))
                    screen.blit(picture, (0, 0))
                    pygame.display.flip()
                    flag1 = 0
                    continue
            if event.type==pygame.MOUSEBUTTONDOWN and flag1==0:
                flag1=1
                print('鼠标按下2', event.pos)
                ys1 = "{}".format(ys)
                ys1 = font.render(ys1, True, (255, 255, 255))
                if flag2==0:
                    screen.blit(image_surface, (0, 0))
                else:
                    screen.blit(image_surface1, (0, 0))
                screen.blit(ys1, (880, 36.5))
                pygame.display.flip()
                continue
