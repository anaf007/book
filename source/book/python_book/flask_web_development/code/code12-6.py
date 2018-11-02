@app.route('/', methods = ['GET', 'POST'])
def index():
    # ...
    show_followed = False
    if current_user.is_authenticated():
        show_followed = bool(request.cookies.get('show_followed', ''))
        if show_followed:
            query = current_user.followed_posts
        else:
            query = Post.query
        pagination = query.order_by(Post.timestamp.desc()).
            paginate(page, 
                per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                error_out=False)
        posts = pagination.items
        return render_template('index.html', 
            form=form, posts=posts,
            show_followed=show_followed, 
            pagination=pagination)
