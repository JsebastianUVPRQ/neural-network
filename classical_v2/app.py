import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import sympy as sp
from scipy.integrate import solve_ivp
import time

# Configuración de la página
st.set_page_config(
    page_title="Mecánica Clásica Avanzada",
    page_icon="🔭",
    layout="wide"
)

# Título principal
st.title("🔭 Mecánica Clásica Avanzada")
st.markdown("---")

# Crear pestañas
tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Teoría Avanzada", 
    "🧪 Tests Interactivos", 
    "📊 Espacio de Fases", 
    "🔄 Ejercicios Matemáticos"
])

# =============================================
# PESTAÑA 1: TEORÍA AVANZADA
# =============================================
with tab1:
    st.header("Hamiltoniano en Coordenadas Esféricas para Potencial Central")
    
    st.markdown(r"""
    ## Sistema con Potencial $U(r) = -\dfrac{\alpha}{r}$

    Consideremos una partícula de masa $m$ moviéndose bajo la influencia de un potencial central:

    $$ U(r) = -\frac{\alpha}{r} $$

    donde $\alpha > 0$ es una constante (por ejemplo, $\alpha = GmM$ en el caso gravitatorio).

    ### 1. Coordenadas Esféricas

    En coordenadas esféricas $(r, \theta, \phi)$, el elemento de línea es:

    $$ ds^2 = dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2 $$

    ### 2. Lagrangiano

    El lagrangiano en coordenadas esféricas es:

    $$ L = T - U = \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2 + r^2\sin^2\theta\dot{\phi}^2) + \frac{\alpha}{r} $$

    ### 3. Momentos Conjugados

    Los momentos conjugados se definen como $p_i = \frac{\partial L}{\partial \dot{q}^i}$:

    $$ p_r = \frac{\partial L}{\partial \dot{r}} = m\dot{r} $$
    $$ p_\theta = \frac{\partial L}{\partial \dot{\theta}} = mr^2\dot{\theta} $$
    $$ p_\phi = \frac{\partial L}{\partial \dot{\phi}} = mr^2\sin^2\theta\dot{\phi} $$

    ### 4. Transformación Legendre y Hamiltoniano

    El hamiltoniano se obtiene mediante la transformación de Legendre:

    $$ H = \sum_i p_i\dot{q}^i - L $$

    Sustituyendo:

    $$ H = p_r\dot{r} + p_\theta\dot{\theta} + p_\phi\dot{\phi} - L $$

    Expresando las velocidades en términos de los momentos:

    $$ \dot{r} = \frac{p_r}{m}, \quad \dot{\theta} = \frac{p_\theta}{mr^2}, \quad \dot{\phi} = \frac{p_\phi}{mr^2\sin^2\theta} $$

    Sustituyendo en la expresión del hamiltoniano:

    $$ H = \frac{p_r^2}{m} + \frac{p_\theta^2}{mr^2} + \frac{p_\phi^2}{mr^2\sin^2\theta} - \left[ \frac{1}{2}m\left(\frac{p_r^2}{m^2} + r^2\frac{p_\theta^2}{m^2r^4} + r^2\sin^2\theta\frac{p_\phi^2}{m^2r^4\sin^4\theta}\right) + \frac{\alpha}{r} \right] $$

    Simplificando:

    $$ H = \frac{p_r^2}{m} + \frac{p_\theta^2}{mr^2} + \frac{p_\phi^2}{mr^2\sin^2\theta} - \frac{1}{2}\left(\frac{p_r^2}{m} + \frac{p_\theta^2}{mr^2} + \frac{p_\phi^2}{mr^2\sin^2\theta}\right) - \frac{\alpha}{r} $$

    Finalmente, obtenemos el **hamiltoniano en coordenadas esféricas**:

    $$ \boxed{H = \frac{p_r^2}{2m} + \frac{p_\theta^2}{2mr^2} + \frac{p_\phi^2}{2mr^2\sin^2\theta} - \frac{\alpha}{r}} $$

    ### 5. Interpretación Física

    - El primer término representa la energía cinética radial
    - El segundo término representa la energía cinética asociada al movimiento en $\theta$
    - El tercer término representa la energía cinética asociada al movimiento en $\phi$
    - El último término es la energía potencial

    ### 6. Ecuaciones de Hamilton

    Las ecuaciones de Hamilton son:

    $$ \dot{r} = \frac{\partial H}{\partial p_r} = \frac{p_r}{m} $$
    $$ \dot{\theta} = \frac{\partial H}{\partial p_\theta} = \frac{p_\theta}{mr^2} $$
    $$ \dot{\phi} = \frac{\partial H}{\partial p_\phi} = \frac{p_\phi}{mr^2\sin^2\theta} $$
    $$ \dot{p}_r = -\frac{\partial H}{\partial r} = \frac{p_\theta^2}{mr^3} + \frac{p_\phi^2}{mr^3\sin^2\theta} - \frac{\alpha}{r^2} $$
    $$ \dot{p}_\theta = -\frac{\partial H}{\partial \theta} = \frac{p_\phi^2\cos\theta}{mr^2\sin^3\theta} $$
    $$ \dot{p}_\phi = -\frac{\partial H}{\partial \phi} = 0 $$

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
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Parámetros del Sistema")
        
        alpha = st.slider("Constante α", 0.1, 5.0, 1.0, 0.1)
        masa = st.slider("Masa m", 0.1, 5.0, 1.0, 0.1)
        L = st.slider("Momento angular L", 0.1, 3.0, 1.0, 0.1)
        energia = st.slider("Energía E", -1.0, 2.0, -0.2, 0.1)
        
        st.markdown("### Potencial Efectivo")
        st.latex(r"U_{\text{eff}}(r) = -\frac{\alpha}{r} + \frac{L^2}{2mr^2}")
    
    with col2:
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
        ax1.set_xlim(0, 10)
        
        # Espacio de fases (r vs p_r)
        # Para una energía dada E, p_r = ±√[2m(E - U_eff(r))]
        r_min = 0.3
        r_vals = np.linspace(r_min, 10, 500)
        U_eff_vals = -alpha/r_vals + L**2/(2*masa*r_vals**2)
        
        # Solo graficar donde E >= U_eff
        valid_indices = energia >= U_eff_vals
        r_valid = r_vals[valid_indices]
        
        if len(r_valid) > 0:
            p_r_pos = np.sqrt(2*masa*(energia - (-alpha/r_valid + L**2/(2*masa*r_valid**2))))
            p_r_neg = -p_r_pos
            
            ax2.plot(r_valid, p_r_pos, 'b-', linewidth=2, label='Espacio de fases')
            ax2.plot(r_valid, p_r_neg, 'b-', linewidth=2)
            ax2.set_xlabel('r')
            ax2.set_ylabel('p_r')
            ax2.set_title('Espacio de Fases (r, p_r)')
            ax2.grid(True)
            ax2.legend()
        
        st.pyplot(fig1)
    
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
    st.header("🔄 Ejercicios Matemáticos Interactivos")
    
    # Ejercicio 1: Cálculo del potencial efectivo
    st.subheader("Ejercicio 1: Potencial Efectivo")
    st.markdown(r"""
    Dado el potencial central $U(r) = -\dfrac{\alpha}{r}$ y momento angular $L$,
    calcula el potencial efectivo $U_{\text{eff}}(r)$.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.latex(r"U_{\text{eff}}(r) = ?")
        opcion_potencial = st.selectbox(
            "Selecciona la expresión correcta:",
            [
                r"-\frac{\alpha}{r}",
                r"-\frac{\alpha}{r} + \frac{L}{r}",
                r"-\frac{\alpha}{r} + \frac{L^2}{2mr^2}",
                r"-\frac{\alpha}{r} - \frac{L^2}{2mr^2}"
            ]
        )
    
    with col2:
        if st.button("Verificar Potencial Efectivo"):
            if opcion_potencial == r"-\frac{\alpha}{r} + \frac{L^2}{2mr^2}":
                st.success("✅ Correcto! Esta es la expresión del potencial efectivo.")
                st.latex(r"U_{\text{eff}}(r) = -\frac{\alpha}{r} + \frac{L^2}{2mr^2}")
            else:
                st.error("❌ Incorrecto. Recuerda que el potencial efectivo incluye el término centrífugo.")
    
    # Ejercicio 2: Hamiltoniano interactivo
    st.subheader("Ejercicio 2: Hamiltoniano en Coordenadas Esféricas")
    st.markdown("Completa la expresión del hamiltoniano:")
    
    hamiltoniano = r"H = \frac{p_r^2}{2m} + "
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        term1 = st.selectbox("Término θ:",
                            [r"\frac{p_\theta}{mr}",
                             r"\frac{p_\theta^2}{2mr^2}",
                             r"\frac{p_\theta}{2mr^2}"])
    
    with col2:
        term2 = st.selectbox("Término φ:",
                            [r"\frac{p_\phi^2}{2mr^2\sin\theta}",
                             r"\frac{p_\phi}{2mr^2\sin^2\theta}",
                             r"\frac{p_\phi^2}{2mr^2\sin^2\theta}"])
    
    with col3:
        term3 = st.selectbox("Término potencial:",
                            [r"-\frac{\alpha}{r}",
                             r"+\frac{\alpha}{r}",
                             r"-\alpha r"])
    
    hamiltoniano_completo = f"H = \\frac{{p_r^2}}{{2m}} + {term1} + {term2} + {term3}"
    
    st.latex(hamiltoniano_completo)
    
    if st.button("Verificar Hamiltoniano"):
        if (term1 == r"\frac{p_\theta^2}{2mr^2}" and 
            term2 == r"\frac{p_\phi^2}{2mr^2\sin^2\theta}" and 
            term3 == r"-\frac{\alpha}{r}"):
            st.success("✅ Hamiltoniano Correcto!")
            st.balloons()
        else:
            st.error("❌ Revisa los términos del hamiltoniano.")
    
    # Ejercicio 3: Cálculo numérico
    st.subheader("Ejercicio 3: Cálculo de Radio de Órbita Circular")
    st.markdown(r"""
    Para una órbita circular, la fuerza centrífuga iguala a la fuerza del potencial:
    """)
    st.latex(r"\frac{L^2}{mr^3} = \frac{\alpha}{r^2}")
    
    alpha_ej = st.slider("α", 0.1, 5.0, 1.0, 0.1, key="alpha_ej")
    L_ej = st.slider("L", 0.1, 3.0, 1.0, 0.1, key="L_ej")
    m_ej = st.slider("m", 0.1, 5.0, 1.0, 0.1, key="m_ej")
    
    radio_calculado = L_ej**2 / (m_ej * alpha_ej)
    
    st.markdown(f"Radio de órbita circular calculado: $r = {radio_calculado:.3f}$")
    
    respuesta_usuario = st.number_input("Ingresa tu respuesta para el radio:", 
                                       min_value=0.1, max_value=10.0, value=1.0, step=0.1)
    
    if st.button("Verificar Radio"):
        if abs(respuesta_usuario - radio_calculado) < 0.01:
            st.success("✅ Correcto! Has calculado bien el radio de la órbita circular.")
        else:
            st.error(f"❌ Incorrecto. El radio correcto es {radio_calculado:.3f}")

# Pie de página
st.markdown("---")
st.markdown("### 📚 Recursos Adicionales")
st.markdown("""
- Goldstein, H., Poole, C., & Safko, J. (2001). Classical Mechanics
- Landau, L. D., & Lifshitz, E. M. (1976). Mechanics
- Marion, J. B., & Thornton, S. T. (1995). Classical Dynamics of Particles and Systems
""")