from manim import *
from manim_slides import Slide

class TitleSlide(Slide):
    def construct(self):
        title = Text("Mecánica Clásica: Movimiento de Proyectiles", font_size=48)
        subtitle = Text("Animación Interactiva con Preguntas", font_size=32)
        self.play(Write(title))
        self.next_slide()
        self.play(Write(subtitle))
        self.next_slide()

class AnimationSlide(Slide):
    def construct(self):
        # Crear ejes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 5, 1],
            axis_config={"color": BLUE},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Trayectoria parabólica
        parabola = axes.plot(lambda x: -0.1 * x**2 + x, x_range=[0, 9], color=RED)

        # Punto móvil
        dot = Dot(color=YELLOW).move_to(axes.c2p(0, 0))

        # Animación
        self.play(Create(axes), Write(labels))
        self.next_slide()
        self.play(Create(parabola))
        self.next_slide()
        self.play(MoveAlongPath(dot, parabola), run_time=3)
        self.next_slide()

class QuizSlide(Slide):
    def construct(self):
        question = Text("¿Cuál es la ecuación del movimiento parabólico?", font_size=36)
        option1 = Text("1. y = x^2", font_size=28)
        option2 = Text("2. y = -0.5*g*t^2 + v0*t", font_size=28)
        option3 = Text("3. y = sin(x)", font_size=28)

        self.play(Write(question))
        self.next_slide()
        self.play(Write(option1))
        self.next_slide()
        self.play(Write(option2))
        self.next_slide()
        self.play(Write(option3))
        self.next_slide()

        answer = Text("Respuesta correcta: 2", font_size=32, color=GREEN)
        self.play(Write(answer))
        self.next_slide()

# Para generar slides, ejecutar: manim-slides convert projectile_quiz TitleSlide AnimationSlide QuizSlide -c html