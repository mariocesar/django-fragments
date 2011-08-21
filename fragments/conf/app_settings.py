from pygments import lexers
from django.conf import settings

FRAGMENTS_AVAILABLE_LANGUAGES = [(lexer[0], lexer[0]) for lexer in lexers.get_all_lexers()]

