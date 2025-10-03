from marshmallow import Schema, fields


class CategorySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    slug = fields.Str()


class ProductSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    price = fields.Float()
    stock = fields.Int()
    image_url = fields.Str()
    category = fields.Nested(CategorySchema)


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Email()
    is_admin = fields.Bool()