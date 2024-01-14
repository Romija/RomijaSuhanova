studenti = {
    123: {'vards': 'Roberts','age': 12,'atzime': 4},
    456: {'vards': 'Alberts','age': 34,'atzime': 8},
    789: {'vards': 'Margarita','age': 5,'atzime': 2}
}

def get_age(student_data):
    return student_data[1]['age']

#veikt vārdnīcas sakārtošanu, izmantojot definēto funkciju, rezultātu saglabāt mainīgajā

sorted_students_by_age = dict(sorted(studenti.items(), key=get_age))
print('Sakārtota vārdnīca pēc vecuma: ')
for id, dati in sorted_students_by_age.items():
    print(f'ID:{id},Dati: {dati}')
