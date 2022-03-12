import os
from typing import Optional

import numpy as np
import pandas as pd
from api.models import Task
from django.conf import settings
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

        BASE_DIR = getattr(settings, "BASE_DIR")
        file_path = os.path.join(BASE_DIR, "test-data.csv")
        file_path = os.path.join(file_path)

        if os.path.exists(file_path):
            if Task.objects.all().exists():
                Task.objects.all().delete()

            data_frame = pd.read_csv(file_path, sep=";")
            data_frame["completed"].replace(np.nan, False, inplace=True)

            for _, data in data_frame.iterrows():
                Task.objects.update_or_create(
                    title=data.title,
                    completed=data.completed,
                )

        if options["commit"]:
            self.stdout.write(self.style.SUCCESS("Successfully refreshed Task data."))
            transaction.savepoint_commit(savepoint)
        else:
            self.stdout.write(self.style.WARNING("Ran command without commit."))
            transaction.savepoint_rollback(savepoint)
