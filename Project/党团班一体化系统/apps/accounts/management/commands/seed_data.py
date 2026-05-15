"""
Management command to seed 50 users across 2 classes.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from apps.accounts.models import User, PartyArchive
from datetime import date


class Command(BaseCommand):
    help = "Seed database with 50 users (2 classes x 25 students)"

    def handle(self, *args, **options):
        if User.objects.count() >= 50:
            self.stdout.write(self.style.WARNING("Users already exist, skipping seed"))
            return

        DEFAULT_PASSWORD = make_password("123456")

        classes = ["计算机2201", "计算机2202"]
        last_names = [
            "张", "李", "王", "刘", "陈", "杨", "赵", "黄", "周", "吴",
            "徐", "孙", "马", "朱", "胡", "郭", "何", "高", "林", "郑",
            "罗", "梁", "谢", "宋", "唐",
        ]
        user_id = 0

        for class_name in classes:
            for i in range(25):
                user_id += 1
                student_id = f"2024{user_id:04d}"
                name = f"{last_names[i]}{chr(ord('A') + (i % 26))}"

                if i == 0:
                    role = "班长"
                elif i == 1:
                    role = "团支书"
                else:
                    role = "普通学生"

                political = "团员" if i <= 20 else "群众"

                user = User.objects.create(
                    id=user_id,
                    username=student_id,
                    student_id=student_id,
                    name=name,
                    password=DEFAULT_PASSWORD,
                    gender="男" if i % 2 == 0 else "女",
                    class_name=class_name,
                    phone=f"138{user_id:08d}",
                    political_status=political,
                    enrollment_date=date(2024, 9, 1),
                    role=role,
                )

                PartyArchive.objects.create(
                    user=user,
                    political_identity=political,
                    join_league_date=date(2023, 5, 1) if political != "群众" else None,
                    org_relation_status="正常",
                )

        self.stdout.write(self.style.SUCCESS(f"Seeded {user_id} users successfully"))
