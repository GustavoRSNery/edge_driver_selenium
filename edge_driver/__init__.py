# Importações principais
from .config import EdgeDriverConfig, AutomacaoSelenium
from .exceptions import (
    EdgeDriverException,
    DriverNotFoundException,
    ElementNotFoundException,
    TimeoutException,
)

# Expõe as classes e exceções principais do pacote
__all__ = [
    'EdgeDriverConfig', 
    'AutomacaoSelenium', 
    'EdgeDriverException', 
    'DriverNotFoundException', 
    'ElementNotFoundException', 
    'TimeoutException',
]
