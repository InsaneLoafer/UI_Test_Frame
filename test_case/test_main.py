from page.app import App

class TestMain:
    def test_main(self):
        app = App()
        app.start().main().goto_search()
