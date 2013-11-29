########
##def escape_html(s):
##    for (i, o) in (("&", "&amp;"),
##                   (">", "%gt;"),
##                   ("<", "&lt;"),
##                   ('"', "&quot")):
##        s = s.replace(i, o)
##    return s
##print escape_html('hello <>"&')
########


import cgi
def valid_text(s):
    return cgi.escape(s, quote = True)

print valid_text('"hello, & = &amp;"')
print valid_text('">')
