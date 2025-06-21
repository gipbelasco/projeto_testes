# models.py
class Disciplina:
    def __init__(self, codigo, nome, creditos_aula, creditos_trabalho,
                 carga_horaria, estagio, pcc, tpa):
        self.codigo = codigo
        self.nome = nome
        self.creditos_aula = creditos_aula
        self.creditos_trabalho = creditos_trabalho
        self.carga_horaria = carga_horaria
        self.estagio = estagio
        self.pcc = pcc
        self.tpa = tpa

class Curso:
    def __init__(self, nome, unidade, duracao_ideal, duracao_minima, duracao_maxima):
        self.nome = nome
        self.unidade = unidade
        self.duracao_ideal = duracao_ideal
        self.duracao_minima = duracao_minima
        self.duracao_maxima = duracao_maxima
        self.disciplinas_obrigatorias = []
        self.disciplinas_optativas_livres = []
        self.disciplinas_optativas_eletivas = []

class Unidade:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []
