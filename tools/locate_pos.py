from geopy.distance import geodesic
import csv
import pandas as pd
from haversine import haversine

# 获取对应索引位置上的经纬度坐标
def get_lat_lon(list,pos_filename):
    position=[[]for i in range(len(list))]
    pos_file = pd.read_csv(pos_filename,header=None)
    for index in range(len(list)):
    # 读取对应的pos文件
        # 获取对应index的经纬度
        lat=(pos_file.loc[int(list[index])-1][1])
        lon=(pos_file.loc[int(list[index])-1][2])
        # 将经纬度添加到list里面
        position[index].append(lon)
        position[index].append(lat)

    return position

# 获得最小距离的点名字
def get_pos(filename,lat1,lon1):
    result=[]
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for i  in reader:
            #计算两个坐标直线距离
            lat2=i[1]
            lon2=i[2]

            distance_result=geodesic((lat1,lon1), (lat2,lon2))
            result.append(distance_result)

        result=result.index(min(result))+1
        return int(result)


