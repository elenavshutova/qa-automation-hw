import pytest
from string_utils import StringUtils

# позитивные  проверки
@pytest.mark.parametrize( 'input_string, result', [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),] )
def test_capitalize_positive(input_string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input_string)
    assert res == result

@pytest.mark.parametrize( 'input_string, result', [
    (" skypro", "skypro"),
    ("  skypro", "skypro"),
    ("   skypro", "skypro"),] )
def test_trim_positive(input_string, result):
    string_utils = StringUtils()
    res = string_utils.trim(input_string)
    assert res == result

@pytest.mark.parametrize( 'input_string, delimeter, result', [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    ("1", ",", ["1"])])
def test_to_list_positive(input_string, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(input_string, delimeter)
    assert res == result 

@pytest.mark.parametrize( 'input_string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),])
def test_contains_positive(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(input_string, symbol)
    assert res == result

@pytest.mark.parametrize( 'input_string, symbol, result', [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),])
def test_delete_symbol_positive(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input_string, symbol)
    assert res == result   

@pytest.mark.parametrize( 'input_string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),])
def test_starts_with_positive(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(input_string, symbol)
    assert res == result

@pytest.mark.parametrize( 'input_string, symbol, result', [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),])
def test_end_with_positive(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(input_string, symbol)
    assert res == result

@pytest.mark.parametrize( 'input_string, result', [
    ("", True), 
    (" ", True), 
    ("SkyPro", False),])
def test_is_empty_positive(input_string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(input_string)
    assert res == result

@pytest.mark.parametrize( 'input_string, joiner, result', [
    ([1,2,3,4], ", ", "1, 2, 3, 4"), 
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro")])
def test_list_to_string_positive(input_string, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input_string, joiner)
    assert res == result   

    # негативные проверки
@pytest.mark.parametrize( 'input_string, joiner, result', [
    ([], ",", ""),  
    (None, ",", ""), 
    ("string", ",", ""), 
    ([1, 2, 3], None, ""),])
def test_list_to_string_negative(input_string, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input_string, joiner)
    assert res == result

@pytest.mark.parametrize('input_string', [
    "",  
    " ",  
])
def test_capitalize_negative(input_string):
    string_utils = StringUtils()
    res = string_utils.capitilize(input_string)
    assert res == input_string


       