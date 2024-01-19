get_budgets = {
    'odam1': {"ism": "John", "budjet": 23000},
    'odam2': {"ism": "Jane", "budjet": 40000},
    'odam3': {"ism": "Bob", "budjet": 2700}
}

def calculate_budget(budget):
    result = 0
    for x in budget.values():
        result += x.get("budjet")

    print(result)

calculate_budget(budget=get_budgets)





