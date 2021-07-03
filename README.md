Welcome to django-openmrs-db, a Django app for talking directly to the OpenMRS
database.

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
