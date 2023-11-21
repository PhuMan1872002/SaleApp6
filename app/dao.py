from app import login,app
from app.models import Category,Product,User
import hashlib
def load_categories():
    return Category.query.all()


def load_products(kw=None,cate_id=None,page=None):
    products=Product.query

    if kw:
        products=products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1)*page_size

        return products.slice(start, start + page_size)


    return products.all()

def count_product():
    return Product.query.count()


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()

def get_user_by_id(id):
    return User.Query.get(id)