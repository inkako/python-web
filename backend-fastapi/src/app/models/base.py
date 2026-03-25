from tortoise import Model, fields


class BaseModel(Model):
    id = fields.BigIntField(pk=True, index=True)

    class Meta:
        abstract = True


class TimestampMixin:
    created_at = fields.DatetimeField(auto_now_add=True, index=True)
    updated_at = fields.DatetimeField(auto_now=True, index=True)
