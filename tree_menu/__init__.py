import logging.config


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s - [%(levelname)s] -  %(name)s - '
                      '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
        },
    },

    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'default_formatter',
            'filename': 'main.log'
        }
    },

    'loggers': {
        'menu_app': {
            'handlers': ['stream_handler', 'file'],
            'level': 'DEBUG',
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
