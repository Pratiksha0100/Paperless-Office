from starlette.responses import JSONResponse
from utils.models import *
from utils.db import database
from utils.misc import row2dict

async def get_profile(request):
    data = request.query_params
    try:
        query = users.select(whereclause = (users.c.uid == data['uid']))
        user = await database.fetch_one(f"""select * from users where uid = '{data['uid']}'""")
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
    }, status_code=404 if not user else 200)

