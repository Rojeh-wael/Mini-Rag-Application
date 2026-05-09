import os
import regex
from fastapi import UploadFile, File
from .BaseController import BaseController
from models import ResponseSignal
from .ProjectController import ProjectController

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale=1048576 ## 1MB in bytes    

    def validate_uploaded_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_ALLOWED.value
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_TOO_LARGE.value
        
        return True, ResponseSignal.FILE_VALIDATION_SUCCESS.value
    

    def generate_unique_filename(self, orig_filename: str, project_id: str):
        
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        clean_filename = self.get_clean_filename(orig_filename)
        new_file_path = os.path.join(project_path,
                                      f"{random_key}_{clean_filename}"
                                      )
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(project_path,
                                      f"{random_key}_{clean_filename}"
                                      )
        return new_file_path,random_key + "_" + clean_filename



    def get_clean_filename(self,orig_filename: str):
        clean_filename = regex.sub(r'[^\w\.-]', '_', orig_filename)
        return clean_filename