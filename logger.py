import logging
import os
class Logger(object):
    def __init__(self, name):
        name = name.replace('.log','')
        logger = logging.getLogger('log_namespace.%s' % name)  # log_namespace can be replaced with your namespace
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            #date_tag = datetime.now().strftime("%Y-%b-%d")
            #file_name = os.path.join(os.getcwd() + "/logs/application_"+ str(date_tag) + ".log")
            logpath = os.getcwd() + "/logs/app.log"
            if not os.path.exists(logpath):
                os.mkdir("logs")
            file_name = os.path.join(os.getcwd() + "/logs/app.log")# usually I keep the LOGGING_DIR defined in some global settings file
            handler = logging.FileHandler(file_name)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler) # finally add handler to logger
        self._logger = logger

    def get(self):
        return self._logger