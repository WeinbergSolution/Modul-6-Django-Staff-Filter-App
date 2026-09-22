### -------- BACKEND 6 - Django Datenbank und Adminpane ---------------- ###

## ----- Example 1: Django Admin – Buchungssystem für Veranstaltungen ----##

# ------------------- Base einrichten ------------------------- #
# ------------------- 1. Repository klonen -------------------- #

# Aufgabenstellung:
# https://hackmd.io/@mtUtNKDMTzWHLKW5U9RnOw/B1cIZfCAll?utm_source=chatgpt.com

# Anleitung zum Einrichten des Repositories:
# https://hackmd.io/@mtUtNKDMTzWHLKW5U9RnOw/HkKF0C6Rlx

# Repository:
# https://github.com/Developer-Akademie-AA/BE_staff_filter_app_teilnehmer


# 1. Repository klonen

# Das bestehende Projekt klonen.

git clone <REPOSITORY-LINK>

# Falls direkt in den aktuell geöffneten leeren Ordner geklont werden soll:

git clone <REPOSITORY-LINK> .


# 2. Virtuelle Umgebung einrichten

# Virtuelle Umgebung erstellen:

python -m venv .venv

# In der Command Prompt (CMD) aktivieren:

.venv\Scripts\activate


# 3. Abhängigkeiten installieren

# Aktuell installierte Pakete prüfen:

pip freeze

# Abhängigkeiten aus der requirements.txt installieren:

pip install -r requirements.txt

# Anschließend prüfen:

pip freeze


# 4. Django Apps prüfen

# In core/settings.py prüfen, ob bookings_app und events_app
# unter INSTALLED_APPS registriert sind.

"""
INSTALLED_APPS = [
    ...
    'bookings_app',
    'events_app',
]
"""


# 5. Migrationen ausführen

# Laut Aufgabenstellung sollten die Migrationen bereits vorhanden sein.
# In unserem Repository waren für bookings_app und events_app jedoch
# keine passenden Migrationen für die vorhandenen Models vorhanden.

# Django meldete:
# "Your models in app(s): 'bookings_app', 'events_app' have changes
# that are not yet reflected in a migration."

# Deshalb mussten zunächst Migrationen erstellt werden:

python manage.py makemigrations

# Anschließend werden die Migrationen auf die Datenbank angewendet:

python manage.py migrate


# 6. Lokalen Server starten

python manage.py runserver


# Falls Fehler auftreten:
# settings.py, INSTALLED_APPS, Datenbankeinstellungen,
# Pfade und eventuell benötigte .env-Dateien prüfen.



#                               Base eingerichtet 




# ------------------- 2. Seed-Daten einfügen ------------------- #

# Die vorbereiteten Seed-Daten befinden sich in der populate.py.

# Mit folgendem Befehl wird die Django Shell gestartet
# und der Inhalt der populate.py darin ausgeführt.

# Wichtig: Den Befehl im Command Prompt (cmd) ausführen.

python manage.py shell < populate.py


# Dadurch werden die vorbereiteten Testdaten
# in die Datenbank eingefügt.

# Seed-Daten dienen dazu, die Datenbank schnell mit
# Beispieldaten für die weiteren Übungen zu befüllen.



#                                    Erledigt 




# ------------------- 3. Server starten ------------------- #

# Django Development Server starten.

python manage.py runserver


# Anschließend die Mitarbeiter-Seite im Browser öffnen:

# http://127.0.0.1:8000/employees/


# Auf dieser Seite werden die Ergebnisse der folgenden
# Aufgaben später ausgegeben.


#                                   Erledigt 




# ------------------- 4. Filter erstellen --------------------- #

# In dieser Aufgabe werden Mitarbeiter mit verschiedenen QuerySets
# aus der Datenbank abgefragt, gefiltert und im Template ausgegeben.


# ------------------- Anleitung Filter und Ausgabe ------------------- #

# Grundlegender Ablauf:
# Datenbank → QuerySet → Context → Template → Ausgabe


# 1. Daten aus der Datenbank holen / filtern

# Beispiel:
employees_over_3000 = Employee.objects.filter(salary__gt=3000)


# 2. QuerySet in den Context (Dictionary) legen

context = {
    'employees_over_3000': employees_over_3000,
}


# 3. Context an das Template übergeben

return render(request, 'employee_list.html', context)


# 4. QuerySet im HTML durchlaufen

# {% for employee in employees_over_3000 %}
#     <ul>
#         <li>{{ employee.name }}</li>
#     </ul>
# {% empty %}
#     <li>No employee with salary over 3000.</li>
# {% endfor %}


