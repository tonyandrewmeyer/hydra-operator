import pytest
from ops.testing import Harness

from charm import HydraCharm


@pytest.fixture()
def harness():
    harness = Harness(HydraCharm)
    harness.set_model_name("hydra-model")
    return harness


@pytest.fixture()
def mocked_kubernetes_service_patcher(mocker):
    mocked_service_patcher = mocker.patch("charm.KubernetesServicePatch")
    mocked_service_patcher.return_value = lambda x, y: None
    yield mocked_service_patcher


@pytest.fixture()
def mocked_update_container(mocker):
    mocked_update_container = mocker.patch("charm.HydraCharm._update_container")
    yield mocked_update_container


@pytest.fixture()
def mocked_fqdn(mocker):
    mocked_fqdn = mocker.patch("socket.getfqdn")
    mocked_fqdn.return_value = "hydra"
    return mocked_fqdn
