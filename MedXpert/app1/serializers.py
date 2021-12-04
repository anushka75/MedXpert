from rest_framework import serializers
from .models import Profile

Users_CHOICES = (
   ('P', 'Patient'),
   ('D', 'Doctor')
)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['user','first_name','last_name','email','password','confirm_password']

    def save(self):
        profile= Profile(
            user=self.validated_data['user'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],
            confirm_password=self.validated_data['confirm_password'],
        )
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'password':'Passwords must match'})
        # profile.set_password(password)
        profile.save()
        return profile
    