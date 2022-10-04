"""
Serializers for the recipe api view
"""
from rest_framework import serializers

from core.models import Recipe, Tag


class RecipeSerializer(serializers.ModelSerializer):
    """Serializers for recipes"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializers for recipe details"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    """Serializers for tags"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only = ['id']
