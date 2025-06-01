from django.db import models
from django.utils import timezone

class Photo(models.Model):
    id = models.AutoField(primary_key=True)  # Теперь id явно определено
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание фото")
    image = models.ImageField(upload_to='photos/', verbose_name="Фотография")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    def __str__(self):
        return self.title if self.title else f"Фото {self.id}"

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
