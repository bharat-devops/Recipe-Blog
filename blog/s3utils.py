from storages.backends.s3boto3 import S3Boto3Storage


def StaticRootS3Boto3Storage(): return S3Boto3Storage(location='static_root')


def MediaRootS3Boto3Storage(): return S3Boto3Storage(location='media_root')
