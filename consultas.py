def listar_cursos_por_unidade(unidades):
    if not unidades:
        print("❌ Nenhuma unidade foi carregada.")
        return

    for unidade in unidades:
        print(f"\n📘 Unidade: {unidade.nome}")
        if not unidade.cursos:
            print("   ⚠️ Nenhum curso coletado nesta unidade.")
        for curso in unidade.cursos:
            print(f"  - {curso.nome}")


def dados_de_um_curso(unidades, nome_curso):
    for unidade in unidades:
        for curso in unidade.cursos:
            if curso.nome.lower() == nome_curso.lower():
                print(f"\nCurso: {curso.nome}")
                print(f"Unidade: {curso.unidade}")
                print("Disciplinas obrigatórias:")
                for d in curso.disciplinas_obrigatorias:
                    print(f" - {d.codigo}: {d.nome}")
                return
    print("Curso não encontrado.")
