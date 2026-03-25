from .settings import Settings

# 应用波及的配置项
settings = Settings()

# 数据库 ORM 配置
TORTOISE_ORM = {
    'connections': {
        'mysql': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': settings.db.host,
                'port': settings.db.port,
                'user': settings.db.username,
                'password': settings.db.password,
                'database': settings.db.database,
            }
        }
    },
    'apps': {
        'models': {
            'models': ['app.models', 'aerich.models'],
            'default_connection': 'mysql',
        }
    },
    # 'routers': ['path.router1', 'path.router2'],
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}
