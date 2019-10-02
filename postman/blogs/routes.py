from flask import (Blueprint, jsonify, request)
from postman import db
from postman.models import Blog

blogs = Blueprint('blogs', __name__)


# Route to return all blogs
@blogs.route('/blogs')
def blog_index():
    blogs = Blog.query.all
    data = {}

    for blog in blogs:
        data[blog.title] = {'title': blog.title, 'summary': blog.summary}

    return jsonify(data)


# Route to create a blog
@blogs.route('/blogs/new')
def blog_new():
    data = request.get_json()
    blog = Blog(title=data['title'], summary=data['summary'])
    db.session.add(blog)
    db.session.commit()

    return 'OK', 200
