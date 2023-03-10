from products.exceptions import ProductAlreadyExistError
from rest_framework.views import Response, status
from products.models import Product

class ProductsMixin:
    def create(self, request, *args, **kwargs):
            find_product = Product.objects.filter(name=self.request.data["name"]).first()
            try:
                if find_product:
                    raise ProductAlreadyExistError(
                        "You have already registered this product."
                    )
                
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)

                return Response(
                    serializer.data, status=status.HTTP_201_CREATED, headers=headers
                )
            
            except ProductAlreadyExistError as e:
                return Response(
                    {"Error": e.message},
                    status.HTTP_400_BAD_REQUEST,
                )