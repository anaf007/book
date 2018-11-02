@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data,
            post=post,author=current_user._get_current_object())
        db.session.add(comment)
        flash('Your comment has been published.')
        return redirect(url_for('.post', id=post.id, page=-1))
    page = request.args.get('page', 1, type=int)
    if page == -1:
        page = (post.comments.count() - 1) / \ 
            current_app.config['FLASKY_COMMENTS_PER_PAGE'] + 1
        pagination = post.comments.order_by(Comment.timestamp.asc()).paginate( page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'], error_out=False)
        comments = pagination.items
        return render_template('post.html', posts=[post], form=form,
                comments=comments, pagination=pagination)
