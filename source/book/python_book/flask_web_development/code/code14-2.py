class User(db.Model):
    # ...

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY']) 
        try:
            data = s.loads(token)
        except:
            return None

        return User.query.get(data['id'])
