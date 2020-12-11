from starlette.responses import JSONResponse
from utils.models import *
from utils.db import database
from utils.misc import row2dict
from datetime import datetime


async def post_manual(request):
    form = await request.form()
    timestamp = datetime.timestamp(datetime.now())
    try:
        data = form.__dict__['_dict']
        filename = form['document'].filename
        contents = await form['document'].read()
        f = open(f'static/manual/{timestamp}-{filename}', 'wb')
        f.write(contents)
        f.close()
        print(data)
        query = manual.insert().values(
            uploaded_by = int(data['uploaded_by']),
            title = data['title'],
            department = data['department'],
            document = f'static/manual/{timestamp}-{filename}'
        )
        
        await database.execute(query)
    except KeyError as e:
        return JSONResponse({
            'error': 'attr not found',
            'data': None
        }, status_code=403)
    except Exception as e:
        print(e)
        return JSONResponse({
            'error': 'internal server error',
            'data': None

        }, status_code=503)
    print(form.__dict__)
    return JSONResponse({
        'error': None,
        'data': {
            'filename': f'static/manual/{timestamp}-{filename}'
        }
    }, 200)

async def get_manual(request):
    data = request.query_params
    try:
        query = manual.select(whereclause = (manual.c.department == data['department']))
        result = await database.fetch_all(query)
    except KeyError as e:
        return JSONResponse({
            'error': 'attr not found',
            'data': None
        }, status_code=403)
    except Exception as e:
        print(e)
        return JSONResponse({
            'error': 'internal server error',
            'data': None

        }, status_code=503)
    return JSONResponse({
        'error': None,
        'data': None if not result else [row2dict(x) for x in result]
    }, 404 if not result else 200)