from django.db import models


try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    pass
else:
    add_introspection_rules([], [
        "^brand\.models\.fields\.FormulaField$"])


class FormulaField(models.CharField):
    pass
