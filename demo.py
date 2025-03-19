from us_visa.logger import logging
from us_visa.exception import USVisaException

try:
    a = 2/0
except Exception as e:
    raise USVisaException(e, sys)


# logging.info('Wellcome to our custome log')


