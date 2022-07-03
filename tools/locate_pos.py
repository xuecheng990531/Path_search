from math import radians, cos, sin, asin, sqrt
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
    pos_new=[]
    # if pos[0]>90 or pos[0]<-90:
    #     pos_new.append(pos[1])
    #     pos_new.append(pos[0])
    #     lat1=pos_new[0]
    #     lon1=pos_new[1]
    # else:
    #     pos_new.append(pos[0])
    #     pos_new.append(pos[1])
    #     lat1=pos_new[0]
    #     lon1=pos_new[1]
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

# if __name__=='__main__':
#     filename='/Users/lixuecheng/Desktop/good/file/filename.csv'
#     list=['1','4','2','8']
#     pos=36.02361176,120.1793559
#     #csv_len=get_csv_length(filename)
#     index=get_pos(filename,pos)
#     print(index)
