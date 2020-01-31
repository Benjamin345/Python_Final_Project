# snippets/models.py
from django.db import models
from pygments import highlight # new
from pygments.formatters.html import HtmlFormatter # new
from pygments.lexers import get_all_lexers, get_lexer_by_name # new
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE) # new
    highlighted = models.TextField() # new

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs): # new
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Incidents(models.Model):
    Number : models.IntegerField()
    Incident_State : models.CharField(max_length=100, blank=True, default='')
    Active :models.BooleanField()
    Reassignement_count : models.IntegerField()
    Reopen_count: models.IntegerField()
    Sys_mod_count: models.IntegerField()
    Made_sla: models.BooleanField()
    Caller_id: models.CharField()
    Opened_by: models.CharField
    Opened_at: models.DateField()
    Sys_created_by: models.CharField()
    Sys_created_at: models.DateField()
    Sys_updated_by: models.CharField()
    Sys_updated_at: models.DateField()
    Contact_type: models.CharField()
    Location: models.CharField()
    Category: models.CharField()
    Subcategory: models.CharField()
    U_symptom: models.CharField()
    Cmdb_ci: models.CharField()
    Impact: models.CharField()
    Urgency: models.CharField()
    Priority: models.CharField()
    Assignment_group: models.CharField()
    Assigned_to: models.CharField()
    Knowledge: models.BooleanField()
    U_priority_confirmation: models.BooleanField()
    Notify:models.CharField()
    Problem_id: models.CharField()
    Rfc: models.CharField()
    Vendor: models.CharField()
    Caused_by: models.CharField()
    Close_code: models.CharField()
    Resolved_by: models.CharField()
    Resolved_at: models.DateField()
    Closed_at:models.DateField()
