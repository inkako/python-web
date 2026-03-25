# import sys
#
# from loguru import logger as loguru_logger
#
# from app.config import settings
#
#
# class Logging:
#     def __init__(self):
#         debug = settings.log.level
#         if debug:
#             self.level = "DEBUG"
#         else:
#             self.level = "INFO"
#
#         self.path = settings.log.path
#
#     def logger_with_setup(self):
#         loguru_logger.remove()
#         loguru_logger.add(sink=sys.stdout, level=self.level)
#         loguru_logger.add(sink=self.path, level=self.level, rotation="100 MB", retention="10 days")
#         return loguru_logger
#
#
# logging = Logging()
# logger = logging.logger_with_setup()
