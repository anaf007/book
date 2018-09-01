@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    user = User.query.filter_by(username=username).first() 
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    if current_user.is_following(user):
        flash('You are already following this user.')
        return redirect(url_for('.user', username=username)) 
        
    current_user.follow(user)
    flash('You are now following %s.' % username)

    return redirect(url_for('.user', username=username))
