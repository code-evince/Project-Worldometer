from ply import lex

# Define the tokens for href tags
tokens = (
    'HREF_TAG',
)

# Define the regex patterns for href tags
t_HREF_TAG = r'<a\s+[^>]*href="(.*?)"[^>]*>(.*?)</a>'

# Lexical analysis function to tokenize the input HTML
def lexer(data):
    lexer = lex.lex()
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        yield token

# Example HTML content
html_content = """
<a href="https://example.com">Link 1</a>
<a href="https://example.org">Link 2</a>
<a href="https://example.net">Link 3</a>
"""

# Parse the HTML content and extract href tags and their content
for token in lexer(html_content):
    if token.type == 'HREF_TAG':
        href = token.value[0]
        content = token.value[1]
        print(f"href: {href}, content: {content}")
