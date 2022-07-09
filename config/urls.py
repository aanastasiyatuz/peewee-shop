from account.views import register
from shop.views import create_product, product_list, product_detail, product_update, create_comment

urlpatterns = [
    ('register/', register),

    ('create-product/', create_product),
    ('products/', product_list),
    ('product-detail/id', product_detail),
    ('product-update/id', product_update),

    ('create-comment/', create_comment),
]