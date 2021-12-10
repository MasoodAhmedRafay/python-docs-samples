# Copyright 2018 Google LLC
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

# [START gae_python38_render_template]
# [START gae_python3_render_template]
#import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
DEFAULT_STUDENTS = (
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry',
)
PLANTS = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets',
}


class Garden(object):
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.lines = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student) * 2
        return [PLANTS[p[i]] for p in self.lines for i in (index, index + 1)]


garden = Garden("VCRRGVRG\nRVGCCGCV")
print(garden.students)
print(garden.lines)
print(garden.plants("Alice"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


# [END gae_python3_render_template]
# [END gae_python38_render_template]
