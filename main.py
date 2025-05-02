from textual.app import App, ComposeResult
from textual.widgets import Tree, Tabs, Tab, TextArea

class MainApp(App):
    CSS_PATH = "style.tcss"

    def composs(self) -> ComposeResult:

        #file tree
        tree: Tree[str] = tree("dune")
        tree.root.expand()

        #tabs
        yield Tabs(
            Tab("help.txt", id="tab1")
        )

        #editor
        yield TextArea.code.editor(language="python")

if __name__ == "__main__":
    app = MainApp()
    app.run()