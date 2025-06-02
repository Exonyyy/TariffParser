import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Parser:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def parse(self, needed_sections):
        """Разбиение веб-страницы по секциям и парсинг данных"""
        self.driver.get(self.url)
        sections_place = self.driver.find_element(By.CLASS_NAME, "accordion")
        sections = sections_place.find_elements(By.CLASS_NAME, "card")

        sections = [sections[i-1] for i in needed_sections]
        parsed_table_data = list()

        for section in sections:
            section.find_element(By.TAG_NAME, "button").click()
            # tables = self.wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, "table")))
            tables = section.find_elements(By.TAG_NAME, "table")
            for table in tables:
                time.sleep(1)
                parsed_table = self.parse_table(table)
                parsed_table_data.append(parsed_table)

        return parsed_table_data

    def parse_table(self, parse_data):
        """Парсинг и группировка таблиц данных"""
        data = list()
        head = [cell.text for cell in parse_data.find_elements(By.TAG_NAME, "th")]
        data.append(head)
        rows = parse_data.find_elements(By.TAG_NAME, "tr")[1:]
        for row in rows:
            self.driver.implicitly_wait(5)
            cells = row.find_elements(By.TAG_NAME, "td")
            data.append([cell.text for cell in cells])
        return data
