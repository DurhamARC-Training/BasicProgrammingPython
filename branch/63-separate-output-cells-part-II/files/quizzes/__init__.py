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
