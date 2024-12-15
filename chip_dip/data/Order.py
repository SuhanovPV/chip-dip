import dataclasses


@dataclasses.dataclass
class Delivery:
    country: str
    city: str
    street: str
    building: str
    delivery_type: str
    comment: str


order_delivery = Delivery(
    country='Россия',
    city='Брянск',
    street='б-р Гагарина',
    building='23',
    delivery_type='Пункты выдачи заказов',
    comment='Комментарий к заказу'
)
