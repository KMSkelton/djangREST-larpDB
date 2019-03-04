from rest_framework import serializers
from attributes.models import Attribute

class AttributeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Attribute
    # fields = "__all__"
    # can explicitly add the fields needed if not all are supposed to be included
    fields = (
      'id',
      'attribute_name',
      'attribute_description'
    )
