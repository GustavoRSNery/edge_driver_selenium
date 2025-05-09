# Selenium - automação do navegador
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver

# Manipulação de arquivos e imagens
from io import BytesIO
from PIL import Image, ImageTk, ImageSequence
import pyautogui
import cv2

# Manipulação de dados
import pandas as pd
import numpy as np

# Utilitários do sistema
import sys
from time import sleep, time

class EdgeDriverConfig:
    def __init__(self, headless=False, inprivate=False, start_maximized=True, log_level=3, window_size=None):
        # Configuração das opções do Edge
        self.options = Options()
        
        # Adiciona argumentos conforme solicitado
        if headless:
            self.options.add_argument("--headless")  # Executa o navegador em modo headless
        if inprivate:
            self.options.add_argument("--inprivate")  # Abre o navegador no modo InPrivate
        if start_maximized:
            self.options.add_argument("--start-maximized")  # Inicia o navegador maximizado
        self.options.add_argument(f"--log-level={log_level}")  # Define o nível de log
        
        # Configura o tamanho da janela, se especificado
        if window_size:
            self.options.add_argument(f"--window-size={window_size[0]},{window_size[1]}")

    def create_driver(self):
        # Inicializa o WebDriver com as opções configuradas
        service = Service()  # Adapte conforme necessário para o caminho do executável
        return webdriver.Edge(service=service, options=self.options)

class AutomacaoSelenium:
    def __init__(self, driver, wait = 20):
        self.driver = driver
        self.wait = wait

    def aguardar_elemento(self, xpath, t=None):
        """Aguarda até que o elemento especificado pelo xpath esteja presente no DOM e visível.

        Args:
            xpath (str): O XPath do elemento a ser localizado.
            t (int, optional): Tempo máximo de espera em segundos. Se None, usa self.wait.

        Returns:
            WebElement: O elemento encontrado, ou None se não for encontrado dentro do tempo especificado.
        """
        t = t if t is not None else self.wait
        try:
            elemento = WebDriverWait(self.driver, t).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return elemento

        except Exception as e:
            # Ignora erros específicos relacionados ao botão não encontrado
            # Condição apenas para não retornar mensagem de erro apos não encontrar o elemento de login invalido na pagina
            if 'EXAMPLE' == xpath:
                return None
            
            if "Message" in str(e):
                print('Não encontrei o elemento indicado')
                return None
            else:
                print(f'Ocorreu um erro inexperado: {e}')
                raise

    def trocar_iframe(self, xpath):
        """Troca para o iframe especificado usando seu XPath."""
        try:
            WebDriverWait(self.driver, self.wait).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, xpath))
            )
            print("Mudança para o iframe foi bem-sucedida.")
        except Exception as e:
            print(f"Erro ao trocar para o iframe: {e}")

    def voltar_para_iframe_pai(self, niveis=1):
        """Volta um número específico de níveis na hierarquia de iframes."""
        for i, _ in enumerate(range(niveis)):
            try:
                self.driver.switch_to.parent_frame()
                print(f'Voltando o {i+1}° iframe...')
            except Exception as e:
                print(f"Erro ao voltar para o iframe pai: {e}")
                break
        """# Exemplo de uso para voltar 1 nível
            AS.voltar_para_iframe_pai(niveis=1)

            # Exemplo de uso para voltar 2 níveis
            AS.voltar_para_iframe_pai(niveis=2)

            Se você precisar sair completamente de todos os 
            iframes e voltar ao contexto principal da página, 
            basta chamar "driver.switch_to.default_content()" diretamente.
        """

    def aguardar_elemento_clicavel(self, xpath):
        """Espera que um elemento esteja clicável na página."""
        try:
            elemento = WebDriverWait(self.driver, self.wait).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            return elemento
        except Exception as e:
            # Ignora erros específicos relacionados ao botão não encontrado
            if "Message" in str(e):
                print('Não encontrei o elemento indicado')
                return None
            else:
                print(f'ERRO: Ocorreu um erro inexperado: {e}')
                raise

    def extrair_dados_div_para_tabela(self, div_principal_xpath):
        """Extrai dados de uma div que representa uma tabela HTML e retorna uma lista de listas."""
        try:
            # Localiza a div principal
            div_principal = self.aguardar_elemento(div_principal_xpath)
            if not div_principal:
                print("Div principal não encontrada.")
                return None

            # Localiza todas as divs (colunas) dentro da div principal
            colunas = div_principal.find_elements(By.XPATH, './/div')
            tabela = []

            # Itera sobre cada div (coluna) para extrair os dados dos spans
            for coluna in colunas:
                # Localiza todos os spans (linhas) dentro de cada div
                linhas = coluna.find_elements(By.XPATH, './/span')
                coluna_dados = [linha.text for linha in linhas] # Adiciona texto de spans não vazios
                if coluna_dados:  # Adiciona a coluna se houver dados
                    tabela.append(coluna_dados)

            # Verifica se a tabela tem dados
            if not tabela:
                print("Nenhum dado encontrado nas colunas.")
                return None

            # Transforma os dados em uma tabela, alinhando as colunas como linhas
            tabela_transposta = list(zip(*tabela))  # Transposta para alinhar as colunas como linhas
            
            # Converte a tabela transposta para um DataFrame do pandas
            df = pd.DataFrame(tabela_transposta)

            return df

        except Exception as e:
            print(f"ERRO: ao extrair dados da div para tabela: {e}")
            return None

    # Abaixo funções sobre imagens. vvv
    def find_image(screenshot, template_path):
        """Encontra a imagem do template no screenshot usando OpenCV."""
        template = cv2.imread(template_path)
        if template is None:
            raise ValueError(f"Não foi possível ler a imagem do template: {template_path}")

        print(f"Tipo de template: {type(template)}, Forma: {template.shape}")

        w, h = template.shape[1], template.shape[0]

        # Converter imagens para escala de cinza
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY) if len(screenshot.shape) == 3 else screenshot
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY) if len(template.shape) == 3 else template

        result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        return max_loc, (w, h), max_val

def find_image(screenshot, template_path):
    """Encontra a imagem do template no screenshot usando OpenCV."""
    template = cv2.imread(template_path)
    if template is None:
        raise ValueError(f"Não foi possível ler a imagem do template: {template_path}")

    print(f"Tipo de template: {type(template)}, Forma: {template.shape}")

    w, h = template.shape[1], template.shape[0]

    # Converter imagens para escala de cinza
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY) if len(screenshot.shape) == 3 else screenshot
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY) if len(template.shape) == 3 else template

    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    return max_loc, (w, h), max_val

def clicar_icone(template_path, confianca_min=0.8):
    """Captura a tela, procura o ícone e clica nele."""
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    max_loc, (w, h), confidence = find_image(screenshot, template_path)

    print(f"[DEBUG] Confiança: {confidence:.2f}")
    if confidence >= confianca_min:
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        pyautogui.moveTo(center_x, center_y, duration=0.2)
        pyautogui.click()
        print(f"[INFO] Clique realizado em: ({center_x}, {center_y})")
        return True
    else:
        print("[WARN] Confiança insuficiente.")
        return False

