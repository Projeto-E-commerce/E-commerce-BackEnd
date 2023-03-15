from django.shortcuts import get_object_or_404
from rest_framework.views import Response, status
from carts.models import CartProduct
from orders.exceptions import StorageError
from orders.models import Order
from products.models import Product
from coupons.models import Coupon
from decimal import Decimal
import ipdb


class OrderMixin:
    def post(self, request):
        code = False
        coupon_owner = False
        if "coupon" in request.data:
            code = request.data["coupon"]
            coupon_owner = get_object_or_404(Coupon, code=code)

        cart_id = request.user.cart
        products_cart = CartProduct.objects.all().filter(
            cart_id=cart_id,
            active=True,
        )

        salesmans = set([product.product.owner for product in products_cart])

        order_return = {}
        for salesman in salesmans:
            products_for_salesman = products_cart.filter(
                product__owner=salesman,
            )

            price_total = 0
            products_list = []
            for product in products_for_salesman:
                product_get = get_object_or_404(Product, id=product.product.id)
                price_final = product_get.price * product.product_count
                if coupon_owner:
                    if coupon_owner.owner == salesman:
                        desconto_decimal = coupon_owner.discount / Decimal("100")
                        product_price = product_get.price * product.product_count
                        valor_desconto = product_price * desconto_decimal
                        price_final = product_price - valor_desconto
                        

                price_total += price_final
                products_list.append(
                    {
                        "id": product_get.id,
                        "name": product_get.name,
                        "category": product_get.category,
                        "description": product_get.description,
                        "price": str(round(price_final, 2)),
                        "count": product.product_count,
                    }
                )
                try:
                    if product.product_count > product_get.storage:
                        raise StorageError(
                            f"You can't buy '{product_get.name}'. There are {product_get.storage} items in storage."
                        )
                    product_get.storage -= product.product_count
                    product_get.save()
                except StorageError as e:
                    return Response(
                        {"Error": e.message},
                        status.HTTP_400_BAD_REQUEST,
                    )

                product.active = False
                product.save()

            # if coupon_owner.owner == salesman:
            #     desconto_decimal = coupon_owner.discount / Decimal('100')
            #     valor_desconto = price_total * desconto_decimal
            #     price_final = price_total - valor_desconto
            # else:
            #     price_final = price_total

            Order.objects.create(
                total_order=price_final,
                user=self.request.user,
                salesman=salesman,
                products_list=products_list,
            )

            order_return[salesman.username] = products_list

        return Response(order_return, status.HTTP_201_CREATED)
