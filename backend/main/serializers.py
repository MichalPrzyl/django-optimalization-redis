from rest_framework import serializers
from main.models import Person, Profile, ProfileB, ProfileC


#
# class ProfileRelatedField(serializers.RelatedField):
#
#     def to_representation(self, instance):
#
#         return_obj = {
#             "id": instance.id
#         }
#
#         print(f"return_obj: {return_obj}")
#
#         return instance.id
#
#
#     def to_internal_value(self, data):
#         return Profile.objects.get(id=data)


class ProfileRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        """Konwersja obiektu na JSON"""
        return {
            # "id": instance.id,
            "name": instance.name  # Dodajemy więcej informacji o profilu
        }

    def to_internal_value(self, data):
        """Konwersja ID lub słownika na obiekt Profile"""
        if isinstance(data, dict):
            data = data.get("id")  # Pobieramy ID ze słownika, jeśli przekazano cały obiekt

        try:
            return Profile.objects.get(id=data)
        except (TypeError, ValueError, Profile.DoesNotExist):
            raise serializers.ValidationError("Invalid profile ID.")

    def get_choices(self, cutoff=None):
        """Naprawa błędu `unhashable type: 'dict'`"""
        queryset = Profile.objects.all()
        return {item.id: self.display_value(item) for item in queryset}

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        # fields = ['name']
        model = Profile
        # read_only_fields = ['column_a', 'column_b', 'column_c', 'column_d', 'column_e']


class ProfileBSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        # fields = ['name']
        model = ProfileB
        # read_only_fields = ['column_a', 'column_b', 'column_c', 'column_d', 'column_e']

class ProfileCSerializer(serializers.ModelSerializer):
    class Meta:
        # read_only_fields = ['column_a', 'column_b', 'column_c', 'column_d', 'column_e']
        fields = '__all__'
        # fields = ['name']
        model = ProfileC

class PersonSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()
    profile_b = ProfileBSerializer()
    profile_c = ProfileCSerializer()

    # profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    # profile = ProfileRelatedField(queryset=Profile.objects, many=False)

    class Meta:
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'profile', 'profile_b', 'profile_c']
        model = Person
        # optimize_related = True

