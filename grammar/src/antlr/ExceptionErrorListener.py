from antlr4.error.ErrorListener import ErrorListener


class ExceptionErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        raise Exception(recognizer, offending_symbol, line, column, msg, e)

    def reportAmbiguity(self, recognizer, dfa, start_index, stop_index, exact, ambiguity_alts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, start_index, stop_index, conflicting_alts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, start_index, stop_index, prediction, configs):
        pass
