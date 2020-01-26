from datetime import date
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from calculadora_do_cidadao import Igpm, Inpc, Ipca, Ipca15, IpcaE, Selic
from calculadora_do_cidadao.__main__ import main

ADAPTERS = (Igpm, Inpc, Ipca, Ipca15, IpcaE, Selic)


def test_export_all(mocker):
    for count, Adapter in enumerate(ADAPTERS, 1):
        download = mocker.patch.object(Adapter, "download")
        download.return_value = (
            (date(2019, 12, 1), Decimal(count)),
            (date(2020, 1, 1), Decimal(count * 1.5)),
        )

    with TemporaryDirectory() as _tmp:
        path = Path(_tmp) / "calculadora-do-cidadao.csv"
        main(path)
        content = path.read_text()

    for Adapter in ADAPTERS:
        assert Adapter.__name__.lower() in content

    assert len(content.split()) == len(ADAPTERS * 2) + 1  # plus 1 for header