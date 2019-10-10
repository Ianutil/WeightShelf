#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""
import requests
import LogUtil
import json
SERVIER_URL = "http://10.10.100.27:9292"


def updateMotion(weightInfo):
    """
    item_id 商品id
    scale_id 秤id
    member_id 会员id
    picture 摄像头拍摄的照片路径
    motion 0拿起商品 1放下商品
    quantity 拿起或放下商品的数量
    :return:
    """
    url = SERVIER_URL + "/motion"
    data = {"item_id": weightInfo["item_id"],
            "scale_id": weightInfo["id"],
            "shelf_id": weightInfo["shelf_id"],
            "member_id": 1,
            "age": 22,
            "gender": 0,
            "picture": "abc.jpg",
            "motion": weightInfo["motion"],
            "quantity":weightInfo["quantity"]}
    print(url)
    print("请求参数：",data)
    LogUtil.d(url)
    LogUtil.d(data)
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            # print(response.content)
            LogUtil.d(response.content)
            data = json.loads(response.content)
            print("响应结果",data)
    except Exception as e:
        print(e)
        LogUtil.e(e)

    return data

def getShelfConfigure(code):
    url = SERVIER_URL + "/scale?shelf_code={0}".format(code)
    LogUtil.d(url)
    print(url)
    """
    id 秤id
    shelf_id 货架id
    x 秤所在列
    y 秤所在行
    max_weight 秤最大称重
    item_id 商品id
    item_weight 单个商品重量
    quantity 商品数量
    status 秤状态。1启用，0不启用
    :return:
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # print(response.content)
            LogUtil.d(response.content)
            data = json.loads(response.content)
            print("响应结果",data)
    except Exception as e:
        print(e)
        LogUtil.e(e)

    return data

def requestItemInfo(itemCode):
    url = SERVIER_URL + "/item/{0}".format(itemCode)
    LogUtil.d(url)
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # print(response.content)
            LogUtil.d(response.content)
            data = json.loads(response.content)
            print("响应结果", data)
    except Exception as e:
        print(e)
        LogUtil.e(e)
if __name__ == "__main__":
    print("Hello World")
    shelfInfo = getShelfConfigure(12345)

    weightInfo = shelfInfo[0]
    # 0拿起商品 1放下商品
    weightInfo["motion"] = 0
    weightInfo["quantity"] = 0
    data = updateMotion(weightInfo)
    requestItemInfo(4)
