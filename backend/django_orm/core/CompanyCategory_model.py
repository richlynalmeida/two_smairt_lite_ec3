from django.db import models
from utils.mixins import MixinsModel

class CompanyCategory(MixinsModel):
    company_category_id = models.AutoField(primary_key=True, verbose_name='Company Category ID')
    company_category_code = models.CharField(max_length=10, blank=False, null=False, unique=True,
                                             verbose_name='Company Category Code', help_text="10-letter category code", db_index=False,)
    company_category_title = models.CharField(max_length=255, blank=False, null=False, unique=True,
                                              verbose_name='Company Category Title', db_index=False,)
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        db_table = 'company_category'
        app_label = 'core'
        verbose_name_plural = "Organization / Company Category"
        ordering = ['company_category_code']

    def __str__(self):
        return f"{self.company_category_code} - {self.company_category_title}"

    def __repr__(self):
        return "<CompanyCategory {}>".format(f"{self.company_category_code} - {self.company_category_title}")

    def __label__(self):
        return f"{self.company_category_code} - {self.company_category_title}"
