import pytest
from unittest.mock import MagicMock

from user_service import UserService


def buscar_por_id_side_effect(usuario_id: int) -> dict | None:
    if usuario_id == 1:
        return {"id": 1, "nome": "Paulo"}
    elif usuario_id == 2:
        return {"id": 2, "nome": "Maria"}
    elif usuario_id == 3:
        return {"id": 3, "nome": None}
    else:
        return {"id": 4, "nome": ""}


@pytest.fixture
def user_service() -> UserService:
    repositorio_mock = MagicMock()
    repositorio_mock.buscar_por_id.side_effect = buscar_por_id_side_effect
    return UserService(repositorio_mock)


def test_obter_nome_usuario_id_1(user_service: UserService):
    nome_usuario = user_service.obter_nome_usuario(1)

    assert nome_usuario == "Paulo"
    user_service.repositorio.buscar_por_id.assert_called_once_with(1)


def test_obter_nome_usuario_id_2(user_service: UserService):
    nome_usuario = user_service.obter_nome_usuario(2)

    assert nome_usuario == "Maria"
    user_service.repositorio.buscar_por_id.assert_called_once_with(2)


def test_obter_nome_usuario_id_3(user_service: UserService):
    nome_usuario = user_service.obter_nome_usuario(3)

    assert nome_usuario is None
    user_service.repositorio.buscar_por_id.assert_called_once_with(3)


def test_obter_nome_usuario_excecao(user_service: UserService):
    user_service.repositorio.buscar_por_id.side_effect = Exception(
        "Erro ao buscar usuário"
    )

    with pytest.raises(Exception) as exc_info:
        user_service.obter_nome_usuario(1)

    assert str(exc_info.value) == "Erro ao buscar usuário"
    user_service.repositorio.buscar_por_id.assert_called_once_with(1)


def test_obter_nome_usuario_usuario_nao_encontrado(user_service: UserService):
    nome_usuario = user_service.obter_nome_usuario(3)

    assert nome_usuario is None
    user_service.repositorio.buscar_por_id.assert_called_once_with(3)


def test_obter_nome_usuario_usuario_com_nome_vazio(user_service: UserService):
    nome_usuario = user_service.obter_nome_usuario(4)

    assert nome_usuario == ""
    user_service.repositorio.buscar_por_id.assert_called_once_with(4)
