##### Iris flask app
A simple flask app to predict the species of an iris flower from the given features

##### structure of the application
1. `irisapp` contains the main module that is `iri.py` and a subfolder `templates`
2. `iris.py` is the file for the flask app. It contains the code for predicting the species and also flask definitions. The line `app = flask.Flask(import_name="irisapp")` tells the server to look for flask resources including the main module the `irisapp` folder
3. `templates` folder contains addition flask resources like `css`  and `html` files.
##### running the application
open your terminal and use the `irisapp` as the root directory make sure it contains `iris.py` and the `templates` subfloder
run the following command in the current directory
`python.exe iris.py`
you should the following output                                                                            

`* Restarting with stat`

`* Debugger PIN: 153-073`

`* Running on http://127.0.0.5:6300/ (Press CTRL+C to quit)`

open `iris.html` and input the required values

`flask`,`jinja2`,`werkzeug` among other libraries are required for this example


