# management/management/commands/seedPostCategories.py

from django.core.management.base import BaseCommand
from post_categories.models import Category


class Command(BaseCommand):
    help = 'Seeds the Category model with initial data'

    def handle(self, *args, **kwargs):
        categories = [
            {"name": "Technology", "description": "Articles related to technology"},
            {"name": "Travel", "description": "Articles about travel destinations"},
            {"name": "Food", "description": "Culinary delights and recipes"},
            {"name": "Fashion", "description": "Trendy fashion tips and updates"},
            {"name": "Health", "description": "Health and wellness advice"},
            {"name": "Finance", "description": "Financial planning and investment tips"},
            {"name": "Sports", "description": "Updates and analysis on sports events"},
            {"name": "Education", "description": "Insights into educational topics"},
            {"name": "Entertainment", "description": "Latest entertainment news and gossip"},
            {"name": "Science", "description": "Discoveries and breakthroughs in science"}
        ]

        for category_data in categories:
            Category.objects.get_or_create(**category_data)

        self.stdout.write(self.style.SUCCESS('Categories seeded successfully.'))
