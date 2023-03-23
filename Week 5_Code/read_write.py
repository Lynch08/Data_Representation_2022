from pathlib import Path
file = Path(r'C:\Users\elyn\Documents\Data_Representation\Week5\Test.txt')
file.write_text(file.read_text().replace('skahdgjlshf', 'Enda'))