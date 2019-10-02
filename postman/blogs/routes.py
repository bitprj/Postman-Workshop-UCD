from flask import (Blueprint, jsonify, request)
from postman import db
from postman.models import Blog

blogs = Blueprint('blogs', __name__)


# Route to return all blogs
@blogs.route('/blogs')
def blog_index():
    blogs = Blog.query.all()
    data = {}

    for blog in blogs:
        data[blog.title] = {'id': blog.id, 'title': blog.title, 'summary': blog.summary}

    return jsonify(data)


# Route to return a specific blog
@blogs.route('/blogs/<int:blog_id>')
def blog_show(blog_id):
    blog = Blog.query.get_or_404(blog_id)

    return jsonify({'id': blog.id, 'title': blog.title, 'summary': blog.summary})


# Route to create a blog
@blogs.route('/blogs/new', methods=['POST'])
def blog_new():
    data = request.get_json()
    blog = Blog(title=data['title'], summary=data['summary'])
    db.session.add(blog)
    db.session.commit()

    return jsonify({'id': blog.id, 'title': blog.title, 'summary': blog.summary})


# Route to edit the blog
@blogs.route('/blogs/<int:blog_id>/edit', methods=['PUT'])
def blog_edit(blog_id):
    data = request.get_json()
    blog = Blog.query.get_or_404(blog_id)

    if 'title' in data:
        blog.title = data['title']
    if 'summary' in data:
        blog.summary = data['summary']

    db.session.commit()

    return jsonify({'id': blog.id, 'title': blog.title, 'summary': blog.summary})

# Route to delete a blog
@blogs.route('/blogs/<int:blog_id>/delete', methods=['DELETE'])
def blog_delete(blog_id):
    blog = Blog.query.get_or_404(blog_id)

    db.session.delete(blog)
    db.session.commit()

    return 'OK', 200
