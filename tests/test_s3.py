from spatter.s3 import S3Bucket

from mock import Mock


class TestS3:

    def test_s3_get_folders_and_file_keys(self):
        """S3Bucket gets a list of key Prefixes and Objects."""
        mock_s3 = Mock()
        s3_response = {'CommonPrefixes': [
                          {'Prefix': 'folder1/'},
                          {'Prefix': 'folder2/'},
                          {'Prefix': 'folder3/'}],
                       'Contents': [
                          {'Key': 'file.txt'},
                          {'Key': 'index.hmtl'},
                          {'Key': 'main.css'}]}
        mock_s3.list_objects.return_value = s3_response

        s3_bucket = S3Bucket('bucket_name',  s3_client=mock_s3)
        assert s3_bucket.get_folders_and_file_keys('foo/') == \
            ['folder1/', 'folder2/', 'folder3/',
             'file.txt', 'index.hmtl', 'main.css']

    def test_s3_gets_object_content(self):
        """S3Bucket gets object content."""
        mock_s3 = Mock()
        mock_s3_object = Mock()
        s3_response = {'Body': mock_s3_object}
        mock_s3_object.read.return_value = "file content"
        mock_s3.get_object.return_value = s3_response

        s3_bucket = S3Bucket('bucket_name',  s3_client=mock_s3)
        assert s3_bucket.get_content('/file.text') == \
            'file content'

