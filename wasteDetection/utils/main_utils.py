import os
import sys
import yaml
import base64

from wasteDetection.logger import logging
from wasteDetection.exception import AppException

def read_yaml_file(file_path: str )-> dict:
    try:
        with open(file_path,'rb') as yaml_file:
            logging.info('Read the yaml file successfully')
            yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys)
    
def write_yaml_file(filepath :str , content: object, replace :bool = False ) -> None:
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        
        os.makedirs(os.path.dir(filepath),exist_ok=True)
        with open(filepath, 'w') as file:
            yaml.dump(content,file)
            logging.info('Successfully write yaml file')
    except Exception as e:
        raise AppException(e,sys)

def decodeImage(imgstring, filename):
    imgdata =  base64.b64decode(imgstring)
    with open("./data/"+filename,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())