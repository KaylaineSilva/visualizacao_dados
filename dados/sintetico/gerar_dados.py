import csv
import random
import calendar
from pathlib import Path

random.seed(252)

areas = ['Computação', 'Matemática', 'Estatística', 'Cultura']
tipos = ['Evento', 'Palestra']
base = {'Computação': 7, 'Matemática': 5, 'Estatística': 4, 'Cultura': 3}

rows = []
idx = 1
for ano in range(2022, 2027):
    for mes in range(1, 13):
        if ano == 2026 and mes > 10:
            continue
        for area in areas:
            n = max(0, base[area] + (3 if mes in [4, 5, 9, 10] else -2 if mes in [1, 7, 12] else 0) + (ano - 2022) // 2 + random.randint(-3, 2))
            for _ in range(n):
                dia = random.randint(1, calendar.monthrange(ano, mes)[1])
                tipo = random.choice(tipos)
                rows.append([
                    f'EV{idx:05d}',
                    f'{tipo} de {area} {idx}',
                    f'{ano}-{mes:02d}-{dia:02d}',
                    area,
                    tipo,
                ])
                idx += 1

out = Path(__file__).parent / 'eventos_exemplo.csv'
with out.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'titulo', 'data', 'area', 'tipo'])
    writer.writerows(rows)

print(f'{len(rows)} eventos sintéticos gerados em {out}')
