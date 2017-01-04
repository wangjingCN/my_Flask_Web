# -*- coding:gb2312 -*-
names = locals()
menuData = [
    {"id": 0, "parent_id": -1, "sectionName": u"一键变更", "sectionURL": " ", "menu_level": 1},
    {"id": 1, "parent_id": 0, "sectionName": u"服务变更", "sectionURL": " ", "menu_level": 2},
    {"id": 2, "parent_id": 1, "sectionName": u"服务上线", "sectionURL": " www.baidu.com/fuwu/shangxian", "menu_level": 3},
    {"id": 3, "parent_id": 1, "sectionName": u"服务检查", "sectionURL": " www.baidu.com/wufu/jiancha", "menu_level": 3},
    {"id": 4, "parent_id": 1, "sectionName": u"服务执行", "sectionURL": " www.baidu.com/fuwu/zhixing", "menu_level": 3},
    {"id": 5, "parent_id": 0, "sectionName": u"域名变更", "sectionURL": " ", "menu_level": 2},
    {"id": 6, "parent_id": 5, "sectionName": u"域名上线", "sectionURL": "wwww.baidu.com/yuming/shagnxian ",
     "menu_level": 3},
    {"id": 7, "parent_id": 5, "sectionName": u"域名检查", "sectionURL": "wwww.baidu.com/yuming/jiancha ", "menu_level": 3},
    {"id": 8, "parent_id": 5, "sectionName": u"域名执行", "sectionURL": "wwww.baidu.com/yuming/zhixing ", "menu_level": 3},
    {"id": 9, "parent_id": -1, "sectionName": u"一键应急", "sectionURL": " ", "menu_level": 1},
    {"id": 91, "parent_id": 9, "sectionName": u"拒绝地址公鸡", "sectionURL": "www.baidu.cm ", "menu_level": 2}
]


def get_menu_data_old(menu_data):
    first_level = []
    second_level = []
    thrid_level = []
    for dataStr in menu_data:
        if dataStr['menu_level'] == 1:
            first_level.append(dataStr)
        if dataStr['menu_level'] == 2:
            second_level.append(dataStr)
        if dataStr['menu_level'] == 3:
            thrid_level.append(dataStr)
    return first_level, second_level, thrid_level


def get_menu_data(menu_data):
    first_level = []
    second_level = []
    thrid_level = []
    for dataStr in menu_data:
        if dataStr['parent_id'] == -1:
            first_level.append(dataStr)
    for dataStr in menu_data:
        if dataStr['parent_id'] != -1:
            second = False
            for first_level_item in first_level:
                if dataStr['parent_id'] == first_level_item['id']:
                    second = True
            if second:
                second_level.append(dataStr)
            else:
                thrid_level.append(dataStr)
    return first_level, second_level, thrid_level


def get_menu_data_new(menu_data):
    # level_num = sorted(menu_data, key=lambda k: (k['menu_level']), reverse=True)[0]['menu_level']
    level_num = sorted(menu_data, key=lambda k: (k['menu_level'],k['id']), reverse=True)[0]['menu_level']
    result = []
    for index in range(1, level_num + 1):
        names[str(index) + '_level'] = []
        for dataStr in menu_data:
            if dataStr['menu_level'] == index:
                names[str(index) + '_level'].append(dataStr)
        result.append(names[str(index) + '_level'])
    return result


def get_menu_data_3(result):
    result_list = []
    for index in result[0]:
        item_list = []
        item_list.append(index['id'])
        i = 1
        while i < len(result):
            if i == 1:
                for child in result[i]:
                    if child['parent_id'] == index['id']:
                        item_list.append(child['id'])
            else:
                for child in result[i]:
                    for parent in result[i - 1]:
                        if child['parent_id'] == parent['id']:
                            item_list.append(child['id'])
            i = i + 1
        result_list.append(item_list)
    return result_list

level_num = sorted(menuData, key=lambda k: (k['menu_level'],k['id']), reverse=True)
print level_num