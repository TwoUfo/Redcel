from environ import Env  # type: ignore[import-untyped]

from .base import BASE_DIR

Env.read_env(BASE_DIR.joinpath(".env"))
env = Env()
