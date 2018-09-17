from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,  primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    blogs = db.relationship('Blog',backref = 'author',lazy="dynamic") 
    comments = db.relationship('Comment', backref = 'author', lazy = "dynamic")
    
    def save_user(self, user):
        db.session.add(user)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username} {self.bio} {self.email}'

class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    content = db.Column(db.String(255))
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'blog',lazy="dynamic")

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls,id):
        blogs = Blog.query.filter_by(blog_id=id).all()
        return blogs

    def delete_blog(self):
        db.session.query(Blog).delete()
        db.session.commit() 

    def __repr__(self):
        return f'User {self.title}'

class Comment(db.Model):
    __tablename__= 'comments'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comment.query.filter_by(comment_id=id).all()
        return comments     

    def __repr__(self):
        return f'Comment{self.title}'       
    


