from django.contrib.auth import get_user_model
from rest_framework import serializers

# Serialisers take json and convert it to python objects and vice versa.
# They are used to validate data and convert it to a format that can
# be used by the model. Serialisers are also used to convert data to a
# format that can be used by the API.


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "name")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    # def update(self, instance, validated_data):
    #     """Update a user, setting the password correctly and return it"""
    #     password = validated_data.pop("password", None)
    #     user = super().update(instance, validated_data)
    #
    #     if password:
    #         user.set_password(password)
    #         user.save()
    #
    #     return user
