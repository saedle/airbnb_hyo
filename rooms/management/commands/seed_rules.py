from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates house rules"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you that I love IU"
    #     )

    def handle(self, *args, **options):
        rules = ["Be nice", "Don't smoke", "Don't Drink", "No girl"]
        for r in rules:
            HouseRule.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(rules)} rules created"))
