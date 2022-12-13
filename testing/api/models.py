from django.db import models

STATUS = (
    ("in_stock", "В наличии"),
    ("by_order", "Под заказ"),
    ("expected", "Ожидается поступление"),
    ("not_available", "Нет в наличии"),
    ("not_produced", "Не производится")
)


class Product(models.Model):
    name = models.CharField(max_length=250)
    vendor_code = models.CharField(max_length=150, unique=True)
    price = models.PositiveIntegerField()
    status = models.CharField(
        max_length=50,
        choices=STATUS
    )
    image = models.ImageField(
        'Картинка',
        upload_to='images/',
    )

    def __str__(self):
        return f"{self.name} - {self.vendor_code}"