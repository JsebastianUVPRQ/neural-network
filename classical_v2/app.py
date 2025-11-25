import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.integrate import solve_ivp
import time


# Título principal
st.title("🔭 Mecánica Clásica")
st.markdown("---")

st.markdown("""
<style>

/* ================================
      FUENTE GLOBAL: INTER
==================================*/
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif !important;
    color: #E8ECF2 !important;
}


/* ================================
             TITULOS
==================================*/
h1, h2, h3, h4 {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    color: #9BCBFF !important;
}


/* ================================
        TARJETAS / CONTENEDORES
==================================*/
div.stMarkdown div {
    background-color: #161925 !important;
    border: 1px solid #1F2330 !important;
    border-radius: 12px !important;
    padding: 1.1rem 1.3rem !important;
    box-shadow: 0 0 8px rgba(0,0,0,0.25) !important;
    margin-bottom: 1.2rem !important;
}


/* ================================
            SIDEBAR
==================================*/
section[data-testid="stSidebar"] {
    background-color: #11131C !important;
    border-right: 1px solid #1A1C25 !important;
}

section[data-testid="stSidebar"] * {
    font-family: 'Inter', sans-serif !important;
}


/* ================================
            BOTONES
==================================*/
.stButton>button {
    background-color: #6EB5FF !important;
    color: #0F111A !important;
    padding: 0.6rem 1.2rem !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 8px !important;
    font-size: 16px !important;
}

.stButton>button:hover {
    background-color: #98CCFF !important;
}


/* ================================
              INPUTS
==================================*/
.stTextInput>div>div>input,
.stNumberInput input,
.stDateInput input {
    background-color: #1A1D29 !important;
    color: #E8ECF2 !important;
    border: 1px solid #2C3142 !important;
    border-radius: 8px !important;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #1A1D29 !important;
    color: #E8ECF2 !important;
    border-radius: 8px !important;
    border: 1px solid #2C3142 !important;
}


/* ================================
        SLIDERS / RANGE INPUTS
==================================*/
[data-baseweb="slider"] {
    color: #E8ECF2 !important;
}

.stSlider > div > div > div {
    background-color: #6EB5FF !important;
}

.stSlider > div > div > div[role="slider"] {
    background-color: #98CCFF !important;
    border-radius: 50% !important;
}


/* ================================
                LATEX
==================================*/
.katex-html {
    font-size: 20px !important;
    color: #E8ECF2 !important;
}


/* ================================
           TABLAS / DATAFRAMES
==================================*/
.dataframe thead th {
    background-color: #1F2330 !important;
    color: #E8ECF2 !important;
}

.dataframe tbody td {
    background-color: #161925 !important;
    color: #D6DBE4 !important;
}


/* ================================
            EXPANDERS
==================================*/
.streamlit-expanderHeader {
    background-color: #161925 !important;
    color: #E8ECF2 !important;
    border-radius: 8px !important;
}

</style>
""", unsafe_allow_html=True)




# Crear pestañas
tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Teoría", 
    "🧪 Tests Órbitas", 
    "📊 Espacio de Fases", 
    "🔄 Quiz"
])

# =============================================
# PESTAÑA 1: TEORÍA AVANZADA
# =============================================
with tab1:
    st.header("Hamiltoniano en Coordenadas Esféricas para Potencial Central")
    
    st.markdown(r"""
    ## Sistema con Potencial $U(r) = -\dfrac{\alpha}{r}$

    Consideremos una partícula de masa $m$ moviéndose bajo la influencia de un potencial central:

    $$ U(r) = -\dfrac{\alpha}{r} $$

    donde $\alpha > 0$ es una constante (por ejemplo, $\alpha = GmM$ en el caso gravitatorio).

    ### 1. Coordenadas Esféricas

    En coordenadas esféricas $(r, \theta, \phi)$, el elemento de línea es:

    $$ ds^2 = dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2 $$

    ### 2. Lagrangiano

    El lagrangiano en coordenadas esféricas es:

    $$ L = T - U = \dfrac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2 + r^2\sin^2\theta\dot{\phi}^2) + \dfrac{\alpha}{r} $$

    ### 3. Momentos Conjugados

    Los momentos conjugados se definen como $p_i = \dfrac{\partial L}{\partial \dot{q}^i}$:

    $$ p_r = \dfrac{\partial L}{\partial \dot{r}} = m\dot{r} $$
    $$ p_\theta = \dfrac{\partial L}{\partial \dot{\theta}} = mr^2\dot{\theta} $$
    $$ p_\phi = \dfrac{\partial L}{\partial \dot{\phi}} = mr^2\sin^2\theta\dot{\phi} $$
    ### 4. Transformación Legendre y Hamiltoniano

    El hamiltoniano se obtiene mediante la transformación de Legendre:

    $$ H = \sum_i p_i\dot{q}^i - L $$

    Sustituyendo:

    $$ H = p_r\dot{r} + p_\theta\dot{\theta} + p_\phi\dot{\phi} - L $$

    Expresando las velocidades en términos de los momentos:

    $$ \dot{r} = \dfrac{p_r}{m}, \quad \dot{\theta} = \dfrac{p_\theta}{mr^2}, \quad \dot{\phi} = \dfrac{p_\phi}{mr^2\sin^2\theta} $$
    Sustituyendo en la expresión del hamiltoniano:

    $$ H = \dfrac{p_r^2}{m} + \dfrac{p_\theta^2}{mr^2} + \dfrac{p_\phi^2}{mr^2\sin^2\theta} - \left[ \dfrac{1}{2}m\left(\dfrac{p_r^2}{m^2} + r^2\dfrac{p_\theta^2}{m^2r^4} + r^2\sin^2\theta\dfrac{p_\phi^2}{m^2r^4\sin^4\theta}\right) + \dfrac{\alpha}{r} \right] $$

    Simplificando:

    $$ H = \dfrac{p_r^2}{m} + \dfrac{p_\theta^2}{mr^2} + \dfrac{p_\phi^2}{mr^2\sin^2\theta} - \dfrac{1}{2}\left(\dfrac{p_r^2}{m} + \dfrac{p_\theta^2}{mr^2} + \dfrac{p_\phi^2}{mr^2\sin^2\theta}\right) - \dfrac{\alpha}{r} $$
    Finalmente, obtenemos el **hamiltoniano en coordenadas esféricas**:

    $$ \boxed{H = \dfrac{p_r^2}{2m} + \dfrac{p_\theta^2}{2mr^2} + \dfrac{p_\phi^2}{2mr^2\sin^2\theta} - \dfrac{\alpha}{r}} $$

    ### 5. Interpretación Física

    - El primer término representa la energía cinética radial
    - El segundo término representa la energía cinética asociada al movimiento en $\theta$
    - El tercer término representa la energía cinética asociada al movimiento en $\phi$
    - El último término es la energía potencial

    ### 6. Ecuaciones de Hamilton

    Las ecuaciones de Hamilton son:

    $$ \dot{r} = \dfrac{\partial H}{\partial p_r} = \dfrac{p_r}{m}\newline \newline$$
    $$ ~~~~~\newline$$
    $$ \dot{\theta} = \dfrac{\partial H}{\partial p_\theta} = \dfrac{p_\theta}{mr^2}\newline$$
    $$ ~~~~~\newline$$
    $$ \dot{\phi} = \dfrac{\partial H}{\partial p_\phi} = \dfrac{p_\phi}{mr^2\sin^2\theta}\newline $$
    $$ ~~~~~\newline$$
    $$ \dot{p}_r = -\dfrac{\partial H}{\partial r} = \dfrac{p_\theta^2}{mr^3} + \dfrac{p_\phi^2}{mr^3\sin^2\theta} - \dfrac{\alpha}{r^2}\newline $$
    $$ ~~~~~\newline$$
    $$ \dot{p}_\theta = -\dfrac{\partial H}{\partial \theta} = \dfrac{p_\phi^2\cos\theta}{mr^2\sin^3\theta}\newline $$
    $$ ~~~~~\newline$$
    $$ \dot{p}_\phi = -\dfrac{\partial H}{\partial \phi} = 0 $$


    Note que $p_\phi$ es constante, lo que refleja la conservación del momento angular en la dirección z.
    """)

# =============================================
# PESTAÑA 2: TESTS INTERACTIVOS
# =============================================
with tab2:
    st.header("🧪 Tests Interactivos de Mecánica Clásica")
    
    # Pregunta 1
    st.subheader("Pregunta 1: Momento Angular")
    st.markdown("¿Cuál de las siguientes cantidades se conserva en un potencial central $U(r) = -\\alpha/r$?")
    
    col1, col2 = st.columns(2)
    with col1:
        opcion1 = st.radio("Selecciona una opción:", 
                          ["Energía cinética solamente", 
                           "Momento lineal", 
                           "Momento angular", 
                           "Ninguna cantidad se conserva"])
    
    with col2:
        if st.button("Verificar Respuesta 1"):
            if opcion1 == "Momento angular":
                st.success("✅ Correcto! En un potencial central, el momento angular se conserva.")
                st.balloons()
            else:
                st.error("❌ Incorrecto. Revisa la teoría sobre potenciales centrales.")
    
    # Pregunta 2 con animación
    st.subheader("Pregunta 2: Trayectorias Orbitales")
    st.markdown("Para un potencial $U(r) = -\\alpha/r$, ¿qué tipo de trayectorias son posibles?")
    
    # Parámetros para la animación
    energy = st.slider("Energía total", -2.0, 2.0, 0.0, 0.1, key="energy_slider")
    angular_momentum = st.slider("Momento angular", 0.1, 2.0, 1.0, 0.1, key="ang_mom_slider")
    
    # Cálculo de parámetros orbitales
    def orbital_type(E, L):
        if E < 0:
            return "Elíptica"
        elif E == 0:
            return "Parabólica"
        else:
            return "Hiperbólica"
    
    tipo_orbita = orbital_type(energy, angular_momentum)
    
    # Gráfica simple de potencial efectivo
    fig, ax = plt.subplots(figsize=(10, 6))
    r = np.linspace(0.1, 10, 1000)
    U_eff = -1/r + angular_momentum**2/(2*r**2)  # Potencial efectivo
    
    ax.plot(r, U_eff, 'b-', linewidth=2, label='Potencial efectivo')
    ax.axhline(y=energy, color='r', linestyle='--', label=f'Energía = {energy}')
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 2)
    ax.set_xlabel('r')
    ax.set_ylabel('Energía')
    ax.set_title(f'Potencial Efectivo - Órbita {tipo_orbita}')
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)
    
    opcion2 = st.selectbox("Selecciona el tipo de órbita:",
                          ["Solo órbitas circulares", 
                           "Solo órbitas elípticas", 
                           "Órbitas elípticas, parabólicas e hiperbólicas",
                           "Solo órbitas rectilíneas"])
    
    if st.button("Verificar Respuesta 2"):
        if opcion2 == "Órbitas elípticas, parabólicas e hiperbólicas":
            st.success("✅ Correcto! Dependiendo de la energía, pueden darse los tres tipos de órbitas.")
        else:
            st.error("❌ Incorrecto. Revisa la teoría de órbitas en potenciales centrales.")

