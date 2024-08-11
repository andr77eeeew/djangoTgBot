from django.core.management.base import BaseCommand, CommandError
import asyncio

from bot.main_bot import bot


class Command(BaseCommand):
    help = 'Runs bot'

    def handle(self, *args, **options):
        asyncio.run(bot.polling())

