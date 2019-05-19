第四章、表单
=======================================================================


4.1 HTML表单
---------------------------------------------------------------------
内容略


4.2 使用FLask-WTF处理表单
---------------------------------------------------------------------
清单：
 - BooleanField：布尔类型，如Flask,True
 - StringField：字符串类型
 - DecimalField：小数点文本字段，如：‘1.23’
 - DateField：日期字段，格式：'%Y-%m-%d'
 - DateTimeField:日期字段，格式：'%Y-%m-%d %H:%M:%S'
 - FieldList:统一字段类型组成列表，如：FieldList(StringField('Name', [validators.required()]))
 - FloatField:浮点数类型
 - IntegerField：整形
 - SelectMultipleField：多选框
 - SelectField： 下拉列表
 - RadioField：单选框
 - TextAreaField:文本域，可接受多行输入
 - PasswordField：密码字段，输入的不会直接在浏览器明文显示
 - FileField：上传文件，但不会处理验证文件，需要手动处理
 - HiddenField：隐藏字段
 - SubmitField：按钮
 - TextField:字符串类型的别名，弃用


实例化字段常用参数:
 - label ： 字段标签label的值
 - render_kw ： 一个字段 对应html标签的属性 可以自定义class css等
 - validators ： 一个列表  包含一系列验证器
 - dafault ： 字符串或可调用的对象

常用的WTForms验证器：
 - DataRequired ：验证数据是否有效
 - Email ：验证email
 - EqualTo ： 验证两个字段值是否相同
 - InputRequired ：验证是否有数据
 - Length ：验证输入值的长度是否在给定范围
 - NumberRange ： 验证输入数字是否在给定返回
 - Optional ： 允许输入值位空并跳过其他验证
 - Regexp ： 使用正则验证
 - URL ：验证URL
 - AnyOf ：确保输入值在可选列表中
 - NoneOf ：确保输入值不在可选列表中



4.3 处理表单数据
---------------------------------------------------------------------
注意传入：{{form.csrf_token()}}


4.4 表单进阶实践
---------------------------------------------------------------------
设置错误消息语言  内容略

使用宏渲染表单 内容略

自定义验证器  内容略

全局验证器  略

文件上传  内容略

多文件上传  内容鲁尔

flask-ckeditor    富文本  已经使用过 内容略   以上这些内容再使用在逐个过来添加


单表单 多个提交按钮

单个页面多个表单