from typing import Optional

import pandas as pd
from api.models import Task
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    """
    Custom Django command to refresh the data entries in `Task` model based on CSV file.
    """

    help = "Custom Django command to refresh the data entries in Task model based on CSV file."

    def add_arguments(self, parser) -> None:
        return parser.add_argument(
            "--commit",
            "-c",
            action="store_true",
            default=False,
            help="Confirm to refresh Task data.",
        )

    @transaction.atomic
    def handle(self, **options) -> Optional[str]:
        savepoint = transaction.savepoint()

        file_path = "/home/vivaain/workspace/django-rest-tutorial/tutorialProject1/test-data.csv"

        data_frame = pd.read_csv(file_path, sep=";")

        import pdb

        for _, data in data_frame.iterrows():
            Task.objects.update_or_create(
                title=data["title"],
                completed=data["completed"],
            )
            pdb.set_trace()

        if options["commit"]:
            self.stdout.write(self.style.SUCCESS("Successfully refreshed Task data."))
            transaction.savepoint_commit(savepoint)
        else:
            self.stdout.write(self.style.WARNING("Ran command without commit."))
            transaction.savepoint_rollback(savepoint)
