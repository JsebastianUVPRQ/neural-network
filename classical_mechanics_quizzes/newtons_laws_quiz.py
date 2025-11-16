from manim import *
from manim_slides import Slide

class NewtonsLawsQuiz(Slide):
    def construct(self):
        # Title
        title = Text("Newton's Laws of Motion Quiz", font_size=48, color=BLUE)
        self.play(Write(title))
        self.next_slide()

        # First Law
        law1 = Text("Newton's First Law: An object at rest stays at rest, and an object in motion stays in motion unless acted upon by a net force.", font_size=28)
        self.play(Transform(title, law1))
        self.next_slide()

        # Animation: ball on table, then table disappears
        ball = Circle(radius=0.3, color=RED).shift(UP * 2)
        table = Rectangle(width=4, height=0.2, color=BROWN).shift(DOWN * 1.5)
        self.play(FadeIn(ball), FadeIn(table))
        self.next_slide()
        self.play(FadeOut(table))
        self.play(ball.animate.shift(DOWN * 3), run_time=2)  # falls
        self.next_slide()

        # Question 1
        q1 = Text("What does Newton's First Law state?", font_size=36)
        self.play(FadeOut(ball), Write(q1))
        self.next_slide()

        # Options
        opt1a = Text("A) Force equals mass times acceleration", font_size=30)
        opt1b = Text("B) Inertia keeps objects moving or at rest", font_size=30)
        opt1c = Text("C) Every action has an equal reaction", font_size=30)
        options1 = VGroup(opt1a, opt1b, opt1c).arrange(DOWN, buff=0.5)
        self.play(FadeIn(options1))
        self.next_slide()
        answer1 = Text("Answer: B) Inertia keeps objects moving or at rest", font_size=32, color=GREEN)
        self.play(Transform(options1, answer1))
        self.next_slide()

        # Second Law
        law2 = Text("Newton's Second Law: F = ma", font_size=36)
        self.play(Transform(answer1, law2))
        self.next_slide()

        # Animation: force on box
        box = Square(side_length=1, color=BLUE)
        force_arrow = Arrow(box.get_right(), box.get_right() + RIGHT * 2, color=RED)
        accel_arrow = Arrow(box.get_center(), box.get_center() + RIGHT, color=GREEN)
        self.play(FadeIn(box))
        self.next_slide()
        self.play(GrowArrow(force_arrow))
        self.next_slide()
        self.play(GrowArrow(accel_arrow))
        self.next_slide()

        # Question 2
        q2 = Text("If force doubles and mass stays the same, what happens to acceleration?", font_size=32)
        self.play(FadeOut(box), FadeOut(force_arrow), FadeOut(accel_arrow), Write(q2))
        self.next_slide()

        opt2a = Text("A) Doubles", font_size=30)
        opt2b = Text("B) Halves", font_size=30)
        opt2c = Text("C) Stays the same", font_size=30)
        options2 = VGroup(opt2a, opt2b, opt2c).arrange(DOWN, buff=0.5)
        self.play(FadeIn(options2))
        self.next_slide()
        answer2 = Text("Answer: A) Doubles", font_size=32, color=GREEN)
        self.play(Transform(options2, answer2))
        self.next_slide()

        # Third Law
        law3 = Text("Newton's Third Law: For every action, there is an equal and opposite reaction.", font_size=32)
        self.play(Transform(answer2, law3))
        self.next_slide()

        # Animation: two balls colliding
        ball1 = Circle(radius=0.3, color=RED).shift(LEFT * 2)
        ball2 = Circle(radius=0.3, color=BLUE).shift(RIGHT * 2)
        arrow1 = Arrow(ball1.get_center(), ball1.get_center() + RIGHT, color=RED)
        arrow2 = Arrow(ball2.get_center(), ball2.get_center() + LEFT, color=BLUE)
        self.play(FadeIn(ball1), FadeIn(ball2))
        self.next_slide()
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.next_slide()

        # Question 3
        q3 = Text("When you push on a wall, why doesn't it move?", font_size=36)
        self.play(FadeOut(ball1), FadeOut(ball2), FadeOut(arrow1), FadeOut(arrow2), Write(q3))
        self.next_slide()

        opt3a = Text("A) It's too heavy", font_size=30)
        opt3b = Text("B) The wall pushes back equally", font_size=30)
        opt3c = Text("C) Gravity holds it", font_size=30)
        options3 = VGroup(opt3a, opt3b, opt3c).arrange(DOWN, buff=0.5)
        self.play(FadeIn(options3))
        self.next_slide()
        answer3 = Text("Answer: B) The wall pushes back equally", font_size=32, color=GREEN)
        self.play(Transform(options3, answer3))
        self.next_slide()

        # End
        end = Text("Newton's Laws Quiz Complete!", font_size=48, color=YELLOW)
        self.play(Transform(answer3, end))