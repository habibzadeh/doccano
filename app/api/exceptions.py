from rest_framework import status
from rest_framework.exceptions import APIException, PermissionDenied, NotFound, ValidationError


class FileParseException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid file format, line {}: {}'
    default_code = 'invalid'

    def __init__(self, line_num, line, code=None):
        detail = self.default_detail.format(line_num, line)
        super().__init__(detail, code)


class AutoLabelingException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Auto labeling not allowed for the document with labels.'


class AutoLabeliingPermissionDenied(PermissionDenied):
    default_detail = 'You do not have permission to perform auto labeling.' \
                     'Please ask the project administrators to add you.'


class URLConnectionError(NotFound):
    default_detail = 'Failed to establish a connection. Please check the URL or network.'


class AWSTokenError(ValidationError):
    default_detail = 'The security token included in the request is invalid.'
