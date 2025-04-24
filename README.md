# AutomacaoSelenium

## Visão Geral

Esta biblioteca fornece uma interface para automação de tarefas no navegador Microsoft Edge utilizando Selenium. Inclui funcionalidades para interação com elementos da página, manipulação de iframes, extração de dados e reconhecimento de imagens para automação visual.

---

## Instalação

Antes de utilizar a biblioteca, instale as dependências necessárias:

```bash
git clone https://github.com/GustavoRSNery/edge_driver_selenium.git
cd edge_driver_selenium
pip install .
cd..
```

Certifique-se de que o Microsoft Edge WebDriver está instalado e configurado corretamente no sistema.

---

## Configuração do WebDriver

A classe `EdgeDriverConfig` configura e instancia um WebDriver do Edge.

### Exemplo de Uso:

```python
from config import EdgeDriverConfig

driver_config = EdgeDriverConfig(headless=False, inprivate=True, start_maximized=True, log_level=3)
driver = driver_config.create_driver()
```

### Parâmetros:

- `headless` (bool): Executa o navegador em modo headless (sem interface gráfica).
- `inprivate` (bool): Inicia o navegador no modo InPrivate.
- `start_maximized` (bool): Inicia o navegador maximizado.
- `log_level` (int): Define o nível de log do navegador.
- `window_size` (tuple): Define o tamanho da janela `(largura, altura)`, opcional.

---

## Classe `AutomacaoSelenium`

A classe `AutomacaoSelenium` encapsula métodos para facilitar a interação com o Selenium.

### Inicialização:

```python
from config import AutomacaoSelenium

automacao = AutomacaoSelenium(driver, wait=20)
```

- `driver`: Instância do WebDriver.
- `wait` (int): Tempo máximo de espera para carregamento de elementos.

---

## Métodos Disponíveis

### 1. `aguardar_elemento(xpath, t=None)`

Aguarda um elemento específico estar visível na página.

```python
elemento = automacao.aguardar_elemento("//div[@id='meuElemento']")
```

- `xpath` (str): Localização do elemento.
- `t` (int, opcional): Tempo máximo de espera.

---

### 2. `trocar_iframe(xpath)`

Troca o contexto para um iframe específico.

```python
automacao.trocar_iframe("//iframe[@id='meuIframe']")
```

---

### 3. `voltar_para_iframe_pai(niveis=1)`

Sai do iframe atual e retorna ao pai.

```python
automacao.voltar_para_iframe_pai(niveis=2)
```

- `niveis` (int): Número de níveis a retornar.

---

### 4. `aguardar_elemento_clicavel(xpath)`

Aguarda até que um elemento esteja pronto para ser clicado.

```python
elemento = automacao.aguardar_elemento_clicavel("//button[@id='meuBotao']")
```

---

### 5. `extrair_dados_div_para_tabela(div_principal_xpath)`

Extrai informações de uma div estruturada como tabela.

```python
df = automacao.extrair_dados_div_para_tabela("//div[@class='tabelaDados']")
```

- Retorna um `pandas.DataFrame` com os dados extraídos.

---

### 6. `find_image(screenshot, template_path)`

Encontra uma imagem específica dentro de uma captura de tela.

```python
location, size = automacao.find_image(screenshot, "caminho/template.png")
```

---

### 7. `clicar_icone(template_path)`

Captura a tela e clica automaticamente em um ícone específico.

```python
automacao.clicar_icone("caminho/icone.png")
```

---

## Exemplo de Uso
```python
from edge_driver import *

def test_edge_driver():
    try:
        # Inicializando o EdgeDriverConfig
        config = EdgeDriverConfig(headless=False, inprivate=True, window_size=(1920, 1080))
        print("Configuração inicializada com sucesso.")

        # Criando o driver
        driver = config.create_driver()
        print("Driver criado com sucesso.")

        # Usando AutomacaoSelenium
        AS = AutomacaoSelenium(driver, wait=60)
        print("Automação iniciada com sucesso.")

        # Realizar uma operação simples no navegador
        driver.get("https://www.google.com")
        print("Página carregada com sucesso!")

        # Fechar o navegador após o teste
        driver.quit()
        print("Navegador fechado com sucesso.")

    except DriverNotFoundException as e:
        print(f"Erro: {e.message}")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Executar o teste
if __name__ == "__main__":
    test_edge_driver()
