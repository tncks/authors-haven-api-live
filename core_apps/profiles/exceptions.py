from rest_framework.exceptions import APIException


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You can not edit a profile that does not belong to you"


class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "You can not follow yourself"
