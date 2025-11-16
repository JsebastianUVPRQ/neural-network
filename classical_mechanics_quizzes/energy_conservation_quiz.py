from manim import *
from manim_slides import Slide

class EnergyConservationQuiz(Slide):
    def construct(self):
        # Title
        title = Text("Energy Conservation Quiz", font_size=48, color=BLUE)
        self.play(Write(title))
        self.next_slide()

        # Kinetic Energy
        ke_def = Text("Kinetic Energy: Energy of motion, KE = 1/2 mv²", font_size=32)
        self.play(Transform(title, ke_def))
        self.next_slide()

        # Animation: moving ball
        ball = Circle(radius=0.3, color=RED)
        velocity_arrow = Arrow(ball.get_center(), ball.get_center() + RIGHT * 2, color=GREEN)
        ke_label = Text("KE increases with speed", font_size=24).next_to(velocity_arrow, UP)
        self.play(FadeIn(ball))
        self.next_slide()
        self.play(GrowArrow(velocity_arrow), Write(ke_label))
        self.next_slide()

        # Potential Energy
        pe_def = Text("Potential Energy: Stored energy, PE = mgh", font_size=32)
        self.play(FadeOut(ball), FadeOut(velocity_arrow), FadeOut(ke_label), Write(pe_def))
        self.next_slide()

        # Animation: ball on hill
        hill = Polygon(LEFT * 3 + DOWN, ORIGIN + UP * 2, RIGHT * 3 + DOWN, color=GREEN)
        ball_pe = Circle(radius=0.3, color=RED).shift(LEFT * 2 + UP)
        pe_label = Text("PE increases with height", font_size=24).next_to(ball_pe, UP)
        self.play(FadeIn(hill), FadeIn(ball_pe), Write(pe_label))
        self.next_slide()

        # Conservation
        cons = Text("Conservation of Energy: Total energy is conserved in isolated systems", font_size=30)
        self.play(Transform(pe_label, cons))
        self.next_slide()

        # Animation: ball rolling down hill
        self.play(ball_pe.animate.shift(RIGHT * 4 + DOWN * 2), run_time=3)
        ke_increase = Text("KE increases", font_size=24, color=RED).shift(RIGHT * 2 + UP)
        pe_decrease = Text("PE decreases", font_size=24, color=BLUE).shift(LEFT * 2 + UP)
        self.play(Write(ke_increase), Write(pe_decrease))
        self.next_slide()

        # Question 1
        q1 = Text("What happens to potential energy when an object falls?", font_size=34)
        self.play(FadeOut(hill), FadeOut(ball_pe), FadeOut(ke_increase), FadeOut(pe_decrease), Write(q1))
        self.next_slide()

        opt1a = Text("A) Increases", font_size=30)
        opt1b = Text("B) Decreases", font_size=30)
        opt1c = Text("C) Stays the same", font_size=30)
        options1 = VGroup(opt1a, opt1b, opt1c).arrange(DOWN, buff=0.5)
        self.play(FadeIn(options1))
        self.next_slide()
        answer1 = Text("Answer: B) Decreases", font_size=32, color=GREEN)
        self.play(Transform(options1, answer1))
        self.next_slide()

        # Question 2
        q2 = Text("In a closed system, total mechanical energy is...", font_size=36)
        self.play(Transform(answer1, q2))
        self.next_slide()

        opt2a = Text("A) Created", font_size=30)
        opt2b = Text("B) Destroyed", font_size=30)
        opt2c = Text("C) Conserved", font_size=30)
        options2 = VGroup(opt2a, opt2b, opt2c).arrange(DOWN, buff=0.5)
        self.play(FadeIn(options2))
        self.next_slide()
        answer2 = Text("Answer: C) Conserved", font_size=32, color=GREEN)
        self.play(Transform(options2, answer2))
        self.next_slide()

        # Question 3
        q3 = Text("What type of energy does a stretched spring have?", font_size=36)
        self.play(Transform(answer2, q3))
        self.next_slide()

        # Animation: spring
        spring = Rectangle(width=0.2, height=2, color=GRAY).shift(LEFT)
        spring_label = Text("Elastic Potential Energy", font_size=24).next_to(spring, RIGHT)
        self.play(FadeIn(spring), Write(spring_label))
        self.next_slide()

        opt3a = Text("A) Kinetic", font_size=30)
        opt3b = Text("B) Gravitational Potential", font_size=30)
        opt3c = Text("C) Elastic Potential", font_size=30)
        options3 = VGroup(opt3a, opt3b, opt3c).arrange(DOWN, buff=0.5)
        self.play(FadeIn(options3))
        self.next_slide()
        answer3 = Text("Answer: C) Elastic Potential", font_size=32, color=GREEN)
        self.play(Transform(options3, answer3))
        self.next_slide()

        # End
        end = Text("Energy Conservation Quiz Complete!", font_size=48, color=YELLOW)
        self.play(FadeOut(spring), FadeOut(spring_label), Transform(answer3, end))