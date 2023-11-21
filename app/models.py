from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app import db
from sqlalchemy import Column,Integer,String,ForeignKey,Float,Boolean,Enum
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100),
                    default='https://cdn.tgdd.vn/Products/Images/42/248293/Xiaomi-11T-White-1-2-3-600x600.jpg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__=='__main__':
    from app import app
    with app.app_context():
        c1 = Category(name='Mobile')
        c2 = Category(name='Tablet')
        c3 = Category(name='Desktop')
        p1 = Product(name='iPhone 13', price=21000000, category_id=1)
        p2 = Product(name='iPad Pro 2023', price=21000000, category_id=2)
        p3 = Product(name='Galaxy Tab S9', price=24000000, category_id=2)
        p4 = Product(name='Galaxy S23', price=29000000, category_id=1)
        p5 = Product(name='iPhone 15 Pro Max', price=25000000, category_id=1)
        p6 = Product(name='iPhone 13 Pro Max', price=23000000, category_id=1)
        import hashlib
        u = User(name='Admin', username='admin',password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),user_role=UserRoleEnum.ADMIN)
        db.session.add(u)
        db.session.commit()
        # db.session.add_all([p1, p2, p3, p4, p5, p6])
        # db.session.commit()
        # import hashlib
        # hashlib.md5("abc@123").hexdigest()
        # db.create_all()
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()
