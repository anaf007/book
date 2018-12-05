class Post(db.Model):
    # ...
    def to_json(self):
        json_post = {
            'url': url_for('api.get_post', id=self.id, _external=True),
            'body': self.body,
            'body_html': self.body_html,
            'timestamp': self.timestamp,
            'author': url_for('api.get_user', id=self.author_id,
                    _external=True),
            'comments': url_for('api.get_post_comments', id=self.id,
                    _external=True)
            'comment_count': self.comments.count()
        }
        return json_post