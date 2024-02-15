# DRF Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_202_ACCEPTED

# Model Imports
from .models import Wishlist
from rooms.models import Room

# Serializer Imports
from .serializers import RoomsWishlistSerializer


class RoomsWishlists(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serializer = RoomsWishlistSerializer(
            all_wishlists,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomsWishlistSerializer(data=request.data)
        if serializer.is_valid():
            wishlist = serializer.save(user=request.user)
            serializer = RoomsWishlistSerializer(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RoomsWishlistDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        serializer = RoomsWishlistSerializer(
            wishlist,
            context={"request": request},
        )
        return Response(serializer.data)

    def delete(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        wishlist.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        serializer = RoomsWishlistSerializer(
            wishlist,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            wishlist = serializer.save()
            serializer = RoomsWishlistSerializer(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RoomsWishlistToggle(APIView):

    def get_wishlist(self, pk, user):
        try:
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get_room(self, room_pk):
        try:
            return Room.objects.get(pk=room_pk)
        except Room.DoesNotExist:
            raise NotFound

    def put(self, request, pk, room_pk):
        wishlist = self.get_wishlist(pk, request.user)
        room = self.get_room(room_pk)
        if wishlist.rooms.filter(pk=room.pk).exists():
            wishlist.rooms.remove(room)
        else:
            wishlist.rooms.add(room)
        return Response(status=HTTP_202_ACCEPTED)
