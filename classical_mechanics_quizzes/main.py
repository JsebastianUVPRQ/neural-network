import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Mecánica Clásica: Potencial Central",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Estilos CSS Personalizados ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4F46E5;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #6B7280;
        text-align: center;
        margin-bottom: 2rem;
    }
    /* Estilo para la caja de matemáticas */
    .math-box {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    /* Ajuste para radios */
    .stRadio label {
        font-size: 1.1rem !important;
        padding-bottom: 10px;
    }
    .theory-text {
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #374151;
        text-align: justify;
    }
    .h3-custom {
        color: #1E40AF;
        margin-top: 2rem;
        border-bottom: 2px solid #E5E7EB;
        padding-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Funciones de Física ---
def get_veff(r, L, m, alpha):
    r = np.maximum(r, 0.01) 
    return (L**2) / (2 * m * r**2) - (alpha / r)

# --- Inicialización de Estado ---
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

# --- Encabezado ---
st.markdown('<div class="main-header">Mecánica Clásica</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">El Problema de los Dos Cuerpos y Fuerzas Centrales</div>', unsafe_allow_html=True)

# --- Pestañas ---
tab1, tab2, tab3 = st.tabs(["📖 Teoría Avanzada", "❓ Quiz Conceptual", "📈 Laboratorio Virtual"])

# ==========================================
# PESTAÑA 1: TEORÍA (ESTILO GOLDSTEIN)
# ==========================================
with tab1:
    st.markdown('<div class="theory-text">', unsafe_allow_html=True)
    
    st.markdown("### 1. Formalismo Hamiltoniano en Campos Centrales")
    st.markdown("""
    Consideremos una partícula de masa $m$ moviéndose bajo la influencia de un campo de fuerza central conservativo derivado de un potencial $U(r)$. 
    Debido a la simetría esférica del problema, el potencial es invariante bajo rotaciones, lo que implica la conservación del vector momento angular $\\vec{L}$. 
    Esta conservación restringe el movimiento de la partícula a un plano fijo perpendicular a $\\vec{L}$.
    """)
    
    st.markdown("**Coordenadas Esféricas:**")
    st.markdown("""
    Para explotar la simetría, escribimos el Hamiltoniano en coordenadas esféricas $(r, \\theta, \\phi)$. 
    La energía cinética en estas coordenadas es $T = \\frac{m}{2}(\\dot{r}^2 + r^2\\dot{\\theta}^2 + r^2\\sin^2\\theta\\dot{\\phi}^2)$. 
    Los momentos canónicos conjugados se definen como $p_i = \\partial L / \\partial \\dot{q}_i$:
    """)

    st.markdown('<div class="math-box">', unsafe_allow_html=True)
    st.latex(r"p_r = m\dot{r}, \quad p_\theta = mr^2\dot{\theta}, \quad p_\phi = mr^2\sin^2\theta\dot{\phi}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("El Hamiltoniano $H = T + U$ expresado en términos de los momentos resulta en:")
    
    st.markdown('<div class="math-box">', unsafe_allow_html=True)
    st.latex(r"H(q, p) = \frac{1}{2m} \left[ p_r^2 + \frac{p_\theta^2}{r^2} + \frac{p_\phi^2}{r^2\sin^2\theta} \right] + U(r)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 2. Coordenadas Cíclicas y Reducción")
    st.markdown("""
    Observamos que la coordenada $\\phi$ es **cíclica** (no aparece explícitamente en $H$), por lo tanto, su momento conjugado $p_\\phi$ es una constante de movimiento:
    $$p_\\phi = \\text{cte} = L_z$$
    
    Dada la conservación de la dirección del momento angular, podemos simplificar el problema eligiendo el sistema de coordenadas tal que el movimiento ocurra en el plano ecuatorial. 
    Fijamos $\\theta = \\pi/2$, lo que implica $p_\\theta = 0$. El Hamiltoniano se reduce drásticamente:
    """)
    
    st.markdown("### 3. El Problema Unidimensional Equivalente")
    st.markdown("""
    Sustituyendo las condiciones del plano ecuatorial y denotando $p_\\phi = L$ (el módulo del momento angular total), obtenemos una ecuación que depende únicamente de la coordenada radial $r$ y su momento $p_r$. 
    Esto es formalmente equivalente a un problema de una sola dimensión ficticio:
    """)

    st.markdown('<div class="math-box">', unsafe_allow_html=True)
    st.latex(r"H_{1D} = \frac{p_r^2}{2m} + \frac{L^2}{2mr^2} + U(r) = E")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    El segundo término, $\\frac{L^2}{2mr^2}$, surge matemáticamente de la energía cinética angular, pero físicamente actúa como un **potencial repulsivo** que impide que la partícula colapse al origen (para $L \\neq 0$). 
    Definimos entonces el **Potencial Efectivo** $V_{eff}(r)$:
    """)

    st.markdown('<div class="math-box">', unsafe_allow_html=True)
    st.latex(r"V_{eff}(r) \equiv \frac{L^2}{2mr^2} - \frac{\alpha}{r}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 4. Análisis Cualitativo de las Órbitas")
    st.markdown("""
    La ecuación de movimiento radial queda determinada por la conservación de la energía: $E = T_r + V_{eff}$. 
    Podemos clasificar las órbitas analizando los puntos de retorno donde $\\dot{r}=0$ (o $p_r=0$), es decir, donde $V_{eff}(r) = E$:
    
    * **$E > 0$**: La partícula tiene suficiente energía para escapar a $r \\to \\infty$. Órbita **hiperbólica** (no ligada).
    * **$E < 0$**: La partícula está confinada entre dos radios de retorno $r_{min}$ (perihelio) y $r_{max}$ (afelio). Órbita **elíptica** (ligada).
    * **$E = V_{min}$**: La partícula yace en el fondo del pozo de potencial. $r$ es constante. Órbita **circular**.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# PESTAÑA 2: QUIZ
# ==========================================
with tab2:
    st.markdown("### Test de Conceptos")
    st.caption("Selecciona la respuesta correcta para validar tu comprensión.")

    questions = [
        {
            "id": "q1",
            "q": "¿Por qué el término $L^2/2mr^2$ se denomina barrera centrífuga?",
            "opts": [
                r"Porque atrae a la partícula hacia el origen rápidamente.",
                r"Porque actúa como un potencial repulsivo que domina a distancias cortas ($r \to 0$).",
                r"Porque es constante y no depende de $r$."
            ],
            "correct": 1, 
            "expl": "Al depender de $1/r^2$, crece más rápido que el potencial atractivo ($1/r$) cuando $r$ es pequeño, 'empujando' a la partícula hacia afuera."
        },
        {
            "id": "q2",
            "q": "En el Hamiltoniano reducido 1D, ¿qué representa $p_r^2/2m$?",
            "opts": [
                r"La energía cinética total del sistema.",
                r"La energía potencial efectiva.",
                r"Solo la parte radial de la energía cinética."
            ],
            "correct": 2,
            "expl": "La energía cinética total se ha dividido en una parte radial ($p_r^2/2m$) y una angular que se ha absorbido en $V_{eff}$."
        },
        {
            "id": "q3",
            "q": "¿Qué condición define una órbita circular estable en este formalismo?",
            "opts": [
                r"Cuando la energía $E$ es positiva.",
                r"Cuando $p_r = 0$ en todo momento (el radio no cambia).",
                r"Cuando el momento angular $L = 0$."
            ],
            "correct": 1,
            "expl": "En una órbita circular, la distancia al centro es constante, por lo tanto no hay velocidad radial ($\dot{r}=0 \Rightarrow p_r=0$) y la partícula está en el mínimo de $V_{eff}$."
        }
    ]

    with st.form("quiz_form"):
        for i, q in enumerate(questions):
            st.markdown(f"**{i+1}. {q['q']}**")
            prev_val = st.session_state.quiz_answers.get(q['id'], None)
            
            choice = st.radio(
                "Selecciona:", 
                q['opts'], 
                index=q['opts'].index(prev_val) if prev_val in q['opts'] else 0,
                key=q['id'],
                label_visibility="collapsed"
            )
            st.markdown("---")

        submitted = st.form_submit_button("Verificar Resultados")
        
        if submitted:
            st.session_state.show_results = True
            for q in questions:
                st.session_state.quiz_answers[q['id']] = st.session_state[q['id']]

    if st.session_state.show_results:
        score = 0
        for i, q in enumerate(questions):
            user_ans = st.session_state.quiz_answers.get(q['id'])
            correct_ans = q['opts'][q['correct']]
            
            if user_ans == correct_ans:
                score += 1
                st.success(f"✅ Pregunta {i+1}: Correcto. {q['expl']}")
            else:
                st.error(f"❌ Pregunta {i+1}: Incorrecto. {q['expl']}")
        
        st.metric("Puntuación", f"{score}/{len(questions)}")

# ==========================================
# PESTAÑA 3: SIMULACIÓN
# ==========================================
with tab3:
    with st.sidebar:
        st.header("🎛️ Controles de Laboratorio")
        st.markdown("Modifica las constantes de movimiento:")
        E_val = st.slider("Energía Total (E)", -2.0, 2.0, -0.5, 0.1)
        L_val = st.slider("Momento Angular (L)", 0.5, 3.0, 1.2, 0.1)
        
        st.markdown("Parámetros del Sistema:")
        m_val = st.slider("Masa (m)", 0.5, 2.0, 1.0, 0.1)
        alpha_val = st.slider("Fuerza del Potencial (α)", 0.5, 3.0, 1.5, 0.1)
        
        st.info("""
        **Interpretación:**
        * La línea roja discontinua es tu Energía Total.
        * La partícula solo puede existir donde $E \\geq V_{eff}$ (zona verde).
        """)

    # Cálculos
    r = np.linspace(0.1, 8.0, 600)
    veff = get_veff(r, L_val, m_val, alpha_val)
    
    # Cálculo de p_r
    kinetic = E_val - veff
    valid_mask = kinetic >= 0
    
    r_valid = r[valid_mask]
    
    if len(r_valid) > 0:
        pr_pos = np.sqrt(2 * m_val * kinetic[valid_mask])
        pr_neg = -pr_pos
    else:
        r_valid = []
        pr_pos = []
        pr_neg = []

    col_graph1, col_graph2 = st.columns(2)

    # Gráfica 1: V_eff
    with col_graph1:
        fig_pot = go.Figure()
        fig_pot.add_trace(go.Scatter(x=r, y=veff, name='V_eff(r)', line=dict(color='#2563eb', width=3)))
        fig_pot.add_hline(y=E_val, line_dash="dash", line_color="#dc2626", annotation_text=f"E = {E_val}")
        
        # Sombreado zona permitida
        if len(r_valid) > 0:
            fig_pot.add_vrect(x0=r_valid[0], x1=r_valid[-1], fillcolor="green", opacity=0.1, line_width=0)
            # Marcar puntos de retorno
            fig_pot.add_trace(go.Scatter(
                x=[r_valid[0], r_valid[-1]], y=[E_val, E_val],
                mode='markers', marker=dict(color='black', size=8), name='Puntos de Retorno'
            ))

        fig_pot.update_layout(
            title="<b>Potencial Efectivo</b> <br><i>Competencia entre atracción y barrera centrífuga</i>", 
            xaxis_title="Distancia radial r", 
            yaxis_title="Energía",
            yaxis_range=[-4, 4], height=400, margin=dict(l=20, r=20, t=60, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_pot, use_container_width=True)

    # Gráfica 2: Espacio Fase
    with col_graph2:
        fig_phase = go.Figure()
        
        if len(r_valid) > 0:
            # Crear ciclo cerrado visualmente
            r_plot = np.concatenate([r_valid, r_valid[::-1]])
            pr_plot = np.concatenate([pr_pos, pr_neg[::-1]])
            
            fig_phase.add_trace(go.Scatter(
                x=r_plot, y=pr_plot, mode='lines', name='Trayectoria de Fase',
                line=dict(color='#7c3aed', width=3), fill='toself', fillcolor='rgba(124, 58, 237, 0.1)'
            ))
            
            # Vector de flujo (flechas)
            step = max(1, len(r_plot) // 12)
            for i in range(0, len(r_plot), step):
                # Añadir pequeñas flechas indicando la dirección del flujo
                pass # (Omitido para mantener limpieza visual, se entiende por la animación)

        else:
            fig_phase.add_annotation(text="Región Clásicamente Prohibida", showarrow=False, font=dict(size=20, color="red"))

        fig_phase.update_layout(
            title="<b>Espacio Fase Radial</b> <br><i>(Momento conjugado vs Coordenada)</i>", 
            xaxis_title="r", 
            yaxis_title="p_r",
            xaxis_range=[0, 8], yaxis_range=[-4, 4], height=400, margin=dict(l=20, r=20, t=60, b=20)
        )
        st.plotly_chart(fig_phase, use_container_width=True)

    # Animación
    st.markdown("#### 🎥 Dinámica Temporal")
    if st.button("▶️ Iniciar Evolución Temporal"):
        if len(r_valid) > 0:
            prog_bar = st.progress(0)
            
            # Interpolación para animación suave
            steps = 50
            indices = np.linspace(0, len(r_plot)-1, steps, dtype=int)
            
            for i, idx in enumerate(indices):
                # Actualizar marcador sobre la gráfica base
                fig_anim = go.Figure(fig_phase)
                fig_anim.add_trace(go.Scatter(
                    x=[r_plot[idx]], y=[pr_plot[idx]], mode='markers',
                    marker=dict(color='#db2777', size=15, line=dict(color='white', width=2)),
                    name='Estado del Sistema'
                ))
                fig_anim.update_layout(height=400, margin=dict(l=20, r=20, t=60, b=20))
                
                # Usar un contenedor vacío para sobreescribir la gráfica en lugar de crear nuevas abajo
                # Nota: En streamlit simple esto rerenderiza, pero es la forma estándar
                st.session_state['anim_plot'] = fig_anim
                
                # Truco: mostrar la gráfica animada en un placeholder si quisieramos (aquí simplificado)
                col_graph2.plotly_chart(fig_anim, use_container_width=True)
                
                time.sleep(0.03)
                prog_bar.progress((i + 1) / steps)
            
            prog_bar.empty()
            st.success("Periodo completado.")