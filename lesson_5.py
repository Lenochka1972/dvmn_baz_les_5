import file_operations
import random
import os
from faker import Faker


def main():

    if not os.path.exists('cards_lesson5'):
        os.makedirs('cards_lesson5')

    fake = Faker('ru_RU')

    skills = [
        'Стремительный прыжок',
        'Электрический выстрел',
        'Ледяной удар',
        'Стремительный удар',
        'Тайный побег',
        'Ледяной выстрел',
        'Огненный заряд'
    ]

    letters_mapping = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        ' ': ' '
    }

    for number in range(10):
        skills_card = random.sample(skills, 5)  # список из 5-ти навыков
        runic_skills = []  # список навыков рунческими буквами

        for skill in skills_card:
            runic_skill = ''  # строка для записи навыка руническими буквами
            for letter in skill:
                runic_letter = letters_mapping[letter]
                runic_skill += runic_letter
            runic_skills.append(runic_skill)

        context = {
            'first_name': fake.first_name_male(),
            'last_name': fake.last_name_male(),
            'job': fake.job(),
            'town': fake.city(),
            'strength': random.randint(2, 19),
            'agility': random.randint(2, 19),
            'endurance': random.randint(2, 19),
            'intelligence': random.randint(2, 19),
            'luck': random.randint(2, 19),
            'skill_1': runic_skills[0],
            'skill_2': runic_skills[1],
            'skill_3': runic_skills[2],
            'skill_4': runic_skills[3],
            'skill_5': runic_skills[4],
        }

        file_operations.render_template('charsheet.svg',
                                        'cards_lesson5/hero_card_{a}.svg'.
                                        format(a=number+1),
                                        context)


if __name__ == '__main__':

    main()
