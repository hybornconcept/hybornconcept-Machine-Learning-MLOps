# from us_visa.logger import logging
# from us_visa.exception import USVisaException

# try:
#     a = 2/0
# except Exception as e:
#     raise USVisaException(e, sys)


# logging.info('Wellcome to our custome log')

# from dotenv import load_dotenv
# import os
# # Load environment variables from .env file
# load_dotenv()
# mongo_db_url = os.getenv('CONNECTION_URL')
# print(mongo_db_url)

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="evidently")

from us_visa.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()


obj.run_pipeline()



