import sys
sys.path.append(r".")
import pytest
from com.andreidsaene7.framework.src.main.python.common.core.builder.email_builder import EmailBuilder

# com/andreidsaene7/framework/src/test/python/core/builder/email_builder/test_email_builder.py


@pytest.fixture
def builder():
    return EmailBuilder()


def test_build_email_with_all_fields(builder):
    email = (
        builder
        .with_subject("Relatório Semanal")
        .with_body("Segue o relatório em anexo.")
        .with_to(["andre@empresa.co.mz"])
        .with_cc(["gestor@empresa.co.mz"])
        .with_attachments(["relatorio.xlsx"])
        .build()
    )

    assert email.subject == "Relatório Semanal"
    assert email.body == "Segue o relatório em anexo."
    assert email.to == ["andre@empresa.co.mz"]
    assert email.cc == ["gestor@empresa.co.mz"]
    assert email.attachments == ["relatorio.xlsx"]

