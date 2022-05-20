import json
from pprint import pprint as pp
PATH = 'candidates.json'


def load_data(path=PATH):
    """Получает данные из json"""
    with open(path, encoding="utf-8") as f:
        candidates_data = json.load(f)
    return candidates_data


def load_candidates_from_json():
    data = load_data()
    return data

def get_candidate(pk):
    """Получает кандидата по его id"""
    candidates = load_data()
    for candidate in candidates:
        if candidate["id"] == pk:
            return candidate


def get_candidates_by_skill(skill_name):
    """Получает список кандидатов с одинаковыми скиллами"""
    candidate_skill = []
    candidates = load_data()
    for candidate in candidates:
        skills = candidate["skills"].lower().split(", ")
        if skill_name.lower() in skills:
            candidate_skill.append(candidate)
            continue
    return candidate_skill


def get_candidates_by_name(candidate_name):
    """Создает список по именам"""
    candidate_names = []
    candidates = load_data()
    for candidate in candidates:
        names = candidate["name"].lower().split(" ")
        if candidate_name.lower() in names:
            candidate_names.append(candidate)

    return candidate_names




#pp(get_candidates_by_name('sheri')) # Проверка функций