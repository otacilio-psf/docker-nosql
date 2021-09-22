from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
result = client['escola']['alunos'].aggregate([
    {
        '$lookup': {
            'from': 'cursos', 
            'localField': 'id_curso', 
            'foreignField': 'id_curso', 
            'as': 'detalhes_curso'
        }
    }, {
        '$project': {
            '_id': 0, 
            'id_discente': 1, 
            'nivel': 1, 
            'detalhes_curso.id_curso': 1, 
            'detalhes_curso.id_unidade': 1, 
            'detalhes_curso.nome': 1
        }
    },
    {'$limit': 10}
])

for doc in result:
    print(doc)