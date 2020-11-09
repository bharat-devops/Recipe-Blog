from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = 'feastbeast/static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'feastbeast/media'
    default_acl = 'public-read'
    file_overwrite = False
