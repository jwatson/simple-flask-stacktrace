import logging
import sys

from flask import Flask


###
### Flask application setup.
###
app = Flask(__name__)
app.debug = True

# Configure logging.
app.logger.setLevel(logging.DEBUG)
del app.logger.handlers[:]

handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)
handler.formatter = logging.Formatter(
    fmt=u"%(asctime)s level=%(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
app.logger.addHandler(handler)


@app.route("/")
def failwhale():
    x = [0],
    x[500]

if __name__ == "__main__":
    app.run()
