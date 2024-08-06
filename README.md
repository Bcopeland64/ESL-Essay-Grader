# ESL-Essay-Grader

# Easy Essay Grader

## Introduction

The Essay Grader is an interactive application developed to assist students and educators at Al Hussein Technical University in evaluating and improving academic essays. Utilizing advanced language processing techniques, the grader focuses on grammar, spelling, and punctuation, providing detailed feedback and a quantified assessment of each essay.

## Features

- **Grammar, Spelling, and Punctuation Evaluation**: The tool automatically checks essays for grammatical errors, spelling mistakes, and punctuation issues.
- **Detailed Feedback**: Provides specific suggestions for improving grammar and correcting spelling errors.
- **Cumulative Scoring**: Calculates an overall score based on grammar, spelling, and punctuation performance.
- **Graphical Feedback Representation**: Visualizes the scores in an easy-to-understand pie chart.
- **User-Friendly Interface**: Built with Gradio for an intuitive and accessible user experience.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.6 or higher.
- Gradio, Plotly, language_tool_python, Pillow, and pyspellchecker Python packages.

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install gradio plotly language_tool_python Pillow pyspellchecker

### Usage

- Open the application link in a web browser.
- Enter or paste the essay text into the input field.
- Submit the text to receive a detailed analysis, including scores and feedback on various aspects of the essay.

### How It Works

1. Essay Submission: Users submit an essay for grading.
2. Automated Analysis: The script performs automated checks for grammar, spelling, and punctuation.
3. Score Calculation: Scores are calculated for each category, and a cumulative score is derived.
4. Feedback Generation: Detailed feedback is provided for identified errors.Result Display: Scores and feedback are displayed to the user through the Gradio interface.
