from reverse import reverse


def test_reverse_string():
    output = reverse("race car")
    assert output == "rac ecar"
