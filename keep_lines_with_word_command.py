import sublime
import sublime_plugin


class KeepLinesWithWordTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        # print(args)
        keep_word = args['with_word']
        # print(keep_word)

        whole_region = sublime.Region(0, self.view.size())
        if whole_region.empty():
            return

        contents = self.view.substr(whole_region)
        contents = contents.replace('\r\n', '\n').replace('\r', '\n')
        lines = contents.split('\n')
        newlines = []
        # print('contents = ' + contents)
        # print(lines)
        # print(type(newlines))
        for i, line in enumerate(lines):
            if keep_word in line:
                newlines.append(line)
        # print(newlines)
        new_contents = '\n'.join(newlines) + '\n'
        # print(new_contents)
        # sublime.status_message(new_contents)

        # self.view.begin_edit() #no need for st3
        self.view.replace(edit, whole_region, new_contents)
        # self.view.end_edit(edit)


class KeepLinesWithWordCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel('Enter the word you need to keep: ', '', self.on_done, None, self.on_cancel)
        # print('after show_input_panel')

    def on_cancel(self):
        # sublime.status_message('cancel operation')
        pass

    def on_done(self, user_input):
        if len(user_input) == 0:
            sublime.status_message('on input')
            return

        view = self.window.active_view()
        view.run_command('keep_lines_with_word_text', {'with_word': user_input})
