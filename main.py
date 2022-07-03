from tools.locate_pos import get_lat_lon,get_pos
from tools.node import *
from fastapi import FastAPI,Query,applications
from typing import List,Optional
import uvicorn
from fastapi.openapi.docs import get_swagger_ui_html
def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui-bundle.js',
        swagger_css_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui.css'
    )

applications.get_swagger_ui_html = swagger_monkey_patch



app=FastAPI(title='get position')


def BFS(adj, src, dest, v, pred, dist):
	queue = []
	visited = [False for i in range(v)];
	for i in range(v):

		dist[i] = 1000000
		pred[i] = -1;

	visited[src] = True;
	dist[src] = 0;
	queue.append(src);

	while (len(queue) != 0):
		u = queue[0];
		queue.pop(0);
		for i in range(len(adj[u])):

			if (visited[adj[u][i]] == False):
				visited[adj[u][i]] = True;
				dist[adj[u][i]] = dist[u] + 1;
				pred[adj[u][i]] = u;
				queue.append(adj[u][i]);

				if (adj[u][i] == dest):
					return True;

	return False;

def get_real_position(lat1,lon1, lat2,lon2):
	v=3000
	filename='file/filename.csv'
	# 对坐标进行更新，使其匹配到对应的坐标上
	s=get_pos(filename, lat1,lon1)
	dest=get_pos(filename, lat2,lon2)


	pred=[0 for i in range(v)]
	dist=[0 for i in range(v)]

	if (BFS(adj, s, dest, v, pred, dist) == False):
		print("processing the position")

	# vector path stores the shortest path
	path = []
	crawl = dest;
	crawl = dest;
	path.append(crawl);
	index=[]

	while (pred[crawl] != -1):
		path.append(pred[crawl]);
		crawl = pred[crawl];
	for i in range(len(path)-1, -1, -1):
		# print(path[i], end=' ')
		index.append(path[i])
	
	return index

@app.get('/main')
async def final(point: Optional[List] = Query([]),car_id:Optional[str]=Query([])):

	filename='file/filename.csv'
	index=[]
	for n_pos in range(len(point)-1):
		if 35.986792<float(point[n_pos].split(',')[1][:-1])<36.035571 and 120.172152<float(point[n_pos].split(',')[0][1:])<120.226063:
			s=point[n_pos]
			dest=point[n_pos+1]

			s_lng=s.split(',')[0].replace('[','')
			s_lat=s.split(',')[1].replace(']','')
			s=s_lat,s_lng

			dest_lng = dest.split(',')[0].replace('[', '')
			dest_lat = dest.split(',')[1].replace(']', '')
			dest = dest_lat, dest_lng

			index_part=get_real_position(s_lat,s_lng, dest_lat,dest_lng)

			index.append(index_part)
		else:
			return{
				"坐标错误信息":
				"上传的坐标中有坐标超过限定的电子围栏,维度限定范围为35.986792-36.035571,经度限定范围为120.172152-120.226063。请确保上传的坐标经纬度在其范围内！"
				}

		merge=sum(index,[])
		# 删除列表中多余的元素
		index_final=[]
		for i in merge:
			if i not in index_final:
				index_final.append(i)

		result=get_lat_lon(index_final,pos_filename=filename)

		information={
			"ID":car_id,
			"LENGTH":len(car_id)
		}
		geometry={
			"type": "MultiLineString",
			"coordinates":result

		}
	return {"property":information,"geometry":geometry}


if __name__=='__main__':
	uvicorn.run(app='main:app', host="114.215.85.130", port=8023, reload=True, debug=True)
