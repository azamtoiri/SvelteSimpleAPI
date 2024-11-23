from django.db import models
from django.db.models import JSONField


class Component(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # hero, text-block, image-gallery and other
    schema = JSONField()  # JSON schema for component data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'components'

    def __str__(self, *args, **kwargs):
        return f"{self.name} | {self.type}"


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    layout = JSONField()  # Components structure on the page
    components = models.ManyToManyField(Component, through='PageComponent')

    class Meta:
        db_table = 'pages'

    def __str__(self, *args, **kwargs):
        return f"{self.title} | {self.slug}"


class PageComponent(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    content = JSONField()  # data for component
    order = models.IntegerField()

    class Meta:
        db_table = 'page_components'
        ordering = ['order']

    def __str__(self, *args, **kwargs):
        return f"{self.page.title} | {self.component.name}"
