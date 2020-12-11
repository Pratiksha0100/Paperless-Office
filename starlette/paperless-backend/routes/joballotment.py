from starlette.responses import JSONResponse
from utils.models import *
from utils.db import database
from utils.misc import row2dict
from datetime import datetime
import traceback
from sqlalchemy import select


async def post_joballotment(request):
    form = await request.form()
    timestamp = datetime.timestamp(datetime.now())
    try:
        data = form.__dict__['_dict']
        sub_date = int(data['submission_date'])
        formatted_sub_date = datetime.fromtimestamp(sub_date)
        filename = form['document'].filename
        contents = await form['document'].read()
        f = open(f'static/joballotment/{timestamp}-{filename}', 'wb')
        f.write(contents)
        f.close()
        print(data)
        query = joballotment.insert().values(
            # job_id = int(data['job_id']),
            alloted_by = int(data['alloted_by']),
            alloted_to = int(data['alloted_to']),
            # allotment_date  = timestamp,
            submission_date = formatted_sub_date,
            title = data['title'],
            task = f'static/joballotment/{timestamp}-{filename}',
            approved_status = False
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
            'filename': f'static/joballotment/{timestamp}-{filename}'
        }
    }, 200)

async def get_joballotment(request):
    data = request.query_params
    try:
        query = joballotment.select(whereclause = (joballotment.c.alloted_to == data['uid']))
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

async def submit_job(request):
    form = await request.form()
    timestamp = datetime.timestamp(datetime.now())
    try:
        data = form.__dict__['_dict']
        filename = form['document'].filename
        contents = await form['document'].read()
        f = open(f'static/submission/{timestamp}-{filename}', 'wb')
        f.write(contents)
        f.close()
        print(data)
        query = joballotment.update().where(joballotment.c.job_id==data['job_id']).values(submission = f'static/submission/{timestamp}-{filename}')
        # query = joballotment.insert().values(
        #     uploaded_by = int(data['uploaded_by']),
        #     title = data['title'],
        #     department = data['department'],
        #     document = f'static/manual/{timestamp}-{filename}'
        # )
        
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
            'filename': f'static/submission/{timestamp}-{filename}'
        }
    }, 200)

async def post_review(request):
    data = await request.json()
    timestamp = datetime.timestamp(datetime.now())
    try:
        query = joballotment.update().where(joballotment.c.job_id==data['job_id']).values(review = data['review'])
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
    return JSONResponse({
        'error': None,
        'data': None
    }, 200)

async def post_reply(request):
    data = await request.json()
    timestamp = datetime.timestamp(datetime.now())
    try:
        query = joballotment.update().where(joballotment.c.job_id==data['job_id']).values(reply = data['reply'])
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
    return JSONResponse({
        'error': None,
        'data': None
    }, 200)

async def approved_status(request):
    data = await request.json()
    # timestamp = datetime.timestamp(datetime.now())
    try:
        query = joballotment.update().where(joballotment.c.job_id==data['job_id']).values(approved_status = True)
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
    return JSONResponse({
        'error': None,
        'data': None
    }, 200)

async def monthly_report(request):
    data = request.query_params
    try:
        # query = joballotment.select(whereclause = (users.c.department == data['department'] and joballotment.c.alloted_to == users.c.uid))
        query  = select([users, joballotment]).where(users.c.department == data['department'] and joballotment.c.alloted_to == users.c.uid)
        result = await database.fetch_all(f'''select j.* from joballotment j, users u where u.department = '{data['department']}' and j.alloted_to = u.uid;''')
    except KeyError as e:

        return JSONResponse({
            'error': 'attr not found',
            'data': None
        }, status_code=403)
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
        print(e)
        return JSONResponse({
            'error': 'internal server error',
            'data': None

        }, status_code=503)

    return JSONResponse({
        'error': None,
        'data': None if not result else [row2dict(x) for x in result]
    }, 404 if not result else 200)

async def employee_list(request):
    data = request.query_params
    try:
        query = users.select(whereclause = (users.c.role == "employee" and users.c.department == data['department']))
        user = await database.fetch_all(f"""select * from users where department = '{data['department']}' and role = 'employee'""")
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
        'data': None if not user else [row2dict(u) for u in user]
    }, status_code=404 if not user else 200)


# post => joballotment = jobid, allby, allto, alldate, submissiondate, title, task
# get => joballotment = select * from joballotment

# post => submission

# post => review and reply


# query  = joballotment.select(whereclause = (joballotment.c.alloted_by == data['alloted_by']))
