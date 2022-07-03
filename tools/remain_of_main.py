# @app.post('/search')
def printShortestDistance(s, dest):
	v=3000
	filename='/Users/lixuecheng/Desktop/good/file/filename.csv'
	# 对坐标进行更新，使其匹配到对应的坐标上
	s=get_pos(filename, s)
	dest=get_pos(filename, dest)


	pred=[0 for i in range(v)]
	dist=[0 for i in range(v)]

	if (BFS(adj, s, dest, v, pred, dist) == False):
		print("wrong message","Given source and destination are not connected")

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

	# 获得对应的坐标
	result=get_lat_lon(index,pos_filename=filename)
	return {"路径是":result}

# @app.post('/new')
def new(point):
	v=3000
	filename='/Users/lixuecheng/Desktop/good/file/filename.csv'
	all_path=[]
	for n_pos in range(len(point)-1):

	# 对坐标进行更新，使其匹配到对应的坐标上
		s=point[n_pos]
		dest=point[n_pos+1]

		s=get_pos(filename, s)
		dest=get_pos(filename, dest)

		pred=[0 for i in range(v)]
		dist=[0 for i in range(v)]

		if (BFS(adj, s, dest, v, pred, dist) == False):
			print("wrong message","Given source and destination are not connected")

		else:
			path = []
			crawl = dest;
			crawl = dest;
			path.append(crawl);
			index=[]

			while (pred[crawl] != -1):
				path.append(pred[crawl]);
				crawl = pred[crawl];
			for i in range(len(path)-1, -1, -1):
				index.append(path[i])
		all_path.append(index)
		merge=sum(all_path,[])

		# 删除列表中多余的元素
		index_final=[]
		for i in merge:
			if i not in index_final:
				index_final.append(i)
		# 最短路径
		result=get_lat_lon(index_final,pos_filename=filename)
	return {"index":result}