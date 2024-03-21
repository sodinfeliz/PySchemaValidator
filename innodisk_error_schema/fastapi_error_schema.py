from .base_error_schema import ErrorSchema


class FastAPIErrorSchema(ErrorSchema):
    
    @classmethod
    def validation_error(cls, **kwargs):
        """Factory method to create an instance for a validation error."""
        defaults = {
            "type": "validation_error",
            "msg": "Validation failed.",
        }
        defaults.update(kwargs)
        return cls(**defaults)
    
    @classmethod
    def value_error(cls, **kwargs):
        """Factory method to create an instance for a value error."""
        defaults = {
            "type": "value_error",
            "msg": "Value error.",
        }
        defaults.update(kwargs)
        return cls(**defaults)
