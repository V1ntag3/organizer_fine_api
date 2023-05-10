from rolepermissions.roles import AbstractUserRole

class UsuarioComum(AbstractUserRole):
    available_permissions={'criarEvento':True}