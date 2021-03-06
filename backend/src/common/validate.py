from schema import SchemaError


class InputValidate:
    def __init__(self, schema: dict = None):
        self.schema = schema

    @staticmethod
    def validate_json(data: dict, schema: dict = None):
        """
        validate info
        :param data:
        :param schema:
        :return:
        """
        try:
            return schema.validate(data)
        except SchemaError:
            return False

