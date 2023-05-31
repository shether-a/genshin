import random
import time,os
import pandas as pd
global star
star=0
def once(uid,flag2):
    role = []
    random.seed(time.perf_counter())
    # init_user_info(uid)
    if uid=='3':
        id=random.randint(30,42)
        role.append(id)
        if id<33:
            role.append('a')#弓箭
        elif id<36 and id>32:
            role.append('b')#法器
        elif id==36:
            role.append('c')#长枪
        elif id==37:
            role.append('d')#大剑
        else:
            role.append('e')#单手剑
        star=3
        role.append(star)
    elif uid=='40':
        lis=[43,44,45,46,47,48,49,401,402,403,404,405,406,407,408]
        id=random.choice(lis)
        role.append(id)
        if id<46:
            role.append('a')
        elif id>46 and id<50:
            role.append('b')
        elif id>400 and id<403:
            role.append('c')
        elif id>402 and id<406:
            role.append('d')
        else:
            role.append('e')
        star=4
        role.append(star)
    elif uid=='41':
        t=random.randint(0,1)
        if t==0:
            id=random.randint(410,412)
            role.append(id)
            if id==410:
                role.append('lei')
            elif id==411:
                role.append('shui')
            else:
                role.append('yan')
        else:
            id=random.randint(413,429)
            role.append(id)
            if id==413 or id==414:
                role.append('feng')
            elif id==415 or id==416 or id==417:
                role.append('yan')
            elif id>417 and id<421:
                role.append('lei')
            elif id==421:
                role.append('shui')
            elif id>421 and id<427:
                role.append('huo')
            else:
                role.append('bing')
        star = 4
        role.append(star)
    elif uid==50:
        if flag2==0:
            id=511
            role.append(id)
            role.append('huo')
        else:
            id=512
            role.append(id)
            role.append('shui')
        star=5
        role.append(star)
    else:
        id=random.randint(501,506)
        role.append(id)
        if id==501:
            role.append('cao')
        elif id==502:
            role.append('bing')
        elif id==503:
            role.append('feng')
        elif id==504:
            role.append('huo')
        elif id==505:
            role.append('shui')
        else:
            role.append('lei')
        star = 5
        role.append(star)
    # pool_str = get_pool_type(gacha_data.gacha_type)
    # #pool_str = get_pool_type(gacha_data['gacha_type'])
    # # 判定星级
    # rank = get_rank(uid, pool_str)
    # # 是否为up
    # if rank != 3:
    #     is_up = is_Up(uid, rank, pool_str)
    # user_info[uid]["gacha_list"]["wish_total"] += 1
    # if rank == 3:
    #     role = random.choice(gacha_data['r3_prob_list'])
    #     user_info[uid]["gacha_list"][("gacha_4_%s" % pool_str)] += 1
    #     user_info[uid]["gacha_list"][("gacha_5_%s" % pool_str)] += 1
    #     role['count'] = 1
    # else:
    #     if is_up:
    #         role = random.choice(gacha_data['r%s_up_items' % rank])
    #         user_info[uid]["gacha_list"]["wish_%s_up" % rank] += 1
    #         role['rank'] = rank
    #     else:
    #         role = random.choice(gacha_data['r%s_prob_list' % rank])
    #     if rank == 4:
    #         user_info[uid]["gacha_list"][("gacha_5_%s" % pool_str)] += 1
    #     elif rank == 5:
    #         user_info[uid]["gacha_list"][("gacha_4_%s" % pool_str)] += 1
    #     user_info[uid]["gacha_list"]["wish_%s" % rank] += 1
    #     if gacha_data.gacha_type != 200:
    #     #if gacha_data['gacha_type'] != 200:
    #         user_info[uid]["gacha_list"][("is_up_%s_%s"%(rank,pool_str))] = not is_up
    #     if role.item_type == '角色':
    #     #if role['item_type'] == '角色':
    #         itemname = 'role'
    #     else:
    #         itemname = 'weapon'
    #     if role.item_name not in user_info[uid]["role_list"]:
    #         user_info[uid]["%s_list" % itemname][role.item_name] = {}
    #         user_info[uid]["%s_list" % itemname][role.item_name]['数量'] = 1
    #         user_info[uid]["%s_list" % itemname][role.item_name]['出货'] = []
    #         if rank == 5:
    #             user_info[uid]["%s_list" % itemname][role.item_name]['星级'] = '★★★★★'
    #             user_info[uid]["%s_list" % itemname][role.item_name]['出货'].append((user_info[uid]['gacha_list']['gacha_%s_%s' % (rank,pool_str)] + 1))
    #         else:
    #             user_info[uid]["%s_list" % itemname][role.item_name]['星级'] = '★★★★'
    #     else:
    #         user_info[uid]["%s_list" % itemname][role.item_name]['数量'] += 1
    #         if rank == 5:
    #             user_info[uid]["%s_list" % itemname][role.item_name]['出货'].append((user_info[uid]['gacha_list']['gacha_%s_%s' % (rank,pool_str)] + 1))
    #     role['count'] = user_info[uid]["gacha_list"]["gacha_%s_%s" % (rank,pool_str)] + 1
    #     user_info[uid]["gacha_list"]["gacha_%s_%s" % (rank,pool_str)] = 0
    # save_user_info()
    return role