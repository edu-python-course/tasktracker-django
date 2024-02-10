# This file contains a fake tasks db
import datetime

tasks = [
    {
        "pk": 41,
        "summary": "Add email subscription feature",
        "description":
            "Brush each side of the quinoa with one cup of turkey. "
            "Truffels pilaf has to have a sliced, quartered quinoa component. "
            "When squeezing large gingers, be sure they are room temperature.",
        "completed": False,
        "created_at": datetime.datetime.strptime(
            "2022-05-01 23:18:05",
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.datetime.strptime(
            "2022-05-01 23:18:05",
            "%Y-%m-%d %H:%M:%S"
        ),
        "assignee": None,
        "reporter": {
            "get_full_name": lambda: "Pippin Sackville-Baggins",
        },
    },
    {
        "pk": 42,
        "summary": "Add user avatar feature",
        "description":
            "This coordinates has only been desired by a unrelated teleport. "
            "This alarm has only been united by a final nano machine. "
            "Galaxy at the center that is when spheroid cashless walk.",
        "completed": True,
        "created_at": datetime.datetime.strptime(
            "2021-02-23 16:45:46",
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.datetime.strptime(
            "2023-08-03 04:58:12",
            "%Y-%m-%d %H:%M:%S"
        ),
        "assignee": {
            "get_full_name": lambda: "Dora Headstrong",
        },
        "reporter": {
            "get_full_name": lambda: "Pippin Sackville-Baggins",
        },
    },
    {
        "pk": 43,
        "summary": "Fix formatting issues on blog posts",
        "description": "",
        "completed": False,
        "created_at": datetime.datetime.strptime(
            "2022-05-01 23:18:05",
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.datetime.strptime(
            "2022-05-01 23:18:05",
            "%Y-%m-%d %H:%M:%S"
        ),
        "assignee": None,
        "reporter": {
            "get_full_name": lambda: "Dora Headstrong",
        },
    },
]


def get_task(pk: int) -> dict:
    for task in tasks:
        if task["pk"] == pk:
            return task
