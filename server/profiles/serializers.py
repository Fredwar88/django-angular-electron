from rest_framework import serializers
from profiles.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile model serializer.
    """
    class Meta:
        model = Profile
        fields = ('about', 'from_location', 'live_location', 'birthdate', 'rank')
