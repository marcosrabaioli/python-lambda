import json
from marshmallow.exceptions import ValidationError
from http import HTTPStatus as status


class RestService:

    @staticmethod
    def _respond(err, statusCode=200, body=None):
        return {
            'statusCode': statusCode,
            'body': err if err else json.dumps(body),
            'headers': {
                'Content-Type': 'application/json',
            },
        }

    @staticmethod
    def responseForError(err):
        if isinstance(err, ValidationError):
            return RestService._respond(err, status.UNPROCESSABLE_ENTITY.value)
        else:
            return RestService._respond(err, status.INTERNAL_SERVER_ERROR.value)

    @staticmethod
    def responseForCreate(object):
        return RestService._respond(statusCode=status.CREATED.value, body=object)
