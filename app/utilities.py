import re
import pandas as pd


class ConvertTable:
    """Класс для трансформации таблицы"""
    def __init__(self, data):
        self.data = data

    def convert_all(self):
        """Изменения всех вложенных таблиц"""
        self.data[3][0] = self.data[1][0]
        for i, table in enumerate(self.data):
            if i % 2 == 1:
                self.data[i] = self.transform_with_tv(table)
            else:
                self.data[i] = self.transform_internet(table)

        self.data[3] = self.fill_channels_from(self.data[1], self.data[3])
        return self.data

    def transform_internet(self, data):
        """Трансформация интернет-тарифов"""
        rows = data[1:]
        result = []
        for row in rows:
            name = row[0]
            price_match = re.search(r'\d+', row[1])
            speed_match = re.search(r'\d+', row[3])
            if price_match and speed_match:
                price = int(price_match.group())
                speed = int(speed_match.group()) // 1000
                result.append([name, None, speed, price])
        return result

    def transform_with_tv(self, data):
        """Трансформация тарифов интернет+тв"""
        headers = data[0][1:]
        speeds = [self.extract_speed(h) for h in headers]
        result = []

        for row in data[1:]:
            base_name, channels = self.extract_channels(row[0])
            for i, price in enumerate(row[1:]):
                full_name = f"{base_name} + {headers[i]}"
                result.append([full_name, channels, speeds[i], int(price)])
        return result

    def extract_channels(self, name):
        """Получение количество каналов"""
        match = re.search(r"(.*?)\s*\((\d+)\s+кан", name)
        if match:
            return match.group(1).strip(), int(match.group(2))
        return name.strip(), None

    def extract_speed(self, header):
        """Получение скорости"""
        match = re.search(r"(\d+)", header)
        if match:
            return int(match.group(1))
        return None

    def normalize_name(self, name):
        """Привидение имени канала"""
        return re.sub(r"[^а-яa-z0-9+]+", " ", name.lower()).strip()

    def fill_channels_from(self, source, target):
        """Заполнение количества каналов на основе данных другой таблицы"""
        channel_map = {}
        for row in source:
            if row[1] is not None:
                key = self.normalize_name(row[0])
                channel_map[key] = row[1]

        for row in target:
            norm_name = self.normalize_name(row[0])
            if norm_name in channel_map:
                row[1] = channel_map[norm_name]

        return target


class ExcelWriter:
    def __init__(self, tables):
        self.tables = tables

    def flatten(self):
        """Расслоение таблиц"""
        flat_data = []
        for table in self.tables:
            flat_data.extend(table)
        return flat_data

    def save_to_excel(self, filename):
        """Сохранение в Excel_file"""
        data = self.flatten()
        df = pd.DataFrame(data, columns=[
            "Название тарифа",
            "Количество каналов",
            "Скорость доступа",
            "Абонентская плата"
        ])
        df.to_excel(filename, index=False)
