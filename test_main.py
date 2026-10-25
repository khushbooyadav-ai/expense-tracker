import pytest
import main
from main import Expense


def test_to_dict():
    expense = Expense("tea", 20)
    assert expense.to_dict() == {"item": "tea", "amount": 20}


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


def test_parser_add():
    args = main.build_parser().parse_args(["add", "tea", "20"])
    assert args.command == "add"
    assert args.item == "tea"
    assert args.amount == 20.0


def test_parser_no_command():
    args = main.build_parser().parse_args([])
    assert args.command is None


def test_parser_rejects_bad_amount():
    with pytest.raises(SystemExit):
        main.build_parser().parse_args(["add", "tea", "abc"])


def test_add_expense_save_to_file(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "FILE", str(tmp_path / "data.json"))
    monkeypatch.setattr(main, "expenses", [])
    main.add_expense("tea", 20)
    loaded = main.load_expenses()
    assert [(e.item, e.amount) for e in loaded] == [("tea", 20)]


def test_delete_by_number(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "FILE", str(tmp_path / "data.json"))
    monkeypatch.setattr(main, "expenses", [Expense("tea", 20), Expense("coffee", 30)])
    main.delete_expense_by_number(1)
    assert [e.item for e in main.expenses] == ["coffee"]


def test_delete_invalid_number_logs_warning(tmp_path, monkeypatch, caplog):
    monkeypatch.setattr(main, "FILE", str(tmp_path / "data.json"))
    monkeypatch.setattr(main, "expenses", [Expense("tea", 20)])
    with caplog.at_level("WARNING"):
        main.delete_expense_by_number(5)
    assert "Invalid delete number" in caplog.text
    assert [e.item for e in main.expenses] == ["tea"]

def test_delete_expense_menu(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "FILE", str(tmp_path / "data.json"))
    monkeypatch.setattr(main, "expenses", [Expense("tea", 20), Expense("coffee", 30)])
    monkeypatch.setattr("builtins.input", lambda _: "1")
    main.delete_expense()
    assert [e.item for e in main.expenses] == ["coffee"]