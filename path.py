import uvicorn
from tools.utils import *
from tools.locate_pos import get_lat_lon
from tools.node import *
from fastapi import FastAPI,Query,applications
from typing import List,Optional
from fastapi.openapi.docs import get_swagger_ui_html

def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui-bundle.js',
        swagger_css_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui.css'
    )

applications.get_swagger_ui_html = swagger_monkey_patch

app=FastAPI(title='坐标替换',description='接受两组坐标并返回两组坐标之间剩下的多组坐标')



@app.get('/main',summary='更新坐标',tags=['接口'])
async def final(
	point: Optional[List] = Query([],description='多组位置信息,先经度后维度,如  \n   \n [120.2814547,36.024223496]'),
	car_id:Optional[str]=Query([],description='车辆的ID')
	):

	is_in_area=isin(point)
	if is_in_area!=0:
		index_final=update_pos(is_in_area)
		
		# request body
		information={
			"ID":car_id,
			"LENGTH":len(car_id)
		}
		geometry={
			"type": "MultiLineString",
			"coordinates":index_final
		}

		return {"property":information,"geometry":geometry}
	else:
		return {
			"坐标错误信息":
			"上传的坐标中有坐标超过限定的电子围栏,维度限定范围为35.986792-36.035571,经度限定范围为120.172152-120.226063。"
			}


if __name__=='__main__':
	uvicorn.run(app='path:app', host="114.215.85.130", port=8080, reload=True, debug=True)
