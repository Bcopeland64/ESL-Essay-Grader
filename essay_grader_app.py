import gradio as gr
import plotly.graph_objects as go
import plotly.io as pio
import language_tool_python
from spellchecker import SpellChecker
from PIL import Image

spell = SpellChecker()


def grade_essay(essay):
    # Initialize language tool
    tool = language_tool_python.LanguageTool('en-US')

    # Initialize spell checker
    spell = SpellChecker()

    # Perform grammar and punctuation check
    grammar_errors = tool.check(essay)
    punctuation_errors = essay.count('.') + essay.count('!') + essay.count('?')

    # Perform spelling check
    misspelled = spell.unknown(essay.split())
    spelling_errors = [word for word in misspelled if word.isalpha()]

    # Calculate scores
    grammar_score = max(0, 10 - len(grammar_errors)) / 10 * 100
    spelling_score = max(0, 10 - len(spelling_errors)) / 10 * 100
    punctuation_score = max(0, 10 - punctuation_errors) / 10 * 100

    cumulative_score = (grammar_score + spelling_score + punctuation_score) / 3

    return cumulative_score, grammar_score, spelling_score, punctuation_score, grammar_errors, spelling_errors


def generate_feedback(grammar_errors, spelling_errors):
    feedback = ""

    if grammar_errors:
        feedback += "Grammar and Punctuation Errors:\n"
        for error in grammar_errors:
            feedback += f"- {error.message.capitalize()} (Suggested correction: {error.replacements[0]})\n"
        feedback += "\n"

    if spelling_errors:
        feedback += "Spelling Errors:\n"
        for error in spelling_errors:
            feedback += f"- {error.capitalize()} (Suggested correction: {spell.correction(error)})\n"
        feedback += "\n"

    return feedback


def plot_scores(scores):
    labels = ['Grammar', 'Spelling', 'Punctuation']
    values = [scores[1], scores[2], scores[3]]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    return fig


def essay_grader(essay):
    scores = grade_essay(essay)
    feedback = generate_feedback(scores[4], scores[5])

    return f"""
    Cumulative Score: {scores[0]:.2f}
    Grammar Score: {scores[1]:.2f}
    Spelling Score: {scores[2]:.2f}
    Punctuation Score: {scores[3]:.2f}

    Feedback:
    {feedback}
    """


# Function to display the Al Hussein Technical University logo
def display_logo():
    logo_path = "/home/brandon/HTU/unnamed.jpg"  # Replace with the actual path to the logo image (JPEG format)
    logo_image = Image.open(logo_path)
    return gr.outputs.Image(logo_image, label="Al Hussein Technical University Logo", type="pil")


iface = gr.Interface(
    fn=essay_grader,
    inputs="text",
    outputs="text",
    title="Al Hussein Technical University Essay Grader",
    server_name="0.0.0.0",
    server_port=7860,
    examples=[["Example essay text"]],
    thumbnail=display_logo
)
iface.launch(share=True)


