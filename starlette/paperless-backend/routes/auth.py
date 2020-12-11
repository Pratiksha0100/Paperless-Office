from starlette.responses import JSONResponse
from utils.models import *
from utils.db import database
from utils.misc import row2dict



async def register(request):
    data = await request.json()
    try:
        query = users.insert().values(
            uname=data['uname'],
            role=data['role'],
            password=data['password'],
            department=data['department'],
            email=data['email'],
            linkedin=data['linkedin'],
            twitter=data['twitter'],
            phone=data['phone'],
            city=data['city']
        )
        await database.execute(query)
    except KeyError as e:
        return JSONResponse({
            'error': 'attr not found',
            'data': None
        }, status_code=401)
    except Exception as e:
        print(e)
        return JSONResponse({
            'error': 'internal server error',
            'data': None

        }, status_code=503)

    return JSONResponse({
        'error': None,
        'data': 'success'
    }, status_code=200)

async def login(request):
    data = await request.json()
    try:
        query = users.select(whereclause = (users.c.email == data['email'] and users.c.password == data['password']))
        
        user = await database.fetch_one(f"""select * from users where email = '{data['email']}' and password = '{data['password']}'""")
        # user = await database.fetch_one(query)
        print(user, data)
    except KeyError as e:
        return JSONResponse({
            'error': 'attr not found',
            'data': None
        }, status_code=401)
    except Exception as e:
        print(e)
        return JSONResponse({
            'error': 'internal server error',
            'data': None

        }, status_code=503)

    return JSONResponse({
        'error': None,
        'data': None if not user else row2dict(user)
    }, status_code=200)




# async def upload_file(request):
#     form = await request.form()
#     print(form)
#     filename = form["file"].filename
#     ty = form['file'].content_type
#     contents = await form["file"].read()
#     f = open(f'outputs/{filename}', 'wb')
#     f.write(contents)
#     f.close()
#     f = open(f'outputs/{filename}', 'r')
#     # print(f.read())
#     await form["file"].close()
#     return JSONResponse({
#         'name': filename,
#         'contents': f.read(),
#         'type': ty
#     })
