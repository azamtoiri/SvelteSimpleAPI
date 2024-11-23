import jsonschema
from django.core.exceptions import ValidationError


class ComponentValidator:
    @classmethod
    def validate_component(cls, component, content):
        """Validation of component content according to its JSON schema"""
        try:
            jsonschema.validate(instance=content, schema=component.schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ValidationError({
                'content': f"Validation error: {e.message}"
            })

    @classmethod
    def get_default_content(cls, component):
        """Generation of default content based on schema"""

        def generate_default(prop_schema):
            if prop_schema.get('type') == 'string':
                return ''
            elif prop_schema.get('type') == 'object':
                return {k: generate_default(v) for k, v in prop_schema.get('properties', {}).items()}
            elif prop_schema.get('type') == 'array':
                return []
            return None

        # Генерация дефолтного контента из схемы
        default_content = generate_default(component.schema)
        return default_content
