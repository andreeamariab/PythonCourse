import json


# Funcție pentru citirea categoriilor din fișier
def read_categories():
    try:
        with open("categories.json", "r") as file:
            categories = json.load(file)
    except FileNotFoundError:
        categories = []
    return categories


# Funcție pentru salvarea categoriilor în fișier
def save_categories(categories):
    with open("categories.json", "w") as file:
        json.dump(categories, file)


# Funcție pentru adăugarea unei categorii
def add_category(category):
    categories = read_categories()
    if category not in categories:
        categories.append(category)
        save_categories(categories)
        print(f"Categoria '{category}' a fost adăugată cu succes.")
    else:
        print(f"Categoria '{category}' există deja.")


# Funcție pentru citirea task-urilor din fișier
def read_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


# Funcție pentru salvarea task-urilor în fișier
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


# Funcție pentru adăugarea unui task
def add_task():
    tasks = read_tasks()

    task = input("Introduceți un task: ")
    deadline = input("Introduceți data limită (format: DD.MM.YYYY HH:MM): ")
    responsible = input("Introduceți persoana responsabilă: ")
    category = input("Introduceți categoria: ")

    categories = read_categories()
    if category in categories:
        if any(t['task'] == task for t in tasks):
            print(f"Task-ul '{task}' există deja.")
        else:
            tasks.append({
                'task': task,
                'deadline': deadline,
                'responsible': responsible,
                'category': category
            })
            save_tasks(tasks)
            print("Task-ul a fost adăugat cu succes.")
    else:
        print(f"Categoria '{category}' nu există.")


# Funcție pentru listarea task-urilor în funcție de categorie
def list_tasks():
    tasks = read_tasks()
    tasks.sort(key=lambda t: t['category'])  # Sortare după categorie

    for task in tasks:
        print(f"Task: {task['task']}")
        print(f"Data limită: {task['deadline']}")
        print(f"Persoană responsabilă: {task['responsible']}")
        print(f"Categorie: {task['category']}")
        print("------------------------")


# Funcție pentru sortare
def sort_tasks(option):
    tasks = read_tasks()

    if option == 1:
        tasks.sort(key=lambda t: t['task'])  # Sortare ascendentă după task
    elif option == 2:
        tasks.sort(key=lambda t: t['task'], reverse=True)  # Sortare descendentă după task
    elif option == 3:
        tasks.sort(key=lambda t: t['deadline'])  # Sortare ascendentă după data
    elif option == 4:
        tasks.sort(key=lambda t: t['deadline'], reverse=True)  # Sortare descendentă după data
    elif option == 5:
        tasks.sort(key=lambda t: t['responsible'])  # Sortare ascendentă după persoană responsabilă
    elif option == 6:
        tasks.sort(key=lambda t: t['responsible'], reverse=True)  # Sortare descendentă după persoană responsabilă
    elif option == 7:
        tasks.sort(key=lambda t: t['category'])  # Sortare ascendentă după categorie
    elif option == 8:
        tasks.sort(key=lambda t: t['category'], reverse=True)  # Sortare descendentă după categorie

    save_tasks(tasks)
    print("Lista a fost sortată cu succes.")


# Funcție pentru filtrare
def filter_tasks():
    tasks = read_tasks()

    field = input("Introduceți câmpul de filtrare (1. Task, 2. Dată, 3. Persoană responsabilă, 4. Categorie): ")
    keyword = input("Introduceți cuvântul cheie pentru filtrare: ")

    if field == "1":
        filtered_tasks = [t for t in tasks if keyword in t['task']]
    elif field == "2":
        filtered_tasks = [t for t in tasks if keyword in t['deadline']]
    elif field == "3":
        filtered_tasks = [t for t in tasks if keyword in t['responsible']]
    elif field == "4":
        filtered_tasks = [t for t in tasks if keyword in t['category']]
    else:
        print("Opțiune invalidă.")
        return

    for task in filtered_tasks:
        print(f"Task: {task['task']}")
        print(f"Data limită: {task['deadline']}")
        print(f"Persoană responsabilă: {task['responsible']}")
        print(f"Categorie: {task['category']}")
        print("------------------------")


# Funcție pentru editare
def edit_task():
    tasks = read_tasks()

    task_id = input("Introduceți ID-ul task-ului pe care doriți să îl editați: ")
    task_id = int(task_id)

    if task_id < 0 or task_id >= len(tasks):
        print("ID-ul task-ului este invalid.")
        return

    field = input(
        "Introduceți câmpul pe care doriți să îl editați (1. Task, 2. Dată, 3. Persoană responsabilă, 4. Categorie): ")
    new_value = input("Introduceți noua valoare: ")

    if field == "1":
        tasks[task_id]['task'] = new_value
    elif field == "2":
        tasks[task_id]['deadline'] = new_value
    elif field == "3":
        tasks[task_id]['responsible'] = new_value
    elif field == "4":
        tasks[task_id]['category'] = new_value
    else:
        print("Opțiune invalidă.")
        return

    save_tasks(tasks)
    print("Task-ul a fost editat cu succes.")


# Funcție pentru ștergere
def delete_task():
    tasks = read_tasks()

    task_id = input("Introduceți ID-ul task-ului pe care doriți să îl ștergeți: ")
    task_id = int(task_id)

    if task_id < 0 or task_id >= len(tasks):
        print("ID-ul task-ului este invalid.")
        return

    del tasks[task_id]
    save_tasks(tasks)
    print("Task-ul a fost șters cu succes.")


# Meniu principal
def main_menu():
    while True:
        print("\n-- Meniu Principal --")
        print("1. Adăugare categorie")
        print("2. Adăugare task")
        print("3. Listare task-uri")
        print("4. Sortare task-uri")
        print("5. Filtrare task-uri")
        print("6. Editare task")
        print("7. Ștergere task")
        print("0. Ieșire")

        option = input("Alegeți o opțiune: ")

        if option == "1":
            category = input("Introduceți categoria: ")
            add_category(category)
        elif option == "2":
            add_task()
        elif option == "3":
            list_tasks()
        elif option == "4":
            sort_option = input("Introduceți opțiunea de sortare: ")
            sort_option = int(sort_option)
            sort_tasks(sort_option)
        elif option == "5":
            filter_tasks()
        elif option == "6":
            edit_task()
        elif option == "7":
            delete_task()
        elif option == "0":
            break
        else:
            print("Opțiune invalidă.")


# Apelarea meniului principal
main_menu()
