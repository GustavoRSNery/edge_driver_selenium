class EdgeDriverException(Exception):
    """Exceção base para erros relacionados ao EdgeDriver."""
    def __init__(self, message="Erro desconhecido no EdgeDriver"):
        self.message = message
        super().__init__(self.message)

class DriverNotFoundException(EdgeDriverException):
    """Exceção quando o driver não for encontrado."""
    def __init__(self, message="Driver do Edge não encontrado. Verifique o caminho ou a instalação"):
        self.message = message
        super().__init__(self.message)

class ElementNotFoundException(EdgeDriverException):
    """Exceção quando um elemento não for encontrado na página."""
    def __init__(self, message="Elemento não encontrado no DOM"):
        self.message = message
        super().__init__(self.message)

class TimeoutException(EdgeDriverException):
    """Exceção quando uma operação excede o tempo limite."""
    def __init__(self, message="Tempo de espera excedido"):
        self.message = message
        super().__init__(self.message)
