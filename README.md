Welcome to django-openmrs-db, a [Django](https://www.djangoproject.com/) app for
talking directly to the [OpenMRS](https://openmrs.org/) database.

This work is copyright Charl P. Botha <cpbotha@vxlabs.com> 2021 and is made
available under the open source BSD 3-clause license.

## Installation

In theory, the following should work.

First install this package, preferably into the virtual environment you're using
for your Django project ([I recommend
poetry](https://vxlabs.com/software-development-handbook/#prefer-poetry-for-managing-project-and-product-dependencies)):

```shell
pip install git+https://github.com/cpbotha/django-openmrs-db.git@main
```

Add `openmrs_db` to your `INSTALLED_APPS`, hook up your Django to the
pre-initialised OpenMRS database, and you should be able to access everything
via the Django ORM.

You should be able to interact with a number of the OpenMRS database tables via
the Django admin.

## Examples

### Django settings DATABASES

If you're connecting directly to the [OpenMRS reference application
docker-compose
setup's](https://github.com/openmrs/openmrs-contrib-ansible-docker-compose/tree/master/files/qa-refapp)
mysql instance, with ports forwarded to the host, your Django database setup
could look like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'openmrs',
        'USER': 'openmrs',
        'PASSWORD': 'Admin123',
        # if this is localhost, mysql will attempt connecting via socket
        'HOST': '127.0.0.1',
        'PORT': '3306',        
    }
}
```