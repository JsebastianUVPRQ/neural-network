from manim import *
from manim_slides import Slide

class EnergyConservationQuiz(Slide):
    def construct(self):
        # --- Título ---
        title = Text("Energy Conservation Quiz", font_size=48, color=BLUE)
        self.play(Write(title))
        self.next_slide()

        # --- Energía Cinética (KE) ---
        ke_def = Text("Kinetic Energy: Energy of motion, KE = 1/2 mv²", font_size=32).to_edge(UP)
        # Usamos ReplacementTransform para reemplazar el título anterior
        self.play(ReplacementTransform(title, ke_def))
        self.next_slide()

        # Animación: bola en movimiento
        ball = Circle(radius=0.3, color=RED).shift(LEFT * 4)
        velocity_arrow = Arrow(ball.get_center(), ball.get_center() + RIGHT * 2, color=GREEN)
        ke_label = Text("KE increases with speed", font_size=24).next_to(velocity_arrow, UP)
        
        # Agrupamos los elementos de la animación
        ke_anim_group = VGroup(ball, velocity_arrow, ke_label)

        self.play(FadeIn(ball))
        self.next_slide()
        self.play(GrowArrow(velocity_arrow), Write(ke_label))
        self.next_slide()
        
        # Animamos el grupo junto
        self.play(ke_anim_group.animate.shift(RIGHT * 8), run_time=2)
        self.next_slide()

        # --- Energía Potencial (PE) ---
        pe_def = Text("Potential Energy: Stored energy, PE = mgh", font_size=32).to_edge(UP)
        # Limpiamos la animación anterior y transformamos el título
        self.play(FadeOut(ke_anim_group), ReplacementTransform(ke_def, pe_def))
        self.next_slide()

        # Animación: bola en colina
        hill = Polygon(LEFT * 4 + DOWN*2, ORIGIN + UP * 2, RIGHT * 4 + DOWN*2, color=GREEN, fill_opacity=0.5)
        # Posicionamos la bola en la cima
        ball_pe = Circle(radius=0.3, color=RED).move_to(ORIGIN + UP * 2 + UP*0.3)
        pe_label = Text("PE increases with height", font_size=24).next_to(ball_pe, UP, buff=0.5)
        
        pe_anim_group = VGroup(hill, ball_pe, pe_label)
        self.play(FadeIn(pe_anim_group))
        self.next_slide()

        # --- Conservación ---
        cons = Text("Conservation of Energy: Total energy is conserved", font_size=30).to_edge(UP)
        # Limpiamos la animación de PE y transformamos el título
        self.play(FadeOut(pe_anim_group), ReplacementTransform(pe_def, cons))
        self.next_slide()

        # Animación: bola rodando
        hill_cons = Polygon(LEFT * 4 + DOWN*2, ORIGIN + UP * 2, RIGHT * 4 + DOWN*2, color=GREEN, fill_opacity=0.5)
        ball_cons = Circle(radius=0.3, color=RED).move_to(ORIGIN + UP * 2 + UP*0.3) # Empezar arriba
        
        # Posicionamos los textos de forma más lógica
        pe_decrease = Text("PE decreases", font_size=24, color=BLUE).shift(UP * 3.5)
        ke_increase = Text("KE increases", font_size=24, color=RED).shift(DOWN * 2.5)
        
        self.play(FadeIn(hill_cons), FadeIn(ball_cons))
        self.next_slide()

        # La bola rueda, el texto de PE aparece arriba
        self.play(
            ball_cons.animate.move_to(RIGHT * 4 + DOWN*2 + UP*0.3), # Rodar hasta abajo a la derecha
            Write(pe_decrease),
            run_time=3
        )
        # El texto de KE aparece abajo
        self.play(Write(ke_increase))
        self.next_slide()

        # Agrupamos para limpiar
        cons_anim_group = VGroup(hill_cons, ball_cons, ke_increase, pe_decrease)

        # --- Pregunta 1 ---
        # Limpiamos la escena anterior
        self.play(FadeOut(cons_anim_group), FadeOut(cons))
        self.next_slide()

        # CORRECCIÓN: Posicionar la pregunta arriba
        q1 = Text("What happens to potential energy when an object falls?", font_size=34).to_edge(UP)
        self.play(Write(q1))
        self.next_slide()

        opt1a = Text("A) Increases", font_size=30)
        opt1b = Text("B) Decreases", font_size=30)
        opt1c = Text("C) Stays the same", font_size=30)
        
        # CORRECCIÓN: Posicionar opciones DEBAJO de la pregunta
        options1 = VGroup(opt1a, opt1b, opt1c).arrange(DOWN, buff=0.5).next_to(q1, DOWN, buff=1.0)
        
        self.play(FadeIn(options1, shift=UP))
        self.next_slide()
        
        # Mostramos la respuesta resaltando la opción correcta
        self.play(Circumscribe(opt1b, color=GREEN)) # Resaltar B
        answer1 = Text("Answer: B) Decreases", font_size=32, color=GREEN).next_to(options1, DOWN, buff=1)
        self.play(Write(answer1))
        self.next_slide()

        q1_group = VGroup(q1, options1, answer1) # Grupo para limpiar

        # --- Pregunta 2 ---
        self.play(FadeOut(q1_group)) # Limpiar Q1
        self.next_slide()

        # CORRECCIÓN: Posicionar la pregunta arriba
        q2 = Text("In a closed system, total mechanical energy is...", font_size=36).to_edge(UP)
        self.play(Write(q2))
        self.next_slide()

        opt2a = Text("A) Created", font_size=30)
        opt2b = Text("B) Destroyed", font_size=30)
        opt2c = Text("C) Conserved", font_size=30)
        
        # CORRECCIÓN: Posicionar opciones DEBAJO de la pregunta
        options2 = VGroup(opt2a, opt2b, opt2c).arrange(DOWN, buff=0.5).next_to(q2, DOWN, buff=1.0)
        
        self.play(FadeIn(options2, shift=UP))
        self.next_slide()
        
        self.play(Circumscribe(opt2c, color=GREEN)) # Resaltar C
        answer2 = Text("Answer: C) Conserved", font_size=32, color=GREEN).next_to(options2, DOWN, buff=1)
        self.play(Write(answer2))
        self.next_slide()

        q2_group = VGroup(q2, options2, answer2) # Grupo para limpiar

        # --- Pregunta 3 ---
        self.play(FadeOut(q2_group)) # Limpiar Q2
        self.next_slide()

        # CORRECCIÓN: Posicionar la pregunta arriba
        q3 = Text("What type of energy does a stretched spring have?", font_size=36).to_edge(UP)
        self.play(Write(q3))
        self.next_slide()

        # Animación: resorte
        # Sustitución: usar una línea gruesa como resorte simple (Spring no está definido)
        spring = Line(LEFT * 2, RIGHT * 2, color=GRAY, stroke_width=6)
        spring_label = Text("Elastic Potential Energy", font_size=24).next_to(spring, DOWN)
        spring_group = VGroup(spring, spring_label).shift(UP * 0.5) # Centrarlo un poco

        self.play(FadeIn(spring_group))
        # Simular estiramiento escalando horizontalmente
        self.play(spring.animate.stretch(1.5, 0), run_time=1.5) # Estirar el resorte
        self.next_slide()

        opt3a = Text("A) Kinetic", font_size=30)
        opt3b = Text("B) Gravitational Potential", font_size=30)
        opt3c = Text("C) Elastic Potential", font_size=30)
        
        # CORRECCIÓN: Posicionar opciones DEBAJO de la animación
        options3 = VGroup(opt3a, opt3b, opt3c).arrange(DOWN, buff=0.5).next_to(spring_group, DOWN, buff=1.0)
        
        self.play(FadeIn(options3, shift=UP))
        self.next_slide()
        
        self.play(Circumscribe(opt3c, color=GREEN)) # Resaltar C
        answer3 = Text("Answer: C) Elastic Potential", font_size=32, color=GREEN).next_to(options3, DOWN, buff=1)
        self.play(Write(answer3))
        self.next_slide()

        q3_group = VGroup(q3, spring_group, options3, answer3) # Grupo para limpiar

        # --- Fin ---
        self.play(FadeOut(q3_group)) # Limpiar Q3
        self.next_slide()

        end = Text("Energy Conservation Quiz Complete!", font_size=48, color=YELLOW)
        self.play(Write(end))
        self.next_slide()

        self.play(FadeOut(end)) # Limpieza final