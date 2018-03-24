# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import ast

# Create your models here.

class Sheet(models.Model):
    sheet_parameters = models.TextField(blank=True)

    def get_sheet_parameters(self):
        if self.sheet_parameters:
            return ast.literal_eval(self.sheet_parameters)
        else:
            return {}

    def set_sheet_parameters(self, params):
        self.sheet_parameters = str(params)
        self.save()
        return True
