
from operator import pos
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from utils.db import database
from routes.auth import register, login
from routes.profile import get_profile
from routes.manual import post_manual, get_manual
# from routes.joballotment import post_joballotment, get_joballotment, submit_job, post_review, post_reply, approved_status, monthly_report
from routes.joballotment import *
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

routes = [
    Route("/register", endpoint=register, methods=["post"]),
    Route("/login", endpoint=login, methods=["post"]),
    Route("/profile", endpoint=get_profile, methods=["get"]),
    Route("/manual", endpoint=post_manual, methods=["post"]),
    Route("/manual", endpoint=get_manual, methods=["get"]),
    Route("/joballotment", endpoint=post_joballotment, methods=["post"]),
    Route("/joballotment", endpoint=get_joballotment, methods=["get"]),
    Route("/submit", endpoint=submit_job, methods=["post"]),
    Route("/review", endpoint=post_review, methods=["post"]),
    Route("/reply", endpoint=post_reply, methods=["post"]),
    Route("/approve", endpoint=approved_status, methods=["post"]),
    Route("/report", endpoint=monthly_report, methods=["get"]),
    Route("/employee", endpoint=employee_list, methods=["get"]),
    Mount('/static', app=StaticFiles(directory='static'), name="static"),
    
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

app = Starlette(
    routes=routes,
    on_startup=[database.connect],
    on_shutdown=[database.disconnect],
    middleware=middleware
)