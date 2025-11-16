# 3Blue1Brown-like Interactive Quizzes on Classical Mechanics

This project contains three interactive quizzes on classical mechanics topics, created using Manim and Manim-Slides for an animated, educational experience similar to 3Blue1Brown videos.

## Quizzes

1. **Kinematics Quiz** (`kinematics_quiz.py`): Covers speed vs velocity, average speed calculation, and acceleration.
2. **Newton's Laws Quiz** (`newtons_laws_quiz.py`): Explores the three laws of motion with animations.
3. **Energy Conservation Quiz** (`energy_conservation_quiz.py`): Discusses kinetic energy, potential energy, and conservation principles.

## Setup

1. Ensure you have Python 3.7+ installed.
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```
   pip install manim manim-slides
   ```

## Running the Quizzes

To run an interactive quiz, first convert it to HTML for web-based interaction:

```
manim-slides convert <filename>.py <ClassName> --to html
```

For example:

- Kinematics: `manim-slides convert kinematics_quiz.py KinematicsQuiz --to html`
- Newton's Laws: `manim-slides convert newtons_laws_quiz.py NewtonsLawsQuiz --to html`
- Energy: `manim-slides convert energy_conservation_quiz.py EnergyConservationQuiz --to html`

This creates a `slides` directory with HTML files. Open `slides/index.html` in your web browser to interact with the quiz using keyboard navigation or on-screen controls. Each quiz features animated explanations followed by multiple-choice questions with revealed answers.

## Features

- Animated explanations of concepts
- Interactive slide navigation
- Multiple-choice questions with instant feedback
- Visual demonstrations of physical principles

Enjoy learning classical mechanics in an engaging, visual way!