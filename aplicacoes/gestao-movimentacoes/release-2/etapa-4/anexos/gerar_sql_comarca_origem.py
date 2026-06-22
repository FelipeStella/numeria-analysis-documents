"""
Le a planilha "Comarcas a corrigir SIGEP.xlsx" e gera um script .sql com os
INSERTs correspondentes na tabela RheEventoComarcaOrigem (SQL Server).

Uso:
    python gerar_sql_comarca_origem.py
"""

from pathlib import Path
from datetime import datetime

import openpyxl

PASTA_BASE = Path(__file__).parent
PLANILHA = PASTA_BASE / "anexos" / "Comarcas a corrigir SIGEP.xlsx"
SAIDA_SQL = PASTA_BASE / "insert_rhe_evento_comarca_origem.sql"

TABELA = "RheEventoComarcaOrigem"
COLUNAS = ("NrFuncional", "NrVinculo", "NoServidor", "NoComarcaOrigem", "DtInicioAtividades")


def escapar_string(valor: str) -> str:
    return str(valor).replace("'", "''")


def formatar_data(valor: datetime) -> str:
    return valor.strftime("%Y-%m-%d")


def ler_linhas(caminho: Path):
    wb = openpyxl.load_workbook(caminho, data_only=True)
    ws = wb.active
    for linha in ws.iter_rows(min_row=2, values_only=True):
        if linha is None or all(v is None for v in linha):
            continue
        nr_funcional, nr_vinculo, no_servidor, no_comarca_origem, dt_inicio_atividades = linha
        yield {
            "NrFuncional": str(nr_funcional),
            "NrVinculo": int(nr_vinculo),
            "NoServidor": str(no_servidor).strip(),
            "NoComarcaOrigem": str(no_comarca_origem).strip(),
            "DtInicioAtividades": formatar_data(dt_inicio_atividades),
        }


def gerar_insert(registro: dict) -> str:
    valores = (
        f"'{escapar_string(registro['NrFuncional'])}'",
        str(registro["NrVinculo"]),
        f"'{escapar_string(registro['NoServidor'])}'",
        f"'{escapar_string(registro['NoComarcaOrigem'])}'",
        f"'{registro['DtInicioAtividades']}'",
    )
    return f"INSERT INTO {TABELA} ({', '.join(COLUNAS)})\nVALUES ({', '.join(valores)});"


def main():
    registros = list(ler_linhas(PLANILHA))

    linhas_sql = [
        f"-- Gerado a partir de '{PLANILHA.name}' ({len(registros)} registros)",
        "",
    ]
    linhas_sql.extend(gerar_insert(r) for r in registros)

    SAIDA_SQL.write_text("\n".join(linhas_sql) + "\n", encoding="utf-8")
    print(f"{len(registros)} INSERTs gerados em: {SAIDA_SQL}")


if __name__ == "__main__":
    main()
