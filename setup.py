from setuptools import setup, find_packages  # type: ignore

setup(
    # Nome do pacote
    name='edge_driver_selenium',
    
    # Versão do pacote
    version='0.1.0',
    
    # Descrição curta
    short_description='Um módulo para automatização usando Edge WebDriver',
    
    # Detecta automaticamente os pacotes
    packages=find_packages(where='.'),
    
    # Dependências necessárias
    install_requires=[
        'selenium>=4.0.0',      
        'Pillow>=8.0.0',        
        'opencv-python>=4.5.0', 
        'pandas>=1.0.0',         
        'numpy>=1.18.0',         
    ],
    
    # Versão mínima do Python
    python_requires='>=3.7',
    
    # Leitura do README para descrição longa
    description="Uma breve descrição do projeto",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    
    # Informações do autor
    author='Gustavo Nery',
    author_email='gustavorsnery@gmail.com',
    
    # URL do repositório
    url='https://github.com/GustavoRSNery/edge_driver_selenium',
    
    # Licença do pacote
    license='MIT',
    
    # Classificadores PyPI
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
