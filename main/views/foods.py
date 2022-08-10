from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import FoodCategory
from main.serializers.food_category import FoodListSerializer


class FoodsListView(APIView):
    def get(self, request):
        # prefetch_related(food) -> for get all foods with 1 request to db
        # prefetch_related(food__additional) -> for get additional foods with 1 request to db

        queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related('food__additional').distinct()
        serializer = FoodListSerializer(instance=queryset, many=True)
        return Response(serializer.data)
