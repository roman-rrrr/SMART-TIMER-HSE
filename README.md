# SMART-TIMER-HSE
Лёгкий веб‑таймер в стиле «Помодоро» с автоматическим открытием браузера и звуком без сторонних аудио‑библиотек.
## Требования
- Python 3.8+ (Windows/macOS/Linux)
- pip
- Зависимости:
  - Flask
  - playsound(1.2.2)
- PyInstaller(опционально, для сборки в один файл)
## Установка
```bash
# создать и активировать виртуальное окружение
# Windows: .venv\Scripts\activate
# Unix/Mac: source .venv/bin/activate
python -m venv .venv
pip install Flask
pip install playsound==1.2.2
# для сборки (опционально):
pip install pyinstaller
```
## Запуск
```bash
python app.py
```
Приложение поднимется на http://127.0.0.1:5000 и вкладка открывается автоматически.
## Использование
- Откройте http://127.0.0.1:5000
- Укажите время окончания (HH:MM), длительности короткого/длинного перерывов, запустите таймер
- При необходимости остановите таймер из интерфейса

## Сборка в исполняемый файл(PyInstaller)
Windows (в --add-data используйте точку с запятой):
```bash
pyinstaller --onefile ^
  --add-data "templates;templates" ^
  --add-data "static;static" ^
  --add-data "back_to_work.mp3;." ^
  --add-data "short.mp3;." ^
  --add-data "long.mp3;." ^
  --add-data "time_end.mp3;." app.py
```
macOS/Linux (в --add-data используйте двоеточие):
```bash
pyinstaller --onefile \
  --add-data "templates:templates" \
  --add-data "static:static" \
  --add-data "back_to_work.mp3:." \
  --add-data "short.mp3:." \
  --add-data "long.mp3:." \
  --add-data "time_end.mp3:." app.py
```
## Возможные проблемы
- Порт занят: измените порт в app.run(..., port=5001).
- Нет звука: убедитесь, что в системе есть ассоциация для MP3 (xdg-open/open/os.startfile).
- В собранной версии нет ресурсов: пересоберите с указанными --add-data.
- Открывается две вкладки: запускайте с use_reloader=False.
