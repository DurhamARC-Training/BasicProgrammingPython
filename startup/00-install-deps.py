import piplite

# Install the dependencies as the jupyterlite starts up.
# Needs to be pure python or available within pyodide.

await piplite.install([
    'jupyterquiz'
])