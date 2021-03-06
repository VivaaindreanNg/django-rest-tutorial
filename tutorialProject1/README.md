## Version 1

This subdirectory is a very rudimentary CRUD website using Django framework. It should contain the following:

### To-do lists:

* [X] Add function-based views.

* [X] Implement unit-testing for views (using [APITestCase](https://www.django-rest-framework.org/api-guide/testing/#api-test-cases) from DRF and [model_mommy](https://model-mommy.readthedocs.io/en/latest/basic_usage.html)).

* [X] Setup [Github Actions YAML file](../.github/workflows/github-actions-ci.yml) for automating unit testing.

* [X] Change the endpoint such that GET, POST, PUT, DELETE methods are using the same endpoint.

* [X] Add PATCH methods for partially-update a request.

* [ ] Implement [Karate Script](https://github.com/VivaaindreanNg/Karate-Test) for Automated Testing.

* [X] Add existing models in Django admin site.

* [ ] Implement Django [get_FOO_display](https://docs.djangoproject.com/en/4.0/ref/models/instances/#django.db.models.Model.get_FOO_display) for fields with choices.

* [X] Add [Custom Django Management Commands](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/) to automate some stuffs (i.e: updating records in DB).

* [ ] Implement webhook for Django.

* [ ] Implement service layer (Based on Two Scoops of Django).


### Run test cases:
To run all test cases, simply run:
```
$ ./manage.py test
```
