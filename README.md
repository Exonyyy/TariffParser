
# Tariff Parser

## Описание

Проект автоматически парсит тарифные планы с сайта [rialcom.ru](https://www.rialcom.ru/internet_tariffs/) для категорий:
- Многоквартирные дома
- Частные дома и коттеджи

После парсинга данные нормализуются, объединяются и сохраняются в Excel-файл `tariffs.xlsx`.

---

## Установка

Проект использует Python 3.10+ и менеджер зависимостей [Poetry](https://python-poetry.org/).

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/your-username/tariff_parser.git
cd tariff_parser
```

### 2. Установите Poetry (если не установлен)

```bash
pip install poetry
```

### 3. Установите зависимости

```bash
poetry install
```

---

## Запуск

Для запуска используйте:

```bash
poetry run python app/main.py
```

Файл `tariffs.xlsx` будет создан в корне проекта.

---

## Настройки

Все настройки проекта находятся в `app/config.py`:

```python
url = "https://www.rialcom.ru/internet_tariffs/"
needed_section = [1, 2]  # индексы секций на сайте
excel_name = "tariffs.xlsx"
```

---

## Структура проекта

```
tariff_parser/
├── .venv/
├── app/
│   ├── main.py            # Точка входа
│   ├── parser.py          # Парсинг через Selenium
│   ├── config.py          # Конфигурация
│   ├── utilities.py       # Преобразование + Excel запись
├── poetry.lock
├── pyproject.toml
└── tariffs.xlsx           # Результат
```

---

## Зависимости

Указаны в `pyproject.toml`. Основные:

- `selenium`
- `pandas`
- `openpyxl` (для записи Excel)
- `poetry`

