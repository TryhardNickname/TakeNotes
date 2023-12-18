from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_note = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_notes')

    def __str__(self):
        return self.title