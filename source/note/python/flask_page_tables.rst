Flask分表
=======================================================================

参考链接：https://www.bbsmax.com/A/Gkz120AZJR/

如下表::

    CREATE TABLE `goods_desc_0` (
      `goods_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '商品id',
      `goods_desc` text NOT NULL COMMENT '商品详细描述',
      PRIMARY KEY (`goods_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='商品信息详情'
    CREATE TABLE `goods_desc_1` (
      `goods_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '商品id',
      `goods_desc` text NOT NULL COMMENT '商品详细描述',
      PRIMARY KEY (`goods_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='商品信息详情'


::

    class GoodsDesc(db.Model):
        __tablename__ = 'goods_desc'
        goods_id = db.Column(db.Integer, primary_key=True)
        goods_desc = db.Column(db.Text, default=None)
        def __str__(self):
            return "GoodsDesc => { \
    goods_id:%d, goods_desc:'%s'}" % (
    self.goods_id, self.goods_desc)
        __repr__ = __str__
    # 代码示例
    goods_id = 101
    table_index = goods_id%2
    table_name = 'goods_desc_%d' % table_index
    GoodsDesc.__table__.name = table_name
    gd = GoodsDesc.query.filter(GoodsDesc.goods_id == goods_id).first()
    # 这样写虽然也能工作，但是是非常危险的，因为GoodsDesc.__table__是静态全局变量，
    # 而且不是web程序request级别的，是app context的，非常不安全。

如下就优雅了::

    class GoodsDesc(object):
        _mapper = {}
        @staticmethod
        def model(goods_id):
            table_index = goods_id%100
            class_name = 'GoodsDesc_%d' % table_index
            ModelClass = GoodsDesc._mapper.get(class_name, None)
            if ModelClass is None:
                ModelClass = type(class_name, (db.Model,), {
                    '__module__' : __name__,
                    '__name__' : class_name,
                    '__tablename__' : 'goods_desc_%d' % table_index,
                    'goods_id' : db.Column(db.Integer, primary_key=True),
                    'goods_desc' : db.Column(db.Text, default=None),
                })
                GoodsDesc._mapper[class_name] = ModelClass
            cls = ModelClass()
            cls.goods_id = goods_id
            return cls
    # 外部代码调用如例如下：
    # -----------------------
    # 新增插入
    gdm = GoodsDesc.model(goods_id)
    gdm.goods_desc = 'desc'
    db.session.add(gd)
    # 查询
    gdm = GoodsDesc.model(goods_id)
    gd = gdm.query.filter_by(goods_id=goods_id).first()
