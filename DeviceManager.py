#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?

第一步：请求货架的配置信息
第二步：启动货架设备
"""

import LogUtil
import Runthread
import RequestShelf
import WeightShelf
import threading
import math

# todo 货架ID
SHELF_CODE = "12345"

shelfConfigureInfo = None
weightScene = None
weightData = None

isStop = False

# todo 获取货架的配置信息
def getShelfConfigure():
    print("获取货架的配置信息#", SHELF_CODE)

    global shelfConfigureInfo
    shelfConfigureInfo = RequestShelf.getShelfConfigure(SHELF_CODE)
    print("getShelfConfigure#", shelfConfigureInfo)


# todo 更新货架的商品信息
def updateShelfConfigure(weightInfo):
    print("更新货架的商品信息#", weightInfo)
    # RequestShelf.updateMotion(weightInfo)
    thread = threading.Thread(target=RequestShelf.updateMotion, args=(weightInfo,))
    thread.start()


def startDevice(scene):
    LogUtil.d("**************** 货架开始启动 ****************")
    print("startDevice#")
    global weightScene
    weightScene = scene

    # 请求配置信息
    shelfThread = threading.Thread(name="Shelf-Configure", target=getShelfConfigure)
    shelfThread.start()

    # 启动称重设备
    weightThread = threading.Thread(name="Weight-Device", target=WeightShelf.startApp)
    weightThread.start()


# todo 根据货架配置信息，查看当前位置的商品数量
def getItemInfo(group, item):
    index = -1
    for i in range(0, len(shelfConfigureInfo)):
        itemInfo = shelfConfigureInfo[i]

        # 就是找到了
        if itemInfo["code"] == item:
            index = i
            break
        else:
            index = -1

    return index


def compareGoods(newWeights, oldWeights):
    flag = False
    print(newWeights)
    print(oldWeights)
    for i in range(1, len(newWeights) + 1):
        key = str(i)
        value = oldWeights[key] - newWeights[key]
        if oldWeights[key] != 0 or newWeights[key] != 0:
            text = "称号#{0} 原重：{1}g 现重：{2}g".format(key, oldWeights[key], newWeights[key])
            print(text)

        # 差值必须不等于0，并且|value| > 5差值大于5
        if value != 0 and math.fabs(value) > 5:
            flag = True
            text = "************** 有变更重量 ******** 称号#{0} 原重：{1}g 现重：{2}g".format(key, oldWeights[key], newWeights[key])
            print(text)
            # todo 根据货架配置信息，查看当前位置的商品数量

    return flag


def compareGoodsWeight(newWeights, oldWeights):
    flag = False
    itemInfo = None
    if not oldWeights or not newWeights:
        return flag, itemInfo

    print("现在货架信息#", newWeights)
    print("原来货架信息#", oldWeights)
    for i in range(0, len(newWeights)):

        currentWeights = newWeights[i]
        originalWeights = oldWeights[i]

        # 1~16称重单元AD模块是否正常的标志位，0为对应称重单元重量不在线，1为在线
        if currentWeights["status"] == 0:
            print("第{0}组不在线{1}".format(i + 1, currentWeights["status"]))
            continue

        # 1~16称重单元AD模块是否正常的标志位，0为故障不稳定，1为正常稳定
        if currentWeights["stable"] == 0:
            print("第{0}组不在线{1}".format(i + 1, currentWeights["stable"]))
            continue

        # 每一组的称量单位
        for j in range(0, 16):
            key = str(i * 16 + j + 1)
            value = originalWeights[key] - currentWeights[key]
            if originalWeights[key] != 0 or currentWeights[key] != 0 :
                text = "称号#{0} 原重：{1}g 现重：{2}g".format(key, originalWeights[key], currentWeights[key])
                print(text)

            # 差值必须不等于0，并且|value| > 30差值大于30
            if value != 0 and math.fabs(value) > 30 and currentWeights[key] < 65530:
                flag = True
                text = "************** 有变更重量 ******** 称号#{0} 原重：{1}g 现重：{2}g".format(key, originalWeights[key],
                                                                                     currentWeights[key])
                print(text)
                # todo 根据货架配置信息，查看当前位置的商品数量
                global shelfConfigureInfo
                index = getItemInfo(i + 1, j + 1)
                itemInfo = shelfConfigureInfo[index]
                item_weight = itemInfo["item_weight"]
                # 现在的个数
                current_count = currentWeights[key] / float(item_weight)
                original_count = originalWeights[key] / float(item_weight)
                current_count = int(round(current_count))
                original_count = int(round(original_count))
                print("商品信息#",  itemInfo)

                # 0拿起商品 1放下商品
                if current_count > original_count:
                    itemInfo["motion"] = 1
                else:
                    itemInfo["motion"] = 0

                count = itemInfo["quantity"]
                count += current_count - original_count

                if count < 0:
                    count = 0
                itemInfo["quantity"] = count
                print("现在商品个数#{0} 原来商品个数#{1} 现后台数量#{2}".format(current_count, original_count, count))

                # todo 上传货架的变更信息
                updateShelfConfigure(itemInfo)

    return flag, itemInfo


# 称的重量信息
def updateWeightInfo(weightInfo64, weightInfo128):
    data = weightInfo64 + weightInfo128
    print("updateWeightInfo#", len(data))
    LogUtil.d(data)

    # 有变化就更新UI
    if not shelfConfigureInfo:
        print("************* 无法获取货架配置信息 ********")
        # 请求配置信息
        shelfThread = threading.Thread(name="Shelf-Configure", target=getShelfConfigure)
        shelfThread.start()
        return
    global weightData
    global weightScene
    if not weightData:
        weightData = data

    flag, itemInfo = compareGoodsWeight(data, weightData)

    if flag:
        weightData = data
        # todo 更新UI，显示识别结果
        thread = Runthread.Runthread()
        thread.setRequest(itemInfo)
        thread._signal.connect(weightScene.updateScene)
        thread.start()


if __name__ == "__main__":
    print("Hello World")