import pytest

from apps.categories.factories import CategoryFactory


@pytest.mark.django_db
def test_category_str(capsys):
    category1 = CategoryFactory()
    print(category1)
    captured = capsys.readouterr()
    assert captured.out == category1.name + "\n"
