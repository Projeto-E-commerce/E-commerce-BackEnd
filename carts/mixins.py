from django.shortcuts import get_object_or_404
from rest_framework.views import Response, status
from carts.models import CartProduct
from carts.serializer import CartProductSerializer
from products.models import Product


class CartMixin:
    def post(self, request, *args, **kwargs):
        product_id = kwargs["pk"]
        cart_product = CartProduct.objects.filter(
            cart=request.user.cart,
            product__id=product_id,
            active=True,
        ).first()
        if cart_product is not None:
            cart_product.product_count += int(
                request.data["product_count"],
            )
            cart_product.save()
            serializer = CartProductSerializer(cart_product)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            get_product = get_object_or_404(
                Product,
                id=product_id,
            )
            cart_order = CartProduct.objects.create(
                cart=request.user.cart,
                product=get_product,
                product_count=int(
                    request.data["product_count"],
                ),
            )
            serializer = CartProductSerializer(cart_order)
            return Response(
                serializer.data,
                status.HTTP_201_CREATED,
            )
        