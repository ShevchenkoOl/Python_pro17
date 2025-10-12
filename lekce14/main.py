# Люди в тестировании
# Из тех с кем вы реально можете столкнуться это:
# 1. Другие разработчики (Они же dev- developer, SE - software engineer)
# 2. Автоматизированные тестировщики (Они же AQA - automation quality assurance, SDET - software development engineer in test)
# 3. Мануальные тестировщики
# В целом любых тестировщиков называют QA(quality assurance) или иногда QC(quality control)

# Dev → SDET → QA → PM (project manager)

# Упрощённая схема потока
# [ DEV пишет код ]
#        ↓
# 🔹 1. Unit tests (разработчик)
#        ↓
# 🔹 2. Integration tests (разработчик / SDET)
#        ↓
# 🔹 3. Acceptance tests (QA / заказчик)
#        ↓
# 🔹 4. Manual exploratory tests (QA)
#        ↓
# Release / Deployment


def mul(a, b):
    return a * b

def powNum(a, b):
    return a ** b

def roundNum(a):
    return round(a)


def get_weather():
    return "Дождь"



def add_task(tasks, task):
    tasks.append(task)
    return tasks

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
    return tasks

def complete_task(tasks, task):
    if task in tasks:
        index = tasks.index(task)
        tasks[index] = f"X {task}"
    return tasks

a = ["Купить хлеб", "Купить"]
print(complete_task(a, "Купить"))