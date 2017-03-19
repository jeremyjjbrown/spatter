import logging
import os

from flask import Flask, render_template, Response, abort
from spatter.s3 import S3Bucket, S3Exception
from spatter.mime import Mime

from spatter import app

bucket_name = os.environ['S3_BUCKET_NAME']
s3_bucket = S3Bucket(bucket_name)


@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        handler = logging.StreamHandler()
        app.logger.addHandler(handler)
        app.logger.setLevel(logging.INFO)
        logger = logging.getLogger('werkzeug')
        logger.addHandler(handler)


@app.route('/<path:path>', methods=['GET'])
@app.route('/', methods=['GET'])
def index(path=''):
    keys = s3_bucket.get_folders_and_file_keys(path)
    head, tail = os.path.split(path.rstrip('/'))
    if path == '' or path.endswith('/'):
        return render_template('index.html',
                               bucket_name=bucket_name,
                               parent=head,
                               keys=keys)
    else:
        try:
            response = s3_bucket.get_content(path)
        except S3Exception:
            abort(404)
        mime_type = Mime.for_ext(path)
        return Response(response, mimetype=mime_type)


if __name__ == '__main__':
    app.run(debug=True)