# ------------------- Aufgabe 1 ------------------- #

# Alle Mitarbeiter aus der Datenbank holen.

employees = Employee.objects.all()

# Im Template können anschließend die benötigten Felder
# des jeweiligen Employee-Objekts ausgegeben werden:

# {{ employee.name }}
# {{ employee.department }}
# {{ employee.salary }}


# ------------------- Aufgabe 2 ------------------- #

# Mitarbeiter mit einem Gehalt über 3000 € filtern.

employees_over_3000 = Employee.objects.filter(salary__gt=3000)

# __gt = greater than / größer als


# ------------------- Aufgabe 3 ------------------- #

# Mitarbeiter mit einem Gehalt von mindestens 5000 € filtern.

employees_at_least_5000 = Employee.objects.filter(salary__gte=5000)

# __gte = greater than or equal / größer oder gleich


# ------------------- Zusatzaufgabe 4 ------------------- #

# Zuerst nur Mitarbeiter aus der Abteilung Sales filtern.

sales_employees = Employee.objects.filter(
    department__name="Sales"
)

# department ist ein ForeignKey.
# Mit department__name greifen wir auf das Feld "name"
# des verbundenen Department-Objekts zu.

# Anschließend den Durchschnitt des Gehalts berechnen.

sales_average = sales_employees.aggregate(
    Avg('salary')
)['salary__avg']

# aggregate() liefert hier ein Dictionary zurück:
# {'salary__avg': Wert}

# Mit ['salary__avg'] wird nur der berechnete Wert entnommen.

# Da sales_average nur ein einzelner Wert ist,
# wird im HTML keine for-Schleife benötigt:

# {{ sales_average|floatformat:2 }}

# floatformat:2 begrenzt die Ausgabe auf zwei Nachkommastellen.


# ------------------- Zusatzaufgabe 5 ------------------- #

# Alle Mitarbeiter aus HR ausschließen und anschließend
# nur Mitarbeiter auswählen, die vor dem 01.01.2022
# eingestellt wurden.

employees_no_hr = Employee.objects.exclude(
    department__name="HR"
).filter(
    hire_date__lt=date(2022, 1, 1)
)

# exclude() schließt Datensätze aus.
# __lt = less than / kleiner als bzw. bei Datum "vor".


# ------------------- Context ------------------- #

# Alle benötigten Ergebnisse werden über den Context
# an das Template übergeben.

context = {
    'employees': employees,
    'employees_over_3000': employees_over_3000,
    'employees_at_least_5000': employees_at_least_5000,
    'sales_average': sales_average,
    'employees_no_hr': employees_no_hr,
}

return render(request, 'employee_list.html', context)


# ------------------- Wichtig ------------------- #

# QuerySets und Berechnungen gehören in die View.
# Das Template ist für die Darstellung der Ergebnisse zuständig.

# Mehrere Objekte:
# {% for employee in employees %}
#     {{ employee.name }}
# {% endfor %}

# Einzelner berechneter Wert:
# {{ sales_average }}


#                            Erledigt 





# ------------------- 5. Ergebnisse rendern ------------------- #

# Die Ergebnisse der QuerySets werden in der employee_list.html
# dargestellt.

# Die benötigten Daten wurden zuvor über den Context
# von der View an das Template übergeben.

# Beispiel Context:
# context = {
#     'employees': employees,
#     'employees_over_3000': employees_over_3000,
#     'employees_at_least_5000': employees_at_least_5000,
#     'sales_average': sales_average,
#     'employees_no_hr': employees_no_hr,
# }


# QuerySets mit mehreren Mitarbeitern werden
# im Template mit einer for-Schleife durchlaufen.

# Beispiel:
# {% for employee in employees_over_3000 %}
#     <ul>
#         <li>{{ employee.name }}</li>
#     </ul>
# {% empty %}
#     <li>No employee found.</li>
# {% endfor %}


# Auf einzelne Felder eines Employee-Objekts
# kann direkt zugegriffen werden:

# {{ employee.name }}
# {{ employee.department }}
# {{ employee.salary }}


# Einzelne berechnete Werte benötigen keine for-Schleife.

# Beispiel Durchschnittsgehalt:
# {{ sales_average|floatformat:2 }} €


# Damit ist der Ablauf vollständig:

# Datenbank
# → QuerySet / Berechnung in der View
# → Context
# → employee_list.html
# → Ausgabe im Browser


# ------------------- 5. Erledigt ------------------- #