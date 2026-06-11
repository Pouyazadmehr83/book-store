import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone  # جدید


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    descriptions = models.TextField(max_length=250,null=True)
    # فیلد جدید برای عکس (اختیاری)
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='book_id_index'),
            models.Index(fields=['title'], name='book_title_index'),
            models.Index(fields=['author'], name='book_author_index'),
        ]
        permissions = [
            ('special_status', 'Can read all books'),
        ]
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.TextField()  # از CharField به TextField تغییر دادم تا کاربر بتونه متن بلند بنویسه
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    # فیلدهای جدید
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],  # 1 تا 5 ستاره
        default=5,
        help_text="Rating from 1 to 5 stars"
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['book'], name='review_book_index'),
            models.Index(fields=['author'], name='review_author_index'),
            models.Index(fields=['-created_at'], name='review_created_at_index'),
        ]
        ordering = ['-created_at']  # جدیدترین اول نمایش داده بشه
        unique_together = ['book', 'author']  # هر کاربر فقط یک بار می‌تونه به هر کتاب نظر بده

    def __str__(self):
        return f'{self.author} - {self.book.title} ({self.rating}⭐)'