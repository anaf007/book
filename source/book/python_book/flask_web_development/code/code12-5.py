@main.route('/followers/<username>')
def followers(username):
    user = User.query.filter_by(username=username).first() 
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = user.followers.paginate(
            page, per_page=current_app.config['FLASKY_FOLLOWERS_PER_PAGE'],
            error_out=False)
    follows = [{'user': item.follower, 'timestamp': item.timestamp} for item in pagination.items]

    return render_template('followers.html', 
            user=user, 
            title="Followers of",
            endpoint='.followers', 
            pagination=pagination,
            follows=follows)
