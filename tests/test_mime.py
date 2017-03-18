from s3proxy.mime import Mime


class TestClass:

    def test_mime_mappings(self):
        assert Mime.for_ext('foo.jpeg') == 'image/jpeg'
        assert Mime.for_ext('unknown.type') == 'text/plain'
