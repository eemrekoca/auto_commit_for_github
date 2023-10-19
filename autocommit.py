import os
from datetime import datetime
from git import Repo

# Değişkenler
REPO_PATH = '/path/to/your/repo'


FILE_PATH = os.path.join(REPO_PATH, 'date.txt')
COMMIT_MESSAGE = f"Otomatik tarih ekleme: {datetime.now()}"

# Dosyaya tarih bilgisi eklenir
with open(FILE_PATH, 'a') as file:
    file.write(f"{datetime.now()}\n")

# Commit ve push işlemleri
repo = Repo(REPO_PATH)
repo.git.add(FILE_PATH)
repo.git.commit('-m', COMMIT_MESSAGE)
repo.git.push('origin', 'main')  

print("Commit başarılı!")