# =============================================
# PESTAÑA 3: ESPACIO DE FASES
# =============================================
with tab3:
    st.header("📊 Espacio de Fases y Potencial Efectivo")
    st.markdown("Explora el espacio de fases para una partícula en un potencial central $U(r) = -\\alpha/r$ con momento angular $L$. Ajusta los parámetros para ver cómo cambian las órbitas y el espacio de fases.")
    
    st.subheader("Parámetros del Sistema")
    
    alpha = st.slider("Constante α", 0.1, 5.0, 1.0, 0.1)
    masa = st.slider("Masa m", 0.1, 5.0, 1.0, 0.1)
    L = st.slider("Momento angular L", 0.1, 3.0, 1.0, 0.1)
    energia = st.slider("Energía E", -1.0, 2.0, -0.2, 0.1)
    
    st.markdown("### Potencial Efectivo")
    st.latex(r"U_{\text{eff}}(r) = -\frac{\alpha}{r} + \frac{L^2}{2mr^2}")


    # Gráfica del potencial efectivo
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    r = np.linspace(0.1, 10, 1000)
    U = -alpha/r
    U_centrifuga = L**2/(2*masa*r**2)
    U_eff = U + U_centrifuga
    
    # Potencial efectivo
    ax1.plot(r, U, 'r--', alpha=0.7, label=r'$-\alpha/r$')
    ax1.plot(r, U_centrifuga, 'g--', alpha=0.7, label=r'$L^2/(2mr^2)$')
    ax1.plot(r, U_eff, 'b-', linewidth=2, label='Potencial efectivo')
    ax1.axhline(y=energia, color='k', linestyle='--', label=f'E = {energia}')
    ax1.set_xlabel('r')
    ax1.set_ylabel('Energía Potencial')
    ax1.set_title('Potencial Efectivo')
    ax1.legend()
    ax1.grid(True)
    ax1.set_ylim(-10, 15)
    ax1.set_xlim(0, 1.5)
    
    # Espacio de fases (r vs p_r)
    # Para una energía dada E, p_r = ±√[2m(E - U_eff(r))]
    r_min = 0.3
    r_vals = np.linspace(r_min, 25, 500)
    U_eff_vals = -alpha/r_vals + L**2/(2*masa*r_vals**2)
    
    # Solo graficar donde E >= U_eff
    valid_indices = energia >= U_eff_vals
    r_valid = r_vals[valid_indices]
    
    if len(r_valid) > 0:
        p_r_pos = np.sqrt(2*masa*(energia - (-alpha/r_valid + L**2/(2*masa*r_valid**2))))
        p_r_neg = -p_r_pos
        
        ax2.plot(r_valid, p_r_pos, 'b-', linewidth=2, label='Espacio de fases')
        ax2.plot(r_valid, p_r_neg, 'b-', linewidth=2)
        ax2.set_xlabel('$r$')
        ax2.set_ylabel('$p_r$')
        ax2.set_xlim(p_r_pos.min()-1, r_valid.max()+1)
        ax2.set_title('Espacio de Fases $(r, p_r)$')
        ax2.grid(True)
        ax2.legend()
    
    st.pyplot(fig1)
    st.markdown("---")
    # Gráfica de órbitas
    st.subheader("Simulación de Órbitas")
    
    def derivadas_orbita(t, y, m, alpha):
        r, theta, pr, ptheta = y
        drdt = pr/m
        dthetadt = ptheta/(m*r**2)
        dprdt = ptheta**2/(m*r**3) - alpha/r**2
        dpthetadt = 0
        return [drdt, dthetadt, dprdt, dpthetadt]
    
    # Condiciones iniciales
    r0 = st.slider("Radio inicial r₀", 0.5, 5.0, 2.0, 0.1)
    theta0 = st.slider("Ángulo inicial θ₀", 0.0, 2*np.pi, 0.0, 0.1)
    
    # Calcular pr0 para la energía seleccionada
    U_eff0 = -alpha/r0 + L**2/(2*masa*r0**2)
    pr0 = np.sqrt(2*masa*(energia - U_eff0))
    
    if st.button("Simular Órbita"):
        # Resolver ecuaciones diferenciales
        t_span = (0, 20)
        t_eval = np.linspace(0, 20, 1000)
        sol = solve_ivp(derivadas_orbita, t_span, [r0, theta0, pr0, L], 
                       args=(masa, alpha), t_eval=t_eval, method='RK45')
        
        # Convertir a coordenadas cartesianas
        x = sol.y[0] * np.cos(sol.y[1])
        y = sol.y[0] * np.sin(sol.y[1])
        
        # Animación simple (mostrar progresivamente)
        fig3, ax3 = plt.subplots(figsize=(8, 8))
        
        placeholder = st.empty()
        
        for i in range(50, len(x), 10):
            ax3.clear()
            ax3.plot(x[:i], y[:i], 'b-', alpha=0.7)
            ax3.plot(x[i-1], y[i-1], 'ro', markersize=8)
            ax3.plot(0, 0, 'yo', markersize=10)  # Centro de fuerza
            
            ax3.set_xlim(-max(np.max(np.abs(x)), 5), max(np.max(np.abs(x)), 5))
            ax3.set_ylim(-max(np.max(np.abs(y)), 5), max(np.max(np.abs(y)), 5))
            ax3.set_xlabel('x')
            ax3.set_ylabel('y')
            ax3.set_title('Órbita en el Espacio de Configuración')
            ax3.grid(True)
            ax3.set_aspect('equal')
            
            placeholder.pyplot(fig3)
            time.sleep(0.1)

