from django.db import models

class Tag(models.Model):
    name = models.TextField(blank=False,
                            null=False)


class Author(models.Model):
    name = models.TextField(blank=False,
                            null=False)
    tags = models.ManyToManyField(Tag,
                                  related_name='authors')

    def __str__(self):
        return f'{self.name}'



class Book(models.Model):
    name = models.TextField(blank=False,
                            null=False)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='booksbyauthor')
    tags = models.ManyToManyField(Tag,
                                  related_name='booksbytag')

    def __str__(self):
        return f'{self.name} ({self.author.name})'

