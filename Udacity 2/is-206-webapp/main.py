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

rotform = """
<font size="6"> <b>Enter some text to ROT13:</b> </font>
<br>
<br>
<form method="post">
	<textarea rows="8" cols="50" type="text" name="rottext">


	</textarea>
	<br>
	<input type="submit">
</form>	
"""

class MainHandler(webapp2.RequestHandler):
    def write_rotform(self):
        self.response.out.write(rotform)


    def get(self):
        self.write_rotform

    def post(self):
        user_text = self.request.get('rottext')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
