import boto3


class S3Bucket(object):
    """S3 client"""

    def __init__(self, bucket_name,  s3_client=None):
        self.bucket_name = bucket_name
        self.s3_client = s3_client or boto3.client('s3')

    def get_folders_and_file_keys(self, key_prefix):
        """Get the folder prefixs and file keys for any key prefix."""

        # key_prefix must end with a / to return useful results for
        # anything but the bucket root, then just / returns nothing.
        result = self.s3_client.list_objects(
            Bucket=self.bucket_name,
            Prefix=key_prefix,
            Delimiter='/'
        )

        keys = []
        for prefix in result.get('CommonPrefixes', []):
            keys.append(prefix.get('Prefix'))
        for file_key in result.get('Contents', []):
            keys.append(file_key.get('Key'))
        return keys

    def get_content(self, key):
        """Get File content"""
        key = key.lstrip('/')
        obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
        response = obj['Body'].read()
        return response

