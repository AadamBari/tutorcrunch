# TutorCruncher Developer Test

In this repo is an unfinished Django web app of a simple till system for buying fruit. Underneath are a few tasks that you need to complete
to get the till up and running.

### Objectives

#### Primary

* Correctly generate and display the change from the amount paid **with demoninations (eg. £17.40 = 1 x £10, 1 X £5, 2 x £1, 2 X £0.20)**.
* Build a list view to list all orders that have taken place
* Add functionality to choose a quantity when buying the product, rather than just 1

#### Secondary (if you have time)

* Use the a [management command](https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/) to add a new product
* Add a unit test (or multiple unit tests) to test submitting the main form

### Notes

* Try and think of the end user's needs. For instance, displaying the figures with currency, or making sure the amount paid is correct.
* Don't forget that if you change a field on the model, you'll need to
[create and run migrations](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-makemigrations)
* Django's documentation is your friend

### Rules

* You have 1.5 hours
* You can use online resources

### Set up

You've got a computer with everything set up, so you just need to navigate to the repo within the terminal and run

```
./manage.py runserver
```

to run the django server. We recommend that you use a virtual environment.

If you need to wipe the database, just delete the `db.sqlite3` database and run `./manage.py migrate` to recreate the database.
