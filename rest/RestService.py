import json
from marshmallow.exceptions import ValidationError
from http import HTTPStatus as Status
from utils.JsonEncoder import DecimalEncoder


class RestService:

    @staticmethod
    def _respond(err=None, statusCode=200, body=None):
        return {
            'statusCode': statusCode,
            'body': err if err else json.dumps(body, cls=DecimalEncoder),
            'headers': {
                'Content-Type': 'application/json',
            },
        }

    @staticmethod
    def responseForError(err):
        if isinstance(err, ValidationError):
            return RestService._respond(err=err, statusCode=Status.UNPROCESSABLE_ENTITY.value)
        else:
            return RestService._respond(err=err, statusCode=Status.INTERNAL_SERVER_ERROR.value)

    @staticmethod
    def responseForCreate(object):
        return RestService._respond(statusCode=Status.CREATED.value, body=object)

    @staticmethod
    def responseForOK(object):
        return RestService._respond(statusCode=Status.OK.value, body=object)
