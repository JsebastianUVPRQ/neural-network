import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.integrate import solve_ivp
import time

# Configuración de página (Debe ser lo primero)
st.set_page_config(
    page_title="Mecánica Clásica Interactiva",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================
# 1. ESTILOS CSS AVANZADOS (GLASSMORPHISM)
# =============================================
st.markdown("""
<style>
    /* Importar fuente moderna */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }

    /* FONDO DE LA APP (Deep Space Gradient) */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        background-attachment: fixed;
    }

    /* CLASE PRINCIPAL: TARJETA DE VIDRIO */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: #E0E0E0;
    }

    /* Estilo de los Botones */
    div.stButton > button {
        background: linear-gradient(90deg, rgba(0, 173, 181, 0.1) 0%, rgba(0, 173, 181, 0.2) 100%);
        border: 1px solid #00ADB5;
        border-radius: 10px;
        color: #00ADB5;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #00ADB5;
        color: white;
        box-shadow: 0 0 15px rgba(0, 173, 181, 0.5);
        transform: translateY(-2px);
    }

    /* Personalización de Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255,255,255,0.05);
        border-radius: 10px 10px 0 0;
        color: white;
        border: none;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: rgba(0, 173, 181, 0.2);
        color: #00ADB5;
        border-bottom: 2px solid #00ADB5;
    }

    /* Sliders y Radio Buttons */
    div[data-baseweb="select"] > div {
        background-color: rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.2);
        color: white;
    }

    /* Títulos y Texto */
    h1, h2, h3 {
        color: #F4F4F8;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    h4 {
        color: #00ADB5 !important;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        padding-bottom: 10px;
        margin-top: 20px;
    }
    
    /* LaTeX tamaño */
    .katex { font-size: 1.1em !important; }
    
    /* Cajas de Quiz personalizadas */
    .option-box {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 8px;
        padding: 15px;
        margin: 5px 0;
        text-align: center;
    }
    .success-box {
        background: rgba(0, 255, 127, 0.1);
        border: 1px solid #00FF7F;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        color: #00FF7F;
    }

</style>
""", unsafe_allow_html=True)

# Función auxiliar para estilizar gráficas oscuras
def style_dark_plot(fig, ax):
    fig.patch.set_alpha(0.0) # Fondo transparente figura
    ax.set_facecolor((0, 0, 0, 0)) # Fondo transparente ejes
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('white')
    legend = ax.legend(facecolor='#1e2130', edgecolor='white')
    plt.setp(legend.get_texts(), color='white')
    return fig

# =============================================
# ESTRUCTURA PRINCIPAL
# =============================================

col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("https://img.icons8.com/fluency/96/ffffff/solar-system.png", width=80)
with col_title:
    st.title("Mecánica Clásica: Órbitas y Potenciales")
    st.markdown("*Una exploración interactiva del formalismo Hamiltoniano*")

# Crear pestañas
tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Teoría Avanzada", 
    "🧪 Laboratorio Orbital", 
    "📊 Espacio de Fases", 
    "📝 Quiz Interactivo"
])

