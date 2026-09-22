from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):



    # Alle Mitarbeiter aus der Datenbank holen

    # 1. Zeige hier im Template eine Liste aller Mitarbeiter, ihrer Abteilung und ihres Gehalts an
    employees = Employee.objects.all()


    # 2. Mitarbeiter mit mehr als 3000 € Gehalt anzeigen

    employees_over_3000 = Employee.objects.filter(salary__gt=3000)

    # 3. Anzahl der Mitarbeiter mit mindestens 5000 € Gehalt ermitteln

    employees_at_least_5000 = Employee.objects.filter(salary__gt=4999)

    # 4. Durchschnittsgehalt des Sales-Teams berechnen

    sales_employees = Employee.objects.filter(department__name="Sales")
    sales_average = sales_employees.aggregate(Avg('salary'))['salary__avg']

    # 5. Mitarbeiter vor dem 01.01.2022 ohne HR-Abteilung ermitteln

    employees_no_hr = Employee.objects.exclude(department__name="HR").filter( hire_date__lt=date(2022, 1, 1))



    # QuerySet an das Template übergeben
    context = {
        'employees': employees,
        'employees_over_3000': employees_over_3000,
        'employees_at_least_5000': employees_at_least_5000,
        'sales_average': sales_average,
        'employees_no_hr': employees_no_hr
    }

    return render(request, 'employee_list.html', context)
















#ANleitung filter benutzen und ausgabe im html viasualisieren 
# Datenbank → QuerySet → Context → Template → Ausgabe

# # 1. Daten aus der Datenbank holen → QuerySet
# employees_over_3000 = Employee.objects.filter(salary__gt=3000)

# # 2. QuerySet in den Context (Dictionary) legen
# context = {
#     'employees': employees,
#     'employees_over_3000': employees_over_3000,
# }

# # 3. Context an das Template übergeben
# return render(request, 'employee_list.html', context)

# Und im Template:

# <!-- 4. QuerySet durchlaufen -->
# {% for employee in employees_over_3000 %}
#     <ul>
#         <li>{{ employee.name }}</li>
#     </ul>
# {% empty %}
#     <li>No employee with salary over 3000.</li>
# {% endfor %}