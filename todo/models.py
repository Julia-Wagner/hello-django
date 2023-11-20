from django.db import models


# after creating a new model run the following to make migrations:
# python manage.py makemigrations (--dry-run to preview)
# python manage.py showmigrations (to show migrations)
# python manage.py migrate (--plan to preview)
# register in models.py
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # update name showing in admin
    def __str__(self):
        return self.name
