from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = 'static_in_env'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media_in_env'
    default_acl = 'public-read'
    file_overwrite = False
