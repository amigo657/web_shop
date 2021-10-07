from re import VERBOSE
from django.db import models
from django.core.exceptions import ValidationError
from user.models import User


def sharp_valid(value):
    if not value.startswitch("#"):
        raise ValidationError(
            f"Invalid value. Maybe '#{value}' ?",
        )

class Kit(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name="Title",
    )
    text = models.TextField(
        verbose_name="Text of kit",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data of create kit",
    )
    edited = models.DateTimeField(
        auto_now=True,
        verbose_name="Data of edit kit",
    )
    views = models.BigIntegerField(
        default=0,
        verbose_name="Count of view."
    )
    is_moderated = models.BooleanField(
        default=False,
        verbose_name="If moderated"
    )

    class Meta:
        db_table = "kits"
        verbose_name = "Kit"
        verbose_name_plural = "Kits"

    def __str__(self):
        return f"Kit of {self.title}"


class Comments(models.Model):
    auther = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    text = models.DateTimeField(
        verbose_name="Text of comment."
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data of create post.",
    )
    edited = models.DateTimeField(
        auto_now=True,
        verbose_name="Data of edit post.",
    )
    is_moderated = models.BooleanField(
        default=False,
        verbose_name="If moderated"
    )

    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment of {self.auther}"