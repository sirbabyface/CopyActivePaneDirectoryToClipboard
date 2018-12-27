#
# Load the libraries that are used in these commands.
#
from fman import DirectoryPaneCommand, show_status_message, clipboard
from fman.url import as_human_readable


class CopyActivePanePathToClipboard(DirectoryPaneCommand):
    def __call__(self):
        pane_path = self.pane.get_path()
        clipboard.clear()
        human_path = as_human_readable(pane_path)
        clipboard.set_text(human_path)
        show_status_message('Path ' + human_path + ' copied to the clipboard', 5)

