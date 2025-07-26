from smartphone import Smartphone
catalog = [
    Smartphone ('HONOR', 'X8b','+79261980396'),
    Smartphone ('TECNO', 'Camon 30','+79261980395'),
    Smartphone ('Samsung', 'Galaxy A15','+79271980396'),
    Smartphone ('Xiaomi', 'POCO M6','+79261970396'),
    Smartphone ('Realme', 'note 50','+79261980396')
]
for smartphone in catalog:
        print(f"{smartphone.marka} - {smartphone.model} - {smartphone.numer}")