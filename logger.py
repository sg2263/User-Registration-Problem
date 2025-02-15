import logging 
#creating a configuration for our loggers , with filename , setting the level and the log message.
logging.basicConfig( filename="project.log",level=logging.INFO,format = "%(asctime)s %(levelname)s %(message)s",filemode='a')

def user_logs():
    return logging.getLogger()