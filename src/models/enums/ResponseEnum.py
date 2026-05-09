from enum import Enum


class ResponseSignal(Enum):
    FILE_VALIDATION_SUCCESS = "file_validation_success"
    FILE_VALIDATION_FAILURE = "file_validation_failure"
    FILE_TYPE_NOT_ALLOWED = "file_type_not_allowed"
    FILE_TOO_LARGE = "file_too_large"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILURE = "file_upload_failure"
    FILE_PROCESSING_FAILURE = "file_processing_failure"