import sys
import pymongo
import urllib.parse
import os
import certifi
from dotenv import load_dotenv

from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME

# Load environment variables from .env file
load_dotenv()

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                # Get connection URL from environment variable
                mongo_db_url = os.getenv("CONNECTION_URL")
                if mongo_db_url is None:
                    # If CONNECTION_URL is not set, try to build it from individual credentials
                    username = os.getenv("MONGODB_USERNAME")
                    password = os.getenv("MONGODB_PASSWORD")
                    host = os.getenv("MONGODB_HOST")
                    
                    if not all([username, password, host]):
                        raise Exception("MongoDB connection details not found in environment variables.")
                    
                    # Escape username and password
                    escaped_username = urllib.parse.quote_plus(username)
                    escaped_password = urllib.parse.quote_plus(password)
                    
                    # Create connection URL
                    mongo_db_url = f"mongodb+srv://{escaped_username}:{escaped_password}@{host}/?retryWrites=true&w=majority&appName=Cluster0"
                
                # Connect to MongoDB with the URL
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e, sys)