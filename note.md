# Migrations
commands
=========
- migrate
- makemigrations
- sqlmigrate
- showmigrations


You should rarely, if ever, need to edit migration files by hand, but it’s
entirely possible to write them manually if you need to. Some of the more
complex operations are not autodetectable and are only available via a
hand-written migration, so don’t be scared about editing them if you have to.

use_in_migrations -> manager class
migrate -> fake-initial

reverse migration -> $ python manage.py migrate app_label 0002

sqash migrations

Warning
=======
References to functions in field options such as upload_to and limit_choices_to
and model manager declarations with managers having use_in_migrations = True
are serialized in migrations, so the functions and classes will need to be kept
around for as long as there is a migration referencing them. Any custom model
fields will also need to be kept, since these are imported directly by
migrations.

In addition, the concrete base classes of the model are stored as pointers, so
you must always keep base classes around for as long as there is a migration
that contains a reference to them. On the plus side, methods and managers from
these base classes inherit normally, so if you absolutely need access to these
you can opt to move them into a superclass.


Considerations when removing model fields¶

Data Migrations¶
$ python manage.py makemigrations --empty yourappname
