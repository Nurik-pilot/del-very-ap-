from django.db import models

class DeliveryStatus(models.TextChoices):
    CREATED = 'created', 'Создана'
    IN_DELIVERY = 'in_delivery', 'Товар передан в доставку'
    DELIVERED = 'delivered', 'Товар доставлен'

class DeliveryOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    item = models.CharField(max_length=100)
    order_status = models.CharField(
        max_length=20,
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.CREATED
    )

    def __str__(self):
        return f"{self.customer_name} - {self.status}"
