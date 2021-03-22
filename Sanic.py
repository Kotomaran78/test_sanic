from sanic import Sanic
from sanic.response import json, text


app = Sanic("cats list")


cat_list = []

capital_dict = {
	"россия": "Москва",
	"франция": "Париж",
	"великобритания": "Лондон",
	"сша": "Вашингтон",
	"китай": "Пекин",
}

class Cat(object):

	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def to_json(self):
		return {
			"name": self.name, 
			"age": self.age, 
			"weight": self.weight 
		}


#Добавить кота в список {"name":"..." , "age":"..." , "weight":"..."}
@app.route("create_cat", methods=["POST"])
async def creat_cat(request):
	try:
		data = request.json
		cat  = Cat(data["name"], data["age"], data["weight"]).to_json()
		cat_list.append(cat)
		return json(cat, status = 201)

	except Exception as error:
		print(error)
		return json({"message": "cat creation failes"}, status = 500)

#Посмотреть всех котов в списке
@app.route("get_cats", methods=["GET"])
async def get_cats(request):
	try:
		return json(cat_list, status = 200)

	except Exception as error:
		print(error)
		return json({"message": "getting cats failed"}, status = 500)



# узнать столицу по стране {"country":"..."}
@app.route("capital", methods=["POST"])
async def capital(request):
	try:
		capital = capital_dict[request.json["country"].lower()]
		return text(capital, status = 200)

	except Exception as error:
		print(error)
		return json({"message": "Ошибка обработки запроса"}, status = 500)

# посмотреть весь словарь со странами:столицами
@app.route("capitals_dict", methods=["GET"])
async def capitals_dict(request):
	try:
		return json(capital_dict, status = 200)

	except Exception as error:
		print(error)
		return json({"message": "Ошибка обработки запроса"}, status = 500)



if __name__ == '__main__':
	app.run()