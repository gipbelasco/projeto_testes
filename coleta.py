import time
import traceback
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from models import Unidade, Curso, Disciplina


def iniciar_driver():
    options = Options()
    options.add_argument('--headless')  # ❌ Comente esta linha se quiser ver o navegador
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get("https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275")
    return driver


def extrair_dados_curso(driver, unidade_nome, curso_nome):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="Grade Curricular"]'))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@summary='Grade Curricular']"))
        )

        soup = BeautifulSoup(driver.page_source, 'lxml')
        tabela = soup.find('table', {'summary': 'Grade Curricular'})
        if not tabela:
            return None

        linhas = tabela.find_all('tr')[1:]
        obrigatorias, eletivas, livres = [], [], []

        for linha in linhas:
            colunas = linha.find_all('td')
            if len(colunas) < 8:
                continue

            disciplina = Disciplina(
                codigo=colunas[0].text.strip(),
                nome=colunas[1].text.strip(),
                creditos_aula=colunas[2].text.strip(),
                creditos_trabalho=colunas[3].text.strip(),
                carga_horaria=colunas[4].text.strip(),
                estagio=colunas[5].text.strip(),
                pcc=colunas[6].text.strip(),
                tpa=colunas[7].text.strip()
            )

            categoria = colunas[-1].text.lower()
            if "obrigatória" in categoria:
                obrigatorias.append(disciplina)
            elif "eletiva" in categoria:
                eletivas.append(disciplina)
            elif "livre" in categoria:
                livres.append(disciplina)

        curso = Curso(
            nome=curso_nome,
            unidade=unidade_nome,
            duracao_ideal="N/A",
            duracao_minima="N/A",
            duracao_maxima="N/A"
        )
        curso.disciplinas_obrigatorias = obrigatorias
        curso.disciplinas_optativas_eletivas = eletivas
        curso.disciplinas_optativas_livres = livres
        return curso

    except Exception as e:
        print(f"❌ Erro ao extrair curso '{curso_nome}' da unidade '{unidade_nome}': {e}")
        traceback.print_exc()
        return None


def coletar_dados(numero_unidades):
    driver = iniciar_driver()
    wait = WebDriverWait(driver, 15)
    driver.find
    print("🔎 Aguardando dropdown de unidades...")
    select_unidade_elem = wait.until(EC.presence_of_element_located((By.ID, "comboUnidade")))
    select_unidade = Select(select_unidade_elem)

    opcoes_unidades = select_unidade.options[1:numero_unidades + 1]

    for opcao_unidade in opcoes_unidades:
        nome_unidade = opcao_unidade.text.strip()
        print(f"\n📘 Unidade: {nome_unidade}")
        select_unidade.select_by_visible_text(nome_unidade)

        driver.find_element(By.NAME, "btnPegar").click()

        # Espera o comboCurso aparecer
        select_curso_elem = wait.until(EC.presence_of_element_located((By.ID, "comboCurso")))
        select_curso = Select(select_curso_elem)

        unidade = Unidade(nome_unidade)
        for opcao_curso in select_curso.options[1:]:
            nome_curso = opcao_curso.text.strip()
            print(f"  🎓 Curso: {nome_curso}")
            select_curso.select_by_visible_text(nome_curso)
            driver.find
