from rest_framework import generics
from rest_framework.response import Response
from main.models import Person
from main.serializers import PersonSerializer

from django.core.cache import cache
import time


class PersonAPI(generics.ListAPIView, generics.CreateAPIView):
    queryset = Person.objects
    serializer_class = PersonSerializer


    # def get(self, request):
    #     qs = Person.objects.all()
    #     data_from_cache = cache.get('my_data')
    #     if data_from_cache:
    #         return Response(data_from_cache)
    #     else:
    #         serializer = self.serializer_class(qs, many=True)
    #         cache.set("my_data", serializer.data)
    #         return Response(serializer.data)

    def post(self, request):
        cache.delete('my_data')
        return super().post(request)


    def get(self, request):
        # qs = Person.objects.all()
        # qs = Person.objects.only("first_name", "last_name")
        qs = Person.objects\
        .select_related('profile', 'profile_b', 'profile_c')


        ## STANDARD ##
        # data = self.serializer_class(qs, many=True).data

        # return Response(data)

        ## STANDARD ##


        ## NO SERIALIZATION ##
        self.queryset = self.queryset.values(
            'first_name', 'last_name',
            'profile', 'column_a', 'column_b', 'column_c', 'column_d', 'column_e',
            'profile_b', 'profile_b__column_a', 'profile_b__column_b', 'profile_b__column_c', 'profile_b__column_d', 'profile_b__column_e',
            'profile_c', 'profile_c__column_a', 'profile_c__column_b', 'profile_c__column_c', 'profile_c__column_d', 'profile_c__column_e',
        )
        return Response(self.queryset)
        ## NO SERIALIZATION ##


        # qs = Person.objects.select_related('profile', 'profile_b', 'profile_c').only(
        #     "first_name", "last_name",
        #     "profile__id", "profile__name",
        #     "profile_b__id", "profile_b__name",
        #     "profile_c__id", "profile_c__name"
        # )



        # data_from_cache = cache.get('big_query_1')
        # if data_from_cache:
        #     print("found data in cache")
        #     return Response(data_from_cache)
        # else:
        #     print("no data in cache")
        #     data = self.serializer_class(qs, many=True).data
        #     cache.set('big_query_1', data)
        #     return Response(data)
