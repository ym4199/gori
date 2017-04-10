from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters

from talent.models import Talent, Curriculum, ClassImage, Registration
from talent.serializers import CurriculumSerializer, ClassImageSerializer, TalentListSerializer, \
    CurriculumWrapperSerializer, TalentShortDetailSerializer
from talent.serializers import LocationWrapperSerializers, TalentDetailSerializer
from talent.serializers import ReviewWrapperSerializer
from talent.serializers.class_image import ClassImageWrapperSerializers
from talent.serializers.registration import TalentRegistrationSerializer, TalentRegistrationWrapperSerializer

__all__ = (
    # talent
    'TalentListCreateView',
    # detail - all
    'TalentDetailView',
    # detail - fragments
    'TalentShortDetailView',
    'CurriculumListView',
    'ClassImageListView',
    'LocationRetrieveView',
    'ClassImageRetrieveView',
    'CurriculumRetrieveView',
    'ReviewRetrieveView',

    # registration
    'TalentRegistrationRetrieveView',

    # 'MyWishListRetrieve',
    # 'MyRegistrationList',
    # 'RegistrationList',

    # 'LocationList',
)

User = get_user_model()


# talent 전체 api
class TalentListCreateView(generics.ListCreateAPIView):
    serializer_class = TalentListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # pagination_class = TalentPagination

    # rest_framework의 SearchFilter 사용시
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('title', 'class_info')

    def perform_create(self, serializer):
        serializer.save(tutor=self.request.user.tutor)

    def get_queryset(self):
        queryset = Talent.objects.all()
        title = self.request.query_params.get('title', None)
        region = self.request.query_params.get('region', None)
        category = self.request.query_params.get('category', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if region is not None:
            queryset = queryset.filter(locations__region__icontains=region).distinct('pk')
        if category is not None:
            queryset = queryset.filter(category__icontains=category)

        return queryset


class LocationRetrieveView(generics.RetrieveAPIView):
    queryset = Talent.objects.all()
    serializer_class = LocationWrapperSerializers


class TalentRegistrationRetrieveView(generics.RetrieveAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentRegistrationWrapperSerializer
    #
    # def get_queryset(self):
    #     return Talent.objects.filter(pk=self.kwargs['pk'])
    # pagination_class = RegistrationPagination

    # def get(self, request, *args, **kwargs):
    #     registration = []
    #     locations = Location.objects.filter(talent=kwargs['pk'])
    #     print(locations)
    #     for location in locations:
    #         registration = location.registration_set.all()
    #     # page = self.paginate_queryset(registration)
    #     # if page is not None:
    #     #     serializer = self.get_serializer(page, many=True)
    #     #     return self.get_paginated_response(serializer.data)
    #
    #     serializer = RegistrationWrapperSerializers(registration, many=True)
    #     return Response(serializer.data)


class ClassImageRetrieveView(generics.RetrieveAPIView):
    queryset = Talent.objects.all()
    serializer_class = ClassImageWrapperSerializers


class CurriculumCreateView(generics.CreateAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer


class CurriculumRetrieveView(generics.RetrieveAPIView):
    queryset = Talent.objects.all()
    serializer_class = CurriculumWrapperSerializer


class TalentShortDetailView(generics.RetrieveAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentShortDetailSerializer


# 하나의 talent에 대한 세부 정보 api
class TalentDetailView(generics.RetrieveAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentDetailSerializer


# class LocationList(generics.ListAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer

# def create(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     serializer.save(
#         photo_set=request.data.getlist('photo')
#     )
#     headers = self.get_success_headers(serializer.data)
#     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CurriculumListView(generics.ListCreateAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer


class ClassImageListView(generics.ListCreateAPIView):
    queryset = ClassImage.objects.all()
    serializer_class = ClassImageSerializer


# class RegistrationRetrieve(generics.RetrieveAPIView):
#     queryset = Talent.objects.all()
#     serializer_class = RegistrationWrapperSerializers
#
#     def get_queryset(self):
#         return Talent.objects.filter(id=self.kwargs['pk'])


class ReviewRetrieveView(generics.RetrieveAPIView):
    queryset = Talent.objects.all()
    serializer_class = ReviewWrapperSerializer


class RegistrationListView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = TalentRegistrationSerializer
