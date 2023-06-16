import pytest
from string_utils import StringUtils

# позитивные  проверки функции capitilize
@pytest.mark.parametrize( 'input_string, result', [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),] )
def test_capitalize_positive(input_string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input_string)
    assert res == result

    # негативные  проверки функции capitilize
    # Проверка пустой строки
@pytest.mark.parametrize('input_string', [
    "",
    " ",
])
def test_capitalize_empty_string(input_string):
    string_utils = StringUtils()
    with pytest.raises(ValueError):
        string_utils.capitilize(input_string)

# Проверка некорректного типа аргумента
@pytest.mark.parametrize('input_string', [
    None,
    123,
    ["skypro"],
])
def test_capitalize_invalid_type(input_string):
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(input_string)

# Проверка строки, которая уже начинается с заглавной буквы
@pytest.mark.parametrize('input_string', [
    "Skypro",
    "SKYPRO",
])
@pytest.mark.xfail(reason="Ожидаемо провалится", strict=True)
def test_capitalize_already_capitalized(input_string):
    string_utils = StringUtils()
    with pytest.raises(ValueError):
        string_utils.capitilize(input_string)

# Проверка строки, содержащей только специальные символы
@pytest.mark.xfail(reason="Ожидаемо провалится", strict=True)
def test_capitalize_special_characters():
    string_utils = StringUtils()
    input_string = "!skypro"
    with pytest.raises(ValueError):
        string_utils.capitilize(input_string)

# позитивные  проверки функции trim
@pytest.mark.parametrize( 'input_string, result', [
    (" skypro", "skypro"),
    ("  skypro", "skypro"),
    ("   skypro", "skypro"),] )
def test_trim_positive(input_string, result):
    string_utils = StringUtils()
    res = string_utils.trim(input_string)
    assert res == result

# негативные  проверки функции trim
# без букв
@pytest.mark.parametrize('input_string', [
    "",
    "     ",
])
def test_trim_negative(input_string):
    string_utils = StringUtils()
    assert string_utils.trim(input_string) == ""

# нет пробела для удаления
def test_trim_no_whitespace():
    string_utils = StringUtils()
    assert string_utils.trim("skypro") == "skypro"

# позитивные  проверки функции to_list
@pytest.mark.parametrize( 'input_string, delimeter, result', [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    ("1", ",", ["1"])])
def test_to_list_positive(input_string, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(input_string, delimeter)
    assert res == result 

# негативные  проверки функции to_list
# Проверка, когда delimeter не является строкой
def test_to_list_invalid_delimeter():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.to_list("a,b,c", 123)

# Проверка, когда string равна None
def test_to_list_none_string():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.to_list(None)

# Проверка, когда delimeter не является строкой
def test_to_list_invalid_delimeter():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.to_list("a,b,c", 123)

# позитивные  проверки функции contains
@pytest.mark.parametrize( 'input_string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),])
def test_contains_positive(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(input_string, symbol)
    assert res == result

# негативные проверки функции contains
# Проверка, когда string равна None
def test_contains_none_string():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.contains(None, "S")

# Проверка, когда symbol равен None
def test_contains_none_symbol():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.contains("SkyPro", None)

# Проверка, когда symbol не является строкой
def test_contains_invalid_symbol():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.contains("SkyPro", 123)

# Проверка, когда string пустая строка
def test_contains_empty_string():
    string_utils = StringUtils()
    res = string_utils.contains("", "S")
    assert res == False

# позитивные  проверки функции delete_symbol
@pytest.mark.parametrize( 'input_string, symbol, result', [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),])
def test_delete_symbol_positive(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input_string, symbol)
    assert res == result  

# негативные  проверки функции delete_symbol 
# символ не найден
def test_delete_symbol_symbol_not_found():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("SkyPro", "Z")
    assert res == "SkyPro"

# Проверка, когда symbol не является строкой
def test_delete_symbol_invalid_symbol():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.delete_symbol("SkyPro", 123)

# Проверка, когда symbol равен None
def test_delete_symbol_none_symbol():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.delete_symbol("SkyPro", None)

# Проверка, когда string равна None
def test_delete_symbol_none_string():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "k")

# позитивные проверки функции starts_with
@pytest.mark.parametrize( 'input_string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),])
def test_starts_with_positive(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(input_string, symbol)
    assert res == result

# негативные проверки функции starts_with
# Проверка, когда string равна None
def test_starts_with_none_string():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.starts_with(None, "S")

# Проверка, когда symbol равен None
def test_starts_with_none_symbol():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.starts_with("SkyPro", None)

# Проверка, когда symbol не является строкой
def test_starts_with_invalid_symbol():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.starts_with("SkyPro", 123)

# Пустая строка
def test_starts_with_empty_string():
    string_utils = StringUtils()
    res = string_utils.starts_with("", "S")
    assert res == False


# позитивные проверки функции end_with
@pytest.mark.parametrize( 'input_string, symbol, result', [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),])
def test_end_with_positive(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(input_string, symbol)
    assert res == result

# негативные проверки функции end_with
# Проверка, когда string равна None
def test_end_with_none_string():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.end_with(None, "S")

# Проверка, когда symbol равен None
def test_end_with_none_symbol():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.end_with("SkyPro", None)

# Проверка, когда symbol не является строкой
def test_end_with_invalid_symbol():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.end_with("SkyPro", 123)

# Пустая строка
def test_end_with_empty_string():
    string_utils = StringUtils()
    res = string_utils.starts_with("", "S")
    assert res == False


# позитивные проверки функции is_empty
@pytest.mark.parametrize( 'input_string, result', [
    ("", True), 
    (" ", True), 
    ("SkyPro", False),])
def test_is_empty_positive(input_string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(input_string)
    assert res == result

# негативные проверки функции is_empty
 # Передаем цифры вместо строки 
 # Передаем список вместо строки
@pytest.mark.parametrize("invalid_argument", [12345, ["a", "b", "c"]])
def test_is_empty_negative(invalid_argument):
    string_utils = StringUtils()

    with pytest.raises(AttributeError):
        string_utils.is_empty(invalid_argument)

    
# позитивные проверки функции list_to_string
@pytest.mark.parametrize( 'input_string, joiner, result', [
    ([1,2,3,4], ", ", "1, 2, 3, 4"), 
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro")])
def test_list_to_string_positive(input_string, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input_string, joiner)
    assert res == result   

# негативные проверки функции list_to_string  
@pytest.mark.parametrize("invalid_argument", [12345, None])
def test_list_to_string_negative(invalid_argument):
    string_utils = StringUtils()
    joiner = ", "

    with pytest.raises((TypeError)):
        string_utils.list_to_string(invalid_argument, joiner)