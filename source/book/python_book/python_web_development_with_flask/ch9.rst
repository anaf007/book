第九章、图片社交网站
=======================================================================

项目地址：https://github.com/greyli/albumy

flask-dropzone文件上传

flask-avatars头像处理

这里有一点可以学习，获取随机数据::

    from sqlalchemy.sql.expression import func

    def explort():
        photo = Photo.query.order_by(func.random()).limit(10)


flask-whooshee全文搜索

User.query.with_parent(xx).first()


with_parent  注意   获取父级的所有内容  

subquery()子查询

