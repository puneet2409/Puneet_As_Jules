import pytest


@pytest.fixture(scope="session")
def supp_l(request):
    return request.param

