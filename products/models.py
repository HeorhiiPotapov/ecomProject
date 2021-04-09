from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator)
from django.utils import timezone
from decimal import Decimal
from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()


class Category(MPTTModel):
    """
    Product category class
    """
    name = models.CharField("Название", max_length=300)
    slug = models.SlugField("Url", max_length=300, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children',
                            verbose_name="Категория верхнего уровня")
    is_active = models.BooleanField("Статус", default=True)

    class MPTTMeta:
        order_insertion_by = ['slug']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:by_category",
                       kwargs={"slug": self.slug})


class Product(models.Model):
    """
    Product class
    """
    ANY = 0
    KHARKOV = 1
    KIEV = 2
    DNEPR = 3

    CITY_LIST = [
        ('0', 'Все'),
        ('1', 'Харьков'),
        ('2', 'Киев'),
        ('3', 'Днепр')
    ]

    name = models.CharField("Название", max_length=300)
    price = models.DecimalField("Цена", max_digits=10,
                                decimal_places=2,
                                default=0)
    discount = models.IntegerField("Дисконт", default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    main_image = models.ImageField(
        "Изображение", upload_to="product_img")
    video = models.URLField("Ссылка на видео", null=True, blank=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="products",
                              verbose_name="Владелец")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name="Категория")
    overview = models.TextField("Описание", max_length=2000)
    is_active = models.BooleanField("Статус", default=False)
    timestamp = models.DateTimeField("Дата добавления", default=timezone.now)
    city = models.CharField(max_length=20, choices=CITY_LIST, default=0)

    class Meta:
        verbose_name = "Товар/Акция"
        verbose_name_plural = "Товары/Акции"
        ordering = ('-timestamp',)

    def price_after_discount(self):
        return self.price - self.price * \
            (self.discount / Decimal('100'))

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})


class Image(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images")
    image = models.ImageField("Изображение", upload_to="product_img")
    is_active = models.BooleanField("Статус", default=True)
    timestamp = models.DateTimeField("Дата добавления", default=timezone.now)

    class Meta:
        verbose_name = "Дополнительное фото"
        verbose_name_plural = "Дополнительные фото"

    def __str__(self):
        return f"{self.product.id}"


class Feedback(models.Model):
    sender = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="feed_sender")
    receiver = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="feed_receiver")
    text = models.TextField(max_length=600)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender.email} at {self.timestamp}"
