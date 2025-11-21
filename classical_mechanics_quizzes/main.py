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
    .math-box {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin: 1rem 0;
        overflow-x: auto;
    }
    /* Ajuste para que los radio buttons con LaTeX tengan mejor espaciado */
    .stRadio label {
        font-size: 1.1rem !important;
        padding-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- Funciones de Física ---
def get_veff(r, L, m, alpha):
    # Evitar división por cero
    r = np.maximum(r, 0.01) 
    return (L**2) / (2 * m * r**2) - (alpha / r)

# --- Inicialización de Estado ---
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

# --- Encabezado ---
st.markdown('<div class="main-header">Mecánica Clásica</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Hamiltoniano y Espacio Fase: El Problema de Kepler</div>', unsafe_allow_html=True)

# --- Pestañas ---
tab1, tab2, tab3 = st.tabs(["📖 Teoría", "❓ Quiz", "📈 Simulación"])

# ==========================================
# PESTAÑA 1: TEORÍA
# ==========================================
with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("1. El Hamiltoniano en 3D")
        st.write("Para una partícula de masa $m$ en potencial $U(r) = -\\alpha/r$:")
        st.markdown("""
        <div class="math-box">
        $$H = \\frac{1}{2m} \left( p_r^2 + \\frac{p_\\theta^2}{r^2} + \\frac{p_\phi^2}{r^2\sin^2\\theta} \right) - \\frac{\\alpha}{r}$$
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.subheader("2. Reducción a 1D")
        st.write("Fijando el plano $\\theta = \pi/2$, surge el **Potencial Efectivo**:")
        st.markdown("""
        <div class="math-box">
        $$H_{1D} = \\frac{p_r^2}{2m} + V_{eff}(r) = E$$
        <br>
        $$V_{eff}(r) = \\frac{L^2}{2mr^2} - \\frac{\\alpha}{r}$$
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# PESTAÑA 2: QUIZ (CORREGIDO)
# ==========================================
with tab2:
    st.markdown("### Test de Conceptos")
    st.info("Selecciona la respuesta correcta. Las fórmulas se renderizan automáticamente.")

    # Definimos las preguntas usando raw strings (r"") y signos $ para LaTeX
    questions = [
        {
            "id": "q1",
            "q": "¿Cuál es la expresión correcta del Hamiltoniano en coordenadas esféricas?",
            "opts": [
                r"$H = \frac{p^2}{2m} - \frac{\alpha}{r}$",
                r"$H = \frac{1}{2m} \left( p_r^2 + \frac{p_\theta^2}{r^2} + \frac{p_\phi^2}{r^2\sin^2\theta} \right) - \frac{\alpha}{r}$",
                r"$H = \frac{1}{2m}(p_r^2 + p_\theta^2) + \frac{\alpha}{r}$"
            ],
            "correct": 1, 
            "expl": "En esféricas, la energía cinética incluye términos angulares divididos por $r^2$ y $r^2\sin^2\\theta$."
        },
        {
            "id": "q2",
            "q": "¿Qué se conserva si el potencial es $U(r)$?",
            "opts": [
                r"Solo el momento radial $p_r$",
                r"El vector momento angular $\vec{L}$ y la Energía $E$",
                r"Ninguna cantidad se conserva"
            ],
            "correct": 1,
            "expl": "El potencial central $U(r)$ es invariante bajo rotaciones (conserva $\\vec{L}$) y temporalmente constante (conserva $E$)."
        },
        {
            "id": "q3",
            "q": "¿Cuál es la forma del Potencial Efectivo $V_{eff}(r)$?",
            "opts": [
                r"$V_{eff} = \frac{L^2}{2mr^2} - \frac{\alpha}{r}$",
                r"$V_{eff} = - \frac{\alpha}{r}$",
                r"$V_{eff} = \frac{L^2}{2mr^2} + \frac{\alpha}{r}$"
            ],
            "correct": 0,
            "expl": "Es la suma de la barrera centrífuga (repulsiva, $\\sim 1/r^2$) y el potencial atractivo ($\\sim -1/r$)."
        }
    ]

    with st.form("quiz_form"):
        for i, q in enumerate(questions):
            st.markdown(f"**{i+1}. {q['q']}**")
            prev_val = st.session_state.quiz_answers.get(q['id'], None)
            
            # st.radio renderiza Markdown/LaTeX en las opciones si están entre $
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
                st.success(f"✅ P{i+1}: Correcto. {q['expl']}")
            else:
                st.error(f"❌ P{i+1}: Incorrecto. {q['expl']}")
        
        st.metric("Tu Puntuación", f"{score}/{len(questions)}")

# ==========================================
# PESTAÑA 3: SIMULACIÓN
# ==========================================
with tab3:
    with st.sidebar:
        st.header("🎛️ Controles")
        E_val = st.slider("Energía (E)", -2.0, 2.0, -0.5, 0.1)
        L_val = st.slider("Momento Angular (L)", 0.5, 3.0, 1.2, 0.1)
        m_val = st.slider("Masa (m)", 0.5, 2.0, 1.0, 0.1)
        alpha_val = st.slider("Potencial (α)", 0.5, 3.0, 1.5, 0.1)
        
        st.caption("Nota: Si la gráfica desaparece, la energía es menor al mínimo del potencial efectivo (región prohibida).")

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

    col_graph1, col_graph2 = st.columns(2)

    # Gráfica 1: V_eff
    with col_graph1:
        fig_pot = go.Figure()
        fig_pot.add_trace(go.Scatter(x=r, y=veff, name='V_eff(r)', line=dict(color='#2563eb', width=3)))
        fig_pot.add_hline(y=E_val, line_dash="dash", line_color="#dc2626", annotation_text=f"E = {E_val}")
        
        # Sombreado zona permitida
        if len(r_valid) > 0:
            fig_pot.add_vrect(x0=r_valid[0], x1=r_valid[-1], fillcolor="green", opacity=0.1, line_width=0)

        fig_pot.update_layout(
            title="Potencial Efectivo", xaxis_title="r", yaxis_title="Energía",
            yaxis_range=[-5, 3], height=350, margin=dict(l=20, r=20, t=40, b=20)
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
                x=r_plot, y=pr_plot, mode='lines', name='Trayectoria',
                line=dict(color='#7c3aed', width=3), fill='toself', fillcolor='rgba(124, 58, 237, 0.1)'
            ))
        else:
            fig_phase.add_annotation(text="Región Prohibida", showarrow=False)

        fig_phase.update_layout(
            title="Espacio Fase (r, pr)", xaxis_title="r", yaxis_title="pr",
            xaxis_range=[0, 8], yaxis_range=[-4, 4], height=350, margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_phase, use_container_width=True)

    # Animación
    if st.button("▶️ Simular Movimiento"):
        if len(r_valid) > 0:
            prog_bar = st.progress(0)
            status_text = st.empty()
            plot_spot = st.empty()
            
            # Trayectoria interpolada reducida para animación fluida
            steps = 40
            indices = np.linspace(0, len(r_plot)-1, steps, dtype=int)
            
            for i, idx in enumerate(indices):
                # Actualizar marcador sobre la gráfica base
                fig_anim = go.Figure(fig_phase)
                fig_anim.add_trace(go.Scatter(
                    x=[r_plot[idx]], y=[pr_plot[idx]], mode='markers',
                    marker=dict(color='#db2777', size=12, line=dict(color='white', width=2))
                ))
                fig_anim.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
                
                plot_spot.plotly_chart(fig_anim, use_container_width=True)
                status_text.text(f"Posición r: {r_plot[idx]:.2f}, Momento pr: {pr_plot[idx]:.2f}")
                prog_bar.progress((i + 1) / steps)
                time.sleep(0.05)
            
            status_text.success("Ciclo finalizado.")
            prog_bar.empty()
# Footer
st.markdown("---")
st.markdown("*Desarrollado con Python y Streamlit. Mecánica Clásica Interactiva.*")