from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
## from https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/

class StaticStorage(S3Boto3Storage):
    bucket_name = 'feastbeast-bucket'
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    bucket_name = 'feastbeast-bucket'
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
    
class PrivateMediaStorage(S3Boto3Storage):
    location = 'private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
