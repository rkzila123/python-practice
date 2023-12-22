'''
Created on Nov 28, 2023

@author: Rohit.Kumar012
'''
import logging

logging.basicConfig(filename='MyLog.log',level=logging.INFO)
logging.critical('Critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')