from django.db import models
from utils.mixins import MixinsModel

class DjangoContentType(MixinsModel):
    django_content_type_id = models.AutoField(primary_key=True, db_column='id', verbose_name='Django Content Type ID')
    app_label = models.CharField(max_length=100, db_column='app_label', verbose_name='App Label')
    model = models.CharField(max_length=100, db_column='model', verbose_name='Model')

    class Meta:
        managed = False  # This tells Django NOT to create or alter the table
        db_table = 'django_content_type'
        app_label = 'core'
        verbose_name = "Django Content Type"
        unique_together = (('app_label', 'model'),)
        ordering = ['app_label', 'model']

    def __str__(self):
        return f"{self.app_label}.{self.model}"

    def __repr__(self):
        return f"<DjangoContentType {self.app_label}.{self.model}>"

    def __label__(self):
        return f"{self.app_label}.{self.model}"
