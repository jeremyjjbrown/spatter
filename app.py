import logging
import os

from flask import Flask, render_template, Response
from spatter.s3 import S3Bucket
from spatter.mime import Mime


app = Flask(__name__)
bucket_name = os.environ['S3_BUCKET_NAME']
s3_bucket = S3Bucket(bucket_name)


@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)


@app.route('/<path:path>', methods=['GET'])
@app.route('/', methods=['GET'])
def index(path=''):
    keys = s3_bucket.get_folders_and_file_keys(path)
    head, tail = os.path.split(path.rstrip('/'))
    app.logger.info(head)
    if path == '' or path.endswith('/'):
        return render_template('index.html',
                               bucket_name=bucket_name,
                               parent=head,
                               keys=keys)
    else:
        response = s3_bucket.get_content(path)
        mime_type = Mime.for_ext(path)
        return Response(response, mimetype=mime_type)


if __name__ == '__main__':
    app.run(debug=True)
