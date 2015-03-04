from django.db import models

class MicroService(models.Model):

    def __unicode__(self):
        return self.title 
    
    title = models.CharField(max_length=100)
    description = models.TextField()

    repo_url = models.URLField(null=True)
    documentation_url = models.URLField(null=True)
    staging_url = models.URLField(null=True)
    live_url = models.URLField(null=True)
    api_explorer_url = models.URLField(null=True)

    maturity = models.PositiveIntegerField()
    owner = models.PositiveIntegerField(help_text="User ID of the person responsible for this service")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
