import sys

from importlib.util import find_spec

async def _ensure_dependencies():
    """Ensure jupyterquiz is installed in Pyodide."""
    if find_spec('jupyterquiz') is None:
        import micropip
        await micropip.install('jupyterquiz>=2.9')

# Auto-install on import
if 'pyodide' in sys.modules:  # Only in browser
    import asyncio
    # Check if we're in a running event loop
    try:
        loop = asyncio.get_running_loop()
        # Already in async context, can await directly
        await _ensure_dependencies()
    except RuntimeError:
        # No running loop, create one
        asyncio.run(_ensure_dependencies())

# Now import normally
import jupyterquiz

def display_quiz(json_path):
    colors = {
        '--jq-multiple-choice-bg': '#66295B', 
        '--jq-mc-button-bg': '#fafafa', 
        '--jq-mc-button-border': '#66295B', 
        '--jq-many-choice-bg': '#66295B', 
        '--jq-numeric-bg': '#66295B', 
        '--jq-numeric-input-bg': '#fafafa', 
        '--jq-numeric-input-label': '#2d2d2d', 
        '--jq-numeric-input-shadow': '#4A1D42', 
        '--jq-string-bg': '#66295B', 
        '--jq-incorrect-color': '#c80202', 
        '--jq-correct-color': '#5CB85C', 
        '--jq-link-color': '#B8A7D6'
    }
    return jupyterquiz.display_quiz(json_path, border_radius=1, colors=colors)
