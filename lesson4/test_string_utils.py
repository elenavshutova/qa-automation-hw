import pytest
from string_utils import StringUtils

# Создание экземпляра класса StringUtils
string_utils = StringUtils()

# Позитивные тесты для функции capitalize()
def test_capitalize_positive():
    assert string_utils.capitalize("skypro") == "Skypro"

# Позитивные тесты для функции trim()
def test_trim_positive():
    assert string_utils.trim("   skypro") == "skypro"

# Позитивные тесты для функции to_list()
def test_to_list_positive():
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]

# Позитивные тесты для функции contains()
def test_contains_positive():
    assert string_utils.contains("SkyPro", "S") == True

# Позитивные тесты для функции delete_symbol()
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"

# Негативные тесты для функции capitalize()
def test_capitalize_negative():
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize(None) == None

# Негативные тесты для функции trim()
def test_trim_negative():
    assert string_utils.trim("") == ""
    assert string_utils.trim(None) == None

# Негативные тесты для функции to_list()
def test_to_list_negative():
    assert string_utils.to_list("") == []
    assert string_utils.to_list(None) == []

# Негативные тесты для функции contains()
def test_contains_negative():
    assert string_utils.contains("SkyPro", "U") == False
    assert string_utils.contains("", "S") == False
    assert string_utils.contains("SkyPro", None) == False

# Негативные тесты для функции delete_symbol()
def test_delete_symbol_negative():
    assert string_utils.delete_symbol("SkyPro", "Pro") == "SkyPro"