class User(db.Model):
    # ...
    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f)

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first() 
        if f:
            db.session.delete(f)

    def is_following(self, user): 
        return self.followed.filter_by(followed_id=user.id).first() is not None

    def is_followed_by(self, user): 
        return self.followers.filter_by(follower_id=user.id).first() is not None