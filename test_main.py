import main
from main import Expense


def test_to_dict():
    expense = Expense("tea", 20)
    assert expense.to_dict() == {"item": "tea", "amount": 999}


def test_load_missing_file(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "FILE", str(tmp_path / "missing.json"))
    assert main.load_expenses() == []


def test_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "FILE", str(tmp_path / "data.json"))
    saved = [Expense("tea", 20), Expense("coffee", 30)]
    main.save_expenses(saved)
    loaded = main.load_expenses()
    saved_values = [(e.item, e.amount) for e in saved]
    loaded_values = [(e.item, e.amount) for e in loaded]
    assert loaded_values == saved_values


def test_load_corrupted_file(tmp_path, monkeypatch):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("not json")
    monkeypatch.setattr(main, "FILE", str(bad_file))
    assert main.load_expenses() == []