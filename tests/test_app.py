from radekholy24.cli.app import main, parse_arguments


class TestParseArguments:
    @staticmethod
    def test(monkeypatch, capsys):
        monkeypatch.setattr("sys.argv", ["file-client"])

        parse_arguments()

        assert not "".join(capsys.readouterr())  # nosec assert_used


class TestMain:
    @staticmethod
    def test(monkeypatch, capsys):
        monkeypatch.setattr("sys.argv", ["file-client"])

        main()

        assert not "".join(capsys.readouterr())  # nosec assert_used
