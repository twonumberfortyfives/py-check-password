import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "template, expected_result",
    [
        pytest.param(
            "Flfm@fk34sjkgu@4t45h5223466fg6h6",
            False
        ),
        pytest.param(
            "skdign24@",
            False
        ),
        pytest.param(
            "Dfjfjjfksiw@jd",
            False
        ),
        pytest.param(
            "sdF23FFFFF",
            False
        ),
        pytest.param(
            "fF@1",
            False
        )
    ]
)
def test_check_password(template: str, expected_result: bool) -> None:
    assert check_password(template) == expected_result
