#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
from valid_html import valid_text
from rot13 import rot_text


rotform = """
<html>
    <head>
        <title>Homework 2 Rot 13</title>
    </head>

    <body>
        <h1>Enter some text to ROT13:</h1>
        <form method="post">
            <textarea style="height: 100px; width:400px;"
            name="text">%(text)s</textarea>
	
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""

signup_form = '''
<html>
    <head>
        <title>Sign in</title>
        <style type="text/css">
          .label {text-align: right}
          .error {color: red}
        </style>
    </head>

    <body>
        <h1>Signup</h1>
        <form method="post">
            <table>
                <tr>
                    <td class="label">
                      Username
                    </td>
                    <td>
                      <input type="text" name="username" value="%(username)s">
                    </td>
                    <td class="error">
                     %(username_error)s
                    </td>
                </tr>

                <tr>
                  <td class="label">
                    Password
                  </td>
                  <td>
                    <input type="password" name="password" value="%(password)s">
                  </td>
                  <td class="error">
                    %(password_error)s
                  </td>
                </tr>

                <tr>
                  <td class="label">
                    Verify Password
                  </td>
                  <td>
                    <input type="password" name="verify" value="%(verify)s">
                  </td>
                  <td class="error">
                    %(verify_error)s
                  </td>
                </tr>

                <tr>
                  <td class="label">
                    Email (optional)
                  </td>
                  <td>
                    <input type="text" name="email" value="%(email)s">
                  </td>
                  <td class="error">
                    %(email_error)s
                  </td>
                </tr>
            </table>

            <input type="submit">
        </form>
    </body>
</html>

                
'''

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello world!")

class RotHandler(webapp2.RequestHandler):
    
    def write_form(self, text=""):
        self.response.out.write(rotform % {"text": text})
    
    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get('text')
        rot13 = rot_text(user_text)
        text = valid_text(rot13)
        self.write_form(text)

class SignupHandler(webapp2.RequestHandler):

    def write_form(self, username="", password="", verify="", email="", username_error="", password_error="", verify_error="", email_error=""):
        self.response.out.write(signup_form % {"username" : username,
                                               "password" : password,
                                               "verify" : verify,
                                               "email" : email,
                                               "username_error" : username_error,
                                               "password_error" : password_error,
                                               "verify_error" : verify_error,
                                               "email_error" : email_error})
    def get(self):
        self.write_form()

    def post(self):
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')

        cgi_username = valid_text(user_username)
        cgi_password = valid_text(user_password)
        cgi_verify = valid_text(user_verify)
        cgi_email = valid_text(user_email)

        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""

        error = False

        if not valid_username(user_username):
            username_error = "Need name!"
            error = True

        if not valid_password(user_password):
            password_error = "Need password!"
            error = True

        if not user_verify or not user_password == user_verify:
            verify_error = "Need verification!"
            error = True

        if not valid_email(user_email):
            email_error = "Need email!"
            error = True

        if error:
            cgi_password = ""
            cgi_verify = ""
            self.write_form(cgi_username,
                            cgi_password,
                            cgi_verify,
                            cgi_email,
                            username_error,
                            password_error,
                            verify_error,
                            email_error)
        else:
            self.redirect("/welcome?username=%s" % user_username)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        self.response.out.write("what? %s" % username)


app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/rot13', RotHandler),
                               ('/welcome', WelcomeHandler),
                               ('/signup', SignupHandler)
                               ], debug=True)
