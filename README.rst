===============================
spatter
===============================


.. image:: https://img.shields.io/pypi/v/spatter.svg
        :target: https://pypi.python.org/pypi/spatter

.. image:: https://img.shields.io/travis/jeremyjjbrown/spatter.svg
        :target: https://travis-ci.org/jeremyjjbrown/spatter

.. image:: https://readthedocs.org/projects/spatter/badge/?version=latest
        :target: https://spatter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/jeremyjjbrown/spatter/shield.svg
     :target: https://pyup.io/repos/github/jeremyjjbrown/spatter/
     :alt: Updates

A simple stateless server to navigate and serve an AWS S3 Bucket.

The easiest way to use it is to grab the docker image.

.. code-block:: bash

    docker pull jeremyjjbrown/spatter
    sudo docker run \
        -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
        -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
        -e S3_BUCKET_NAME=$S3_BUCKET_NAME \
        -p 80:8000 jeremyjjbrown/spatter

* https://hub.docker.com/r/jeremyjjbrown/spatter/
* Free software: Apache License v2

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

