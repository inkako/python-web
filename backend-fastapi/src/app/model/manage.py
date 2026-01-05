from tortoise import fields

from .base import BaseModel, TimestampMixin
from app.enum import MenuType


class User(BaseModel, TimestampMixin):
    username = fields.CharField(max_length=32, unique=True, description="用户名称")
    alias = fields.CharField(max_length=48, null=True, description="昵称", index=True)
    email = fields.CharField(max_length=255, unique=True, description="邮箱", index=True)
    phone = fields.CharField(max_length=20, null=True, description="手机号", index=True)
    password = fields.CharField(max_length=128, null=True, description="密码")
    is_active = fields.BooleanField(default=True, description="是否激活", index=True)
    is_superuser = fields.BooleanField(default=False, description="是否为超级用户", index=True)
    last_login = fields.DatetimeField(null=True, description="最后登录时间", index=True)
    dept_id = fields.IntField(null=True, description="部门ID", index=True)
    roles = fields.ManyToManyField(model_name="model.Role", related_name="users", through="user_role")

    class Meta:
        table = "user"
        table_description = "用户表"


class Role(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=128, unique=True, description="名称", index=True)
    desc = fields.CharField(max_length=512, null=True, description="描述")
    menus = fields.ManyToManyField(model_name="model.Menu", related_name="roles", through="role_menu")
    apis = fields.ManyToManyField(model_name="model.Api", related_name="roles", through="role_api")

    class Meta:
        table = "role"
        table_description = "角色表"


class Menu(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=128, unique=True, description="名称", index=True)
    desc = fields.CharField(max_length=512, null=True, description="描述")
    menu_type = fields.CharEnumField(MenuType, null=True, description="类型")
    icon = fields.CharField(max_length=128, null=True, description="图标")
    path = fields.CharField(max_length=512, null=True, description="路径")
    order = fields.IntField(default=0, null=True, description="排序")
    is_hidden = fields.BooleanField(default=False, description="是否隐藏")
    parent_id = fields.IntField(null=True, description="父ID")

    class Meta:
        table = "menu"
        table_description = "菜单表"


class Api(BaseModel, TimestampMixin):
    path = fields.CharField(max_length=512, description="接口路径", index=True)
    method = fields.CharField(max_length=16, description="请求方法")
    name = fields.CharField(max_length=128, unique=True, description="接口名称", index=True)
    desc = fields.CharField(max_length=512, null=True, description="接口描述")

    class Meta:
        table = "api"
        table_description = "接口表"
