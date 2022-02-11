## Version 1

This subdirectory is a very rudimentary CRUD website using Django framework. It should contain the following:

### To-do lists:

* [X] Add function-based views.

* [ ] Implement unit-testing for views (using [APITestCase](https://www.django-rest-framework.org/api-guide/testing/#api-test-cases) from DRF and [model_mommy](https://model-mommy.readthedocs.io/en/latest/basic_usage.html)).

* [ ] Implement [DRF Router](https://www.django-rest-framework.org/api-guide/routers/) for mapping of URL with views.

* [X] Setup [Github Actions YML file](../.github/workflows/github-actions-ci.yml) for automating unit testing.


### Run test cases:
To run all test cases, simply run:
```
$ ./manage.py test
```
