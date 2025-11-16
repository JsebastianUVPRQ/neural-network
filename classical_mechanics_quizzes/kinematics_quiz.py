from manim import *
from manim_slides import Slide

class KinematicsQuiz(Slide):
    def construct(self):
        # Title slide
        title = Text("Kinematics Quiz", font_size=48, color=BLUE)
        self.play(Write(title))
        self.next_slide()

        # Question 1: Difference between speed and velocity
        question1 = Text("What is the difference between speed and velocity?", font_size=36)
        self.play(Transform(title, question1))
        self.next_slide()

        # Explanation animation
        speed_def = Text("Speed: Scalar quantity, magnitude only", font_size=30, color=RED)
        velocity_def = Text("Velocity: Vector quantity, magnitude and direction", font_size=30, color=GREEN)

        self.play(Write(speed_def))
        self.next_slide()
        self.play(Transform(speed_def, velocity_def))
        self.next_slide()

        # Visual: arrow for velocity
        arrow = Arrow(ORIGIN, RIGHT * 2, color=GREEN)
        speed_label = Text("Speed: 10 m/s", font_size=24).next_to(arrow, UP)
        velocity_label = Text("Velocity: 10 m/s East", font_size=24).next_to(arrow, UP)

        self.play(FadeIn(arrow), Write(speed_label))
        self.next_slide()
        self.play(Transform(speed_label, velocity_label))
        self.next_slide()

        # Question 2: Average speed calculation
        question2 = Text("A car travels 200 km in 4 hours. What is its average speed?", font_size=36)
        self.play(Transform(velocity_label, question2), FadeOut(arrow))
        self.next_slide()

        # Options
        opt_a = Text("A) 50 km/h", font_size=30)
        opt_b = Text("B) 100 km/h", font_size=30)
        opt_c = Text("C) 800 km/h", font_size=30)
        options = VGroup(opt_a, opt_b, opt_c).arrange(DOWN, buff=0.5)
        self.play(FadeIn(options))
        self.next_slide()

        # Reveal answer
        answer = Text("Correct Answer: A) 50 km/h", font_size=36, color=GREEN)
        self.play(Transform(options, answer))
        self.next_slide()

        # Question 3: Acceleration
        question3 = Text("What is acceleration?", font_size=36)
        self.play(Transform(answer, question3))
        self.next_slide()

        # Animation: changing velocity
        initial_v = Arrow(ORIGIN, RIGHT, color=BLUE).shift(LEFT * 2)
        final_v = Arrow(ORIGIN, RIGHT * 2, color=BLUE).shift(RIGHT * 2)
        accel_arrow = Arrow(initial_v.get_end(), final_v.get_end(), color=RED, buff=0)

        accel_label = Text("Acceleration: Change in velocity over time", font_size=24).next_to(accel_arrow, UP)

        self.play(FadeIn(initial_v), Write(Text("Initial Velocity", font_size=20).next_to(initial_v, DOWN)))
        self.next_slide()
        self.play(FadeIn(final_v), Write(Text("Final Velocity", font_size=20).next_to(final_v, DOWN)))
        self.next_slide()
        self.play(FadeIn(accel_arrow), Write(accel_label))
        self.next_slide()

        # End quiz
        end_text = Text("Kinematics Quiz Complete!", font_size=48, color=YELLOW)
        self.play(FadeOut(accel_label), FadeOut(initial_v), FadeOut(final_v), FadeOut(accel_arrow), Write(end_text))