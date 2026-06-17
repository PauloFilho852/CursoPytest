from typing import Optional, Protocol, TypedDict


class Usuario(TypedDict):
    id: int
    nome: str


class RepositorioUsuario(Protocol):
    def buscar_por_id(self, usuario_id: int) -> Optional[Usuario]: ...


class UserService:
    def __init__(self, repositorio: RepositorioUsuario) -> None:
        self.repositorio = repositorio

    def obter_nome_usuario(self, usuario_id: int) -> Optional[str]:
        usuario = self.repositorio.buscar_por_id(usuario_id)

        if not usuario:
            return None

        return usuario["nome"]