# =============================================
# PESTAÑA 4: EJERCICIOS MATEMÁTICOS
# =============================================
with tab4:
    st.markdown('<h2 class="section-header">Ejercicios</h2>', unsafe_allow_html=True)
    

    # Ejercicio 1: Cálculo del potencial efectivo
    st.markdown("""
    <div class="exercise-box">
    <h3>📝 Ejercicio 1: Potencial Efectivo</h3>
    </div>
    """, unsafe_allow_html=True)
    st.latex(r"\text{Dado el potencial } U(r) = -\frac{\alpha}{r} \text{ y el momento angular } \vec{L}, ")
    st.latex(r"\text{determina la expresión del potencial efectivo } U_{\text{eff}}(r).")
    

    # Mostrar las opciones con LaTeX renderizado
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción A:**")
        st.latex(r"U_{\text{eff}}(r) = -\frac{\alpha}{r}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción B:**")
        st.latex(r"U_{\text{eff}}(r) = -\frac{\alpha}{r} + \frac{L}{r}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción C:**")
        st.latex(r"U_{\text{eff}}(r) = -\frac{\alpha}{r} + \frac{L^2}{2mr^2}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción D:**")
        st.latex(r"U_{\text{eff}}(r) = -\frac{\alpha}{r} - \frac{L^2}{2mr^2}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Selección con letras
    opcion_potencial = st.radio(
        "Selecciona la opción correcta:",
        ["A", "B", "C", "D"],
        key="potencial_eff"
    )
    
    if st.button("✅ Verificar Potencial Efectivo", key="btn_potencial"):
        if opcion_potencial == "C":
            st.markdown("""
            <div class="success-box">
            <h4>✅ Correcto!</h4>
            <p>Esta es la expresión correcta del potencial efectivo, que incluye el término centrífugo.</p>
            </div>
            """, unsafe_allow_html=True)
            st.latex(r"U_{\text{eff}}(r) = -\frac{\alpha}{r} + \frac{L^2}{2mr^2}")
        else:
            st.error("❌ Incorrecto. Recuerda que el potencial efectivo incluye el término centrífugo.")
    
    # Ejercicio 2: Hamiltoniano interactivo
    st.markdown("""
    <div class="exercise-box">
    <h3>📝 Ejercicio 2: Hamiltoniano en Coordenadas Esféricas</h3>
    <p>Completa la expresión del hamiltoniano para un potencial central.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"H = \frac{p_r^2}{2m} + \text{???} + \text{???} + \text{???}")
    
    st.markdown("**Para cada término, selecciona la opción correcta.**")
    
    # Término en θ
    st.markdown("#### Término en θ:")
    col_theta1, col_theta2, col_theta3 = st.columns(3)
    
    with col_theta1:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción A:**")
        st.latex(r"\frac{p_\theta}{mr}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_theta2:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción B:**")
        st.latex(r"\frac{p_\theta^2}{2mr^2}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_theta3:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción C:**")
        st.latex(r"\frac{p_\theta}{2mr^2}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    term1 = st.radio(
        "Selecciona el término correcto para θ:",
        ["A", "B", "C"],
        key="theta_term"
    )
    
    # Término en φ
    st.markdown("#### Término en φ:")
    col_phi1, col_phi2, col_phi3 = st.columns(3)
    
    with col_phi1:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción A:**")
        st.latex(r"\frac{p_\phi^2}{2mr^2\sin\theta}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_phi2:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción B:**")
        st.latex(r"\frac{p_\phi}{2mr^2\sin^2\theta}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_phi3:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción C:**")
        st.latex(r"\frac{p_\phi^2}{2mr^2\sin^2\theta}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    term2 = st.radio(
        "Selecciona el término correcto para φ:",
        ["A", "B", "C"],
        key="phi_term"
    )
    
    # Término potencial
    st.markdown("#### Término potencial:")
    col_pot1, col_pot2, col_pot3 = st.columns(3)
    
    with col_pot1:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción A:**")
        st.latex(r"-\frac{\alpha}{r}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_pot2:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción B:**")
        st.latex(r"\frac{\alpha}{r}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_pot3:
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        st.markdown("**Opción C:**")
        st.latex(r"-\alpha r")
        st.markdown('</div>', unsafe_allow_html=True)
    
    term3 = st.radio(
        "Selecciona el término correcto para el potencial:",
        ["A", "B", "C"],
        key="pot_term"
        
    )
    
    # Mostrar el hamiltoniano completo seleccionado
    st.markdown("#### Hamiltoniano seleccionado:")
    
    # Mapear las selecciones a expresiones LaTeX
    term1_dict = {"A": r"\frac{p_\theta}{mr}", "B": r"\frac{p_\theta^2}{2mr^2}", "C": r"\frac{p_\theta}{2mr^2}"}
    term2_dict = {"A": r"\frac{p_\phi^2}{2mr^2\sin\theta}", "B": r"\frac{p_\phi}{2mr^2\sin^2\theta}", "C": r"\frac{p_\phi^2}{2mr^2\sin^2\theta}"}
    term3_dict = {"A": r"-\frac{\alpha}{r}", "B": r"+\frac{\alpha}{r}", "C": r"-\alpha r"}
    
    hamiltoniano_completo = f"H = \\frac{{p_r^2}}{{2m}} + {term1_dict[term1]} + {term2_dict[term2]} + {term3_dict[term3]}"
    st.latex(hamiltoniano_completo)
    
    if st.button("✅ Verificar Hamiltoniano", key="btn_hamiltoniano"):
        # Verificar si todas las selecciones son correctas
        if term1 == "B" and term2 == "C" and term3 == "A":
            st.markdown("""
            <div class="success-box">
            <h4>✅ Hamiltoniano Correcto!</h4>
            <p>Has construido correctamente el hamiltoniano en coordenadas esféricas.</p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
            st.latex(r"H = \frac{p_r^2}{2m} + \frac{p_\theta^2}{2mr^2} + \frac{p_\phi^2}{2mr^2\sin^2\theta} - \frac{\alpha}{r}")
        else:
            st.error("❌ Revisa los términos del hamiltoniano.")
            st.info("Recuerda la forma correcta:")
            st.latex(r"H = \frac{p_r^2}{2m} + \frac{p_\theta^2}{2mr^2} + \frac{p_\phi^2}{2mr^2\sin^2\theta} + - \frac{\alpha}{r}")


# Pie de página
st.markdown("---")
st.markdown("### 📚 Recursos Adicionales")
st.markdown("""
- Goldstein, H., Poole, C., & Safko, J. (2001). Classical Mechanics
- Landau, L. D., & Lifshitz, E. M. (1976). Mechanics  
- Marion, J. B., & Thornton, S. T. (1995). Classical Dynamics of Particles and Systems
""")

