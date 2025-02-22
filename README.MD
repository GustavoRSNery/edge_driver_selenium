
# Exemplo de uso...........................

    from edge_driver import EdgeDriverConfig, AutomacaoSelenium, DriverNotFoundException # type: ignore

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
