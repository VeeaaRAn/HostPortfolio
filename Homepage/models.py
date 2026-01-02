from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('GAME', 'Game Development'),
        ('DATA', 'Data Engineer'),
        ('WEB', 'Full Stack Web'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True) # Optional link to GitHub or Demo
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title