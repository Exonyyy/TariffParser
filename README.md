# Tariff Parser

## Описание

Проект автоматически парсит тарифные планы с сайта (https://www.rialcom.ru/internet_tariffs/) для категорий:

Многоквартирные дома
Частные дома и коттеджи

После парсинга данные нормализуются, объединяются и сохраняются в Excel-файл `tariffs.xlsx`.


## Установка

Проект использует **Python 3.10+** и менеджер зависимостей **[Poetry](https://python-poetry.org/)**.

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/your-username/tariff_parser.git
cd tariff_parser
```

> Для Windows: выполняйте команды в **Git Bash** или **PowerShell**.

---

### 2. Установка Poetry

#### Если Poetry ещё не установлен:

```bash
pip install poetry
```

Для Windows можно также:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Проверьте установку:

```bash
poetry --version
```

---

### 3. Установка зависимостей

```bash
poetry install
```

---

### 4. Установка ChromeDriver для Selenium

#### Selenium требует WebDriver:

1. Откройте Chrome и проверьте версию:  `chrome://settings/help`
2. Скачайте [ChromeDriver](https://sites.google.com/chromium.org/driver/) соответствующей версии
3. Распакуйте и:

   * для Windows: добавьте путь к `chromedriver.exe` в переменную среды `PATH`
   * для Linux/macOS: переместите в `/usr/local/bin`

---

## Запуск

```bash
poetry run python app/main.py
```

Результат: `tariffs.xlsx` в корне проекта.

---

## Настройки

Изменяются в `app/config.py`:

```python
url = "https://www.rialcom.ru/internet_tariffs/"
needed_section = [1, 2]  # Индексы секций на сайте
excel_name = "tariffs.xlsx"
```

---

## 📁 Структура проекта

```
tariff_parser/
├── .venv/                   # Виртуальное окружение Poetry
├── app/
│   ├── main.py              # Точка входа
│   ├── parser.py            # Парсинг через Selenium
│   ├── config.py            # Конфигурация
│   ├── utilities.py         # Excel обработка
├── poetry.lock
├── pyproject.toml
└── tariffs.xlsx             # Результат парсинга
```

---

## 📚 Основные зависимости

Перечислены в `pyproject.toml`. Основные:

| Библиотека | Назначение               | Команда ручной установки |
| ---------- | ------------------------ | ------------------------ |
| selenium   | Веб-парсинг              | `pip install selenium`   |
| pandas     | Работа с таблицами       | `pip install pandas`     |
| openpyxl   | Запись Excel файлов      | `pip install openpyxl`   |
| poetry     | Управление зависимостями | `pip install poetry`     |

> ❗️ Все библиотеки установятся автоматически через `poetry install`
