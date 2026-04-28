from animal_shelter import data


def test_convert_camel_case():
    assert data.convert_camel_case("CamelCase") == "camel_case"
    assert data.convert_camel_case("CamelCASE") == "camel_case"
    assert data.convert_camel_case("camel-case") != "camel_case"

    assert data.convert_camel_case("snake_case") == "snake_case"

    assert data.convert_camel_case("HelloWorld") == "hello_world"
    assert data.convert_camel_case("Hello   World") == "hello_world"
    assert data.convert_camel_case("Hello\tWorld") == "hello_world"
    assert data.convert_camel_case("helloWorld TestCase") == "hello_world_test_case"
