from flask.ext.mail import Message
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]' 
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
        sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to]) 
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)