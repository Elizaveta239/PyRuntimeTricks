import ast
import inspect
import sys
import traceback

from _ast import Assert, Name


def _get_assert_at_line(node, line):
    for child in ast.walk(node):
        if isinstance(child, Assert) and \
                child.lineno == line:
            return child
    return None


def _get_vars_names(source, line):
    node = ast.parse(source)
    assert_node = _get_assert_at_line(node, line)
    children = list(ast.iter_child_nodes(assert_node))
    if len(children) < 1:
        return
    for expr in ast.walk(children[0]):
        if isinstance(expr, Name):
            yield expr.id


def show_vars(e):
    """
    Show variables values used inside assertion statement

    :param e: an instance of AssertionError exception
    """
    tb = e.__traceback__
    frame = tb.tb_frame
    code = frame.f_code
    line = tb.tb_lineno - code.co_firstlineno + 1
    source = inspect.getsource(code)
    traceback.print_tb(tb)
    sys.stderr.write("Variables Values:\n")
    for name in _get_vars_names(source, line):
        if name in frame.f_locals:
            sys.stderr.write(f"{name} = {frame.f_locals[name]}\n")
            sys.stderr.flush()
