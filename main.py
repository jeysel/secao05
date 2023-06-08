from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware import Middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


from views import home_view, error_view
from views.admin import admin_view


middlewares = [
   Middleware(
       TrustedHostMiddleware,
       allowed_hosts=['127.0.0.1', 'fapiw.geekuniversity.com.br']
    ),
    # Middleware(HTTPSRedirectMiddleware), HABILITAR EM PRODUÇÃO
]

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    exception_handlers=error_view.exception_handlers,
    middleware=middlewares
    )

app.include_router(home_view.router)
app.include_router(admin_view.router)
app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, log_level="info")
