from myapp.models import LoginTotalUsers

objects = LoginTotalUsers.objects.all()

unique_ids = {}

for obj in objects:
    employee_record_ids = obj.employee_ids
    for key in employee_record_ids.keys():
        unique_ids[key] = key
