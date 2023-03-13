from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# entidad user


class User (BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name='daniel', surname='romero', url='daniel.com', age=26),
              User(id=2, name='jonathan', surname='aguirre',
                   url='daniel.com', age=26),
              User(id=3, name='you', surname='tube', url='daniel.com', age=26)
              ]


# @app.get('/usersjson')
# async def usersjson():
#     return [
#         {'name': 'daniel', 'surname': 'romero',
#             'url': 'danielromeroag.web.app', 'age': 26},
#         {'name': 'jonathan', 'surname': 'aguirre',
#             'url': 'jona.web.app', 'age': 26},
#         {'name': 'you', 'surname': 'tube', 'url': 'youtube.com', 'age': 26},
#     ]


@app.get('/usersclass')
async def usersclass():
    return User(name='daniel', surname='romero', url='daniel.com', age=26)


@app.get('/users')
async def users():
    return users_list

# path
@app.get('/user/{id}')
async def user(id: int):
    return search_user(id)

# query
@app.get('/user/')
async def user(id: int):
    return search_user(id)


def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {'error': 'no se ha encontrado el usuario'}