# =============================================
# PESTAÑA 1: TEORÍA AVANZADA
# =============================================
with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Hamiltoniano en Coordenadas Esféricas")
    st.markdown(r"""
    Consideremos una partícula de masa $m$ bajo un **potencial central** $U(r) = -\dfrac{\alpha}{r}$.
    
    ### 1. Transformación al Hamiltoniano
    
    Partiendo del Lagrangiano en esféricas y aplicando la transformación de Legendre $H = \sum p_i \dot{q}^i - L$, llegamos a la expresión fundamental de la energía total del sistema.
    
    El **Hamiltoniano** resultante es:

    $$ \boxed{H = \underbrace{\dfrac{p_r^2}{2m}}_{\text{Radial}} + \underbrace{\dfrac{p_\theta^2}{2mr^2}}_{\text{Angular }\theta} + \underbrace{\dfrac{p_\phi^2}{2mr^2\sin^2\theta}}_{\text{Angular }\phi} - \underbrace{\dfrac{\alpha}{r}}_{\text{Potencial}}} $$

    Donde los momentos conjugados determinan la dinámica en el espacio de fases $(q, p)$.
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col_t1, col_t2 = st.columns(2)
    
    with col_t1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Ecuaciones de Movimiento")
        st.markdown(r"""
        Las ecuaciones canónicas de Hamilton $\dot{q} = \frac{\partial H}{\partial p}$ y $\dot{p} = -\frac{\partial H}{\partial q}$ nos dan:
        
        $$ \dot{r} = \dfrac{p_r}{m} $$
        $$ \dot{p}_r = \dfrac{p_\theta^2}{mr^3} + \dfrac{p_\phi^2}{mr^3\sin^2\theta} - \dfrac{\alpha}{r^2} $$
        
        Note como la fuerza centrífuga emerge naturalmente en $\dot{p}_r$.
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_t2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Conservación")
        st.markdown(r"""
        Dado que $\phi$ es una coordenada cíclica (no aparece explícitamente en $H$):
        
        $$ \dot{p}_\phi = -\dfrac{\partial H}{\partial \phi} = 0 \implies p_\phi = \text{cte} $$
        
        Esto corresponde a la conservación del componente $z$ del **momento angular**.
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================
# PESTAÑA 2: TESTS INTERACTIVOS
# =============================================
with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🧪 Simulador de Conceptos")
    st.markdown("Verifica tu intuición física antes de pasar a los cálculos numéricos.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col_q1, col_q2 = st.columns(2)
    
    # Pregunta 1
    with col_q1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("1. Momento Angular")
        st.markdown("¿Qué cantidad se conserva estrictamente en un potencial central $U(r)$?")
        opcion1 = st.radio("Tu respuesta:", 
                          ["Energía cinética", "Momento lineal", "Momento angular", "Ninguna"], key="radio_q1")
        
        if st.button("Verificar Q1"):
            if opcion1 == "Momento angular":
                st.success("✅ ¡Correcto! La isotropía del espacio implica conservación de L.")
            else:
                st.error("❌ Incorrecto. Piensa en las simetrías rotacionales.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Pregunta 2
    with col_q2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("2. Geometría Orbital")
        st.markdown("Si la energía total $E < 0$ (y $E > U_{min}$), la trayectoria es:")
        
        # Mini gráfica ilustrativa
        fig_mini, ax_mini = plt.subplots(figsize=(4, 2))
        x = np.linspace(-2, 2, 100)
        ax_mini.plot(x, x**2, color='#00ADB5', alpha=0.8)
        ax_mini.set_yticks([])
        ax_mini.set_xticks([])
        ax_mini.text(0, 1, "Potencial", color="white", ha="center")
        style_dark_plot(fig_mini, ax_mini)
        st.pyplot(fig_mini)

        opcion2 = st.selectbox("Selecciona tipo:", ["Hiperbólica", "Parabólica", "Elíptica/Circular", "Caótica"], key="sel_q2")
        
        if st.button("Verificar Q2"):
            if opcion2 == "Elíptica/Circular":
                st.success("✅ ¡Exacto! Los estados ligados ocurren con energía negativa.")
            else:
                st.error("❌ Incorrecto. Revisa el diagrama de energía efectiva.")
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================
# PESTAÑA 3: ESPACIO DE FASES
# =============================================
with tab3:
    st.header("📊 Laboratorio de Espacio de Fases")
    
    # Controles en una fila superior dentro de una tarjeta
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        alpha = st.slider("Constante α", 0.1, 5.0, 1.0, 0.1)
    with c2:
        masa = st.slider("Masa m", 0.1, 5.0, 1.0, 0.1)
    with c3:
        L_val = st.slider("Momento L", 0.5, 3.0, 1.0, 0.1)
    with c4:
        energia = st.slider("Energía E", -1.5, 2.0, -0.5, 0.1)
    st.markdown('</div>', unsafe_allow_html=True)

    # Gráficas Principales
    col_plot1, col_plot2 = st.columns([1, 1])
    
    r = np.linspace(0.15, 8, 1000)
    U = -alpha/r
    U_centrifuga = L_val**2/(2*masa*r**2)
    U_eff = U + U_centrifuga
    
    with col_plot1:
        st.markdown("### Potencial Efectivo")
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        ax1.plot(r, U_eff, color='#00ADB5', linewidth=2.5, label='$U_{eff}(r)$')
        ax1.plot(r, U, color='#F39C12', linestyle=':', alpha=0.6, label='Atractivo')
        ax1.plot(r, U_centrifuga, color='#E74C3C', linestyle=':', alpha=0.6, label='Centrífugo')
        ax1.axhline(y=energia, color='white', linestyle='--', alpha=0.8, label=f'E = {energia}')
        
        # Relleno de zona prohibida
        ylim = ax1.get_ylim()
        ax1.fill_between(r, ylim[0], ylim[1], where=(U_eff > energia), color='gray', alpha=0.2)
        
        ax1.set_ylim(-2, 3)
        ax1.set_xlim(0, 6)
        ax1.set_xlabel('Radio r')
        ax1.set_ylabel('Energía')
        style_dark_plot(fig1, ax1)
        st.pyplot(fig1)

    with col_plot2:
        st.markdown("### Espacio de Fases $(r, p_r)$")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        
        # Calcular momento radial: pr = +/- sqrt(2m(E - Ueff))
        valid_mask = energia >= U_eff
        r_valid = r[valid_mask]
        
        if len(r_valid) > 1:
            pr = np.sqrt(2*masa*(energia - U_eff[valid_mask]))
            ax2.plot(r_valid, pr, color='#D35400', linewidth=2)
            ax2.plot(r_valid, -pr, color='#D35400', linewidth=2)
            # Cerrar la curva si es elíptica
            if energia < 0:
                ax2.plot([r_valid[0], r_valid[0]], [-pr[0], pr[0]], color='#D35400', linewidth=2)
                ax2.plot([r_valid[-1], r_valid[-1]], [-pr[-1], pr[-1]], color='#D35400', linewidth=2)
                
        ax2.set_xlabel('Posición r')
        ax2.set_ylabel('Momento Radial $p_r$')
        ax2.set_xlim(0, 6)
        ax2.set_ylim(-3, 3)
        ax2.grid(True, linestyle='--', alpha=0.2)
        style_dark_plot(fig2, ax2)
        st.pyplot(fig2)

    st.markdown("---")
    
    # Simulación de Órbita 2D
    st.subheader("🪐 Simulación Orbital en Tiempo Real")
    
    col_sim_ctrl, col_sim_plot = st.columns([1, 2])
    
    with col_sim_ctrl:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        r0 = st.number_input("Radio Inicial", 1.0, 5.0, 2.0)
        btn_simular = st.button("🚀 Lanzar Simulación")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_sim_plot:
        if btn_simular:
            # Calcular velocidad inicial basada en energía
            U_eff_r0 = -alpha/r0 + L_val**2/(2*masa*r0**2)
            if energia < U_eff_r0:
                st.error("Error: Energía insuficiente para este radio inicial.")
            else:
                pr0 = np.sqrt(2*masa*(energia - U_eff_r0))
                
                def derivadas(t, y):
                    r_t, theta_t, pr_t, ptheta_t = y
                    dr = pr_t/masa
                    dtheta = ptheta_t/(masa*r_t**2)
                    dpr = ptheta_t**2/(masa*r_t**3) - alpha/r_t**2
                    return [dr, dtheta, dpr, 0]

                t_eval = np.linspace(0, 30, 600)
                sol = solve_ivp(derivadas, [0, 30], [r0, 0, pr0, L_val], t_eval=t_eval)
                
                # Plot
                x_orb = sol.y[0] * np.cos(sol.y[1])
                y_orb = sol.y[0] * np.sin(sol.y[1])
                
                fig3, ax3 = plt.subplots(figsize=(6, 6))
                ax3.plot(0, 0, 'o', color='yellow', markersize=15, label='Centro') # Sol
                ax3.plot(x_orb, y_orb, color='#00ADB5', linewidth=1.5)
                ax3.plot(x_orb[-1], y_orb[-1], 'o', color='white', markersize=6) # Particula
                
                max_range = max(np.max(np.abs(x_orb)), np.max(np.abs(y_orb))) * 1.2
                ax3.set_xlim(-max_range, max_range)
                ax3.set_ylim(-max_range, max_range)
                ax3.set_aspect('equal')
                style_dark_plot(fig3, ax3)
                st.pyplot(fig3)

# =============================================
# PESTAÑA 4: QUIZ (Estilo Tarjetas)
# =============================================
with tab4:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📝 Desafío Matemático")
    st.markdown("Construye el Hamiltoniano correcto seleccionando los términos.")
    st.markdown('</div>', unsafe_allow_html=True)

    col_h1, col_h2, col_h3 = st.columns(3)
    
    with col_h1:
        st.markdown("**Término Cinético Radial**")
        st.latex(r"\frac{p_r^2}{2m}")
        st.info("Fijo")

    with col_h2:
        st.markdown("**Término Angular**")
        sel_ang = st.radio("Elige:", 
                 [r"A) p_\theta / r", r"B) p_\theta^2 / (2mr^2)", r"C) p_\theta^2 / r"], 
                 index=1, key="quiz_ang")
        
    with col_h3:
        st.markdown("**Potencial**")
        sel_pot = st.radio("Elige:", 
                 [r"A) +\alpha/r", r"B) -\alpha r", r"C) -\alpha/r"], 
                 index=2, key="quiz_pot")

    st.markdown("---")
    
    if st.button("Verificar Ecuación Final"):
        correct_ang = "B" in sel_ang
        correct_pot = "C" in sel_pot
        
        if correct_ang and correct_pot:
            st.markdown("""
            <div class="success-box">
                <h3>🎉 ¡Excelente!</h3>
                <p>Has derivado correctamente el Hamiltoniano clásico.</p>
            </div>
            """, unsafe_allow_html=True)
            st.latex(r"H = \frac{p_r^2}{2m} + \frac{p_\theta^2}{2mr^2} + \frac{p_\phi^2}{2mr^2\sin^2\theta} - \frac{\alpha}{r}")
            st.balloons()
        else:
            st.warning("⚠️ Hay un error. Recuerda: La energía cinética depende del cuadrado del momento y el potencial gravitatorio es inversamente proporcional a la distancia y negativo.")

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: rgba(255,255,255,0.5);'>Desarrollado con Streamlit • Mecánica Clásica</p>", unsafe_allow_html=True)

