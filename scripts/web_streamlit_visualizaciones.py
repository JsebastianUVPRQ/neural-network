import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
import time

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Visualizaciones de Física Universitaria",
    page_icon="⚛️",
    layout="wide"
)

st.title("⚛️ Visualizaciones Interactivas de Física")
st.markdown("Explora conceptos clave de física universitaria con simulaciones en tiempo real.")

# --- Barra Lateral de Navegación ---
st.sidebar.header("Menú de Conceptos")
opcion = st.sidebar.radio(
    "Selecciona un Tema:",
    [
        "Campo Eléctrico",
        # ¡NUEVAS OPCIONES AQUÍ!
        "Ecuaciones de Euler-Lagrange",
        "Potenciales Centrales",
        "Funciones Trigonométricas Hiperbólicas"
    ]
)


st.sidebar.markdown("---")
st.sidebar.info("Esta web está construida con Python y Streamlit.")

# --- Función para Campo Eléctrico ---
def visualizacion_campo_electrico():
    """Muestra el campo eléctrico de una carga puntual."""
    st.header("Campo Eléctrico de una Carga Puntual")
    st.write("El campo eléctrico ($\vec{E}$) de una carga puntual ($Q$) es $\vec{E} = k \frac{Q}{r^2}\hat{r}$.")
    
    # Parámetros de entrada
    Q = st.slider("Magnitud de la Carga ($Q$ en $\mu C$)", -10.0, 10.0, 5.0, 1.0)
    
    # Constante de Coulomb (k)
    k = 8.99e9 # N m^2/C^2 (aproximado)
    
    st.subheader(f"Carga: $Q = {Q} \mu C$")
    
    # Configuración de la cuadrícula
    L_grid = 5.0 # Lado de la cuadrícula
    N = 15 # Número de puntos
    x = np.linspace(-L_grid, L_grid, N)
    y = np.linspace(-L_grid, L_grid, N)
    X, Y = np.meshgrid(x, y)
    
    # Posición de la carga
    x_carga, y_carga = 1, 1
    
    # Cálculo del campo eléctrico
    r_x = X - x_carga
    r_y = Y - y_carga
    R_sq = r_x**2 + r_y**2
    R = np.sqrt(R_sq)
    
    # Evitar la división por cero en la posición de la carga
    R[R < 0.1] = 0.1 
    
    # Magnitud del campo (escala arbitraria)
    E_mag = (k * (Q * 1e-6)) / R_sq
    
    # Componentes del campo
    Ex = E_mag * (r_x / R)
    Ey = E_mag * (r_y / R)
    
    # Normalizar las flechas para una mejor visualización
    E_mag_norm = np.sqrt(Ex**2 + Ey**2)
    Ex_norm = Ex / E_mag_norm
    Ey_norm = Ey / E_mag_norm
    
    # Gráfica
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Campo eléctrico (usando quiver)
    ax.quiver(X, Y, Ex_norm, Ey_norm, color='blue' if Q > 0 else 'red', scale=20, scale_units='inches', alpha=0.7)
    
    # Dibujar la carga
    color_carga = 'red' if Q < 0 else 'blue'
    marker_carga = 'o'
    ax.plot(x_carga, y_carga, marker_carga, color=color_carga, markersize=15)
    
    # Etiquetas y título
    ax.set_xlabel("x (unidades)")
    ax.set_ylabel("y (unidades)")
    ax.set_title(f"Campo Eléctrico de una Carga Puntual ($Q = {Q} \mu C$)")
    ax.set_xlim(-L_grid, L_grid)
    ax.set_ylim(-L_grid, L_grid)
    ax.grid(True, linestyle='--', alpha=0.6)
    
    st.pyplot(fig)
    
    # Explicación del campo
    st.subheader("Dirección del Campo")
    if Q > 0:
        st.write("El campo eléctrico se dirige **radialmente hacia afuera** de la carga positiva (fuente).")
        st.markdown(" Image of electric field lines from a positive charge")
    elif Q < 0:
        st.write("El campo eléctrico se dirige **radialmente hacia adentro** de la carga negativa (sumidero).")
        st.markdown("")
    else:
        st.write("La carga es cero, por lo tanto, no hay campo eléctrico.")


# Continúa en app_fisica.py

# --- Función para Euler-Lagrange ---
def visualizacion_euler_lagrange():
    """Permite ingresar una Lagrangiana simple y muestra su E-L."""
    st.header("Ecuaciones de Euler-Lagrange (Mecánica Analítica) 🚀")
    st.write("Las ecuaciones de Euler-Lagrange determinan las ecuaciones de movimiento de un sistema: $\\frac{d}{dt}\\left(\\frac{\\partial L}{\\partial \\dot{q}}\\right) - \\frac{\\partial L}{\\partial q} = 0$.")

    st.subheader("Lagrangiana Simple: $L = \\frac{1}{2}m\\dot{x}^2 - V(x)$")
    st.markdown("Consideramos una Lagrangiana unidimensional simple con coordenadas $q=x$.")
    
    m = st.number_input("Masa ($m$)", value=1.0, step=0.1)
    
    st.markdown("---")
    
    st.subheader("Selecciona el Potencial $V(x)$")
    potencial = st.radio(
        "Potencial a modelar:",
        ["Masa Resorte ($V = \\frac{1}{2}kx^2$)", "Caída Libre ($V = mgx$)", "Potencial Cúbico ($V = ax^3$)", "Otro..."]
    )
    
    # Derivadas de L
    dL_d_dot_x = f"$m\\dot{x}$"
    dL_dt_dL_d_dot_x = f"$m\\ddot{x}$" # Derivada temporal
    
    # Resultado de la Ecuación de Euler-Lagrange
    E_L_result = "..."

    if potencial == "Masa Resorte ($V = \\frac{1}{2}kx^2$)":
        k = st.number_input("Constante de Resorte ($k$)", value=1.0, step=0.1)
        dL_dx = f"$-kx$" # - dV/dx
        E_L_result = f"$m\\ddot{x} + {k}x = 0$ (Movimiento Armónico Simple)"
    elif potencial == "Caída Libre ($V = mgx$)":
        g = st.number_input("Gravedad ($g$)", value=9.81, step=0.1)
        dL_dx = f"$-{m*g:.2f}$" # - dV/dx
        E_L_result = f"$m\\ddot{x} + {m*g:.2f} = 0 \\Rightarrow \\ddot{x} = -g$ (Caída Libre)"
    elif potencial == "Potencial Cúbico ($V = ax^3$)":
        a = st.number_input("Constante ($a$)", value=1.0, step=0.1)
        dL_dx = f"$-3{a}x^2$" # - dV/dx
        E_L_result = f"$m\\ddot{x} + 3{a}x^2 = 0$"
    else:
        st.info("Ingresa la forma de tu potencial $V(x)$ para el análisis.")
        return

    st.markdown("---")
    st.subheader("Cálculo Detallado")
    
    # Primera parte de E-L: Derivada respecto a la velocidad generalizada
    st.latex(f"\\frac{{\\partial L}}{{\\partial \\dot{x}}} = \\frac{{\\partial}}{{\\partial \\dot{x}}} \\left( \\frac{{1}}{{2}}m\\dot{{x}}^2 - V(x) \\right) = {dL_d_dot_x}")
    # Segunda parte: Derivada temporal de la primera parte
    st.latex(f"\\frac{{d}}{{dt}}\\left(\\frac{{\\partial L}}{{\\partial \\dot{{x}}}}\\right) = \\frac{{d}}{{dt}} \\left( {dL_d_dot_x} \\right) = {dL_dt_dL_d_dot_x}")
    
    # Tercera parte: Derivada respecto a la coordenada generalizada
    st.latex(f"\\frac{{\\partial L}}{{\\partial x}} = \\frac{{\\partial}}{{\\partial x}} \\left( \\frac{{1}}{{2}}m\\dot{{x}}^2 - V(x) \\right) = -\\frac{{\\partial V}}{{\\partial x}} = {dL_dx}")
    
    st.subheader("Ecuación de Movimiento Resultante (Euler-Lagrange):")
    st.latex(E_L_result)
    st.success("Esta es la ecuación diferencial que describe el movimiento del sistema.")

# --- Función para Potenciales Centrales ---
def visualizacion_potenciales_centrales():
    """Muestra el Potencial Efectivo de un potencial central."""
    st.header("Potenciales Centrales y Potencial Efectivo 🌌")
    st.write("El movimiento en un potencial central $V(r)$ se reduce a un problema unidimensional con el **Potencial Efectivo** $V_{eff}(r) = V(r) + \\frac{l^2}{2\\mu r^2}$.")

    # Parámetros de entrada
    L = st.slider("Momento Angular ($l$)", 0.1, 5.0, 1.0, 0.1)
    mu = st.slider("Masa Reducida ($\\mu$)", 0.1, 2.0, 1.0, 0.1)

    st.subheader("Selecciona el Potencial Central $V(r)$")
    potencial_central = st.radio(
        "Potencial a modelar:",
        ["Gravitatorio/Coulomb Atractivo ($V(r) = -k/r$)", "Oscilador Armónico ($V(r) = \\frac{1}{2}kr^2$)"]
    )

    r = np.linspace(0.1, 10.0, 200)

    # Cálculo del Potencial Centrífugo
    V_centrifugo = L**2 / (2 * mu * r**2)

    # Cálculo de V(r) y V_efectivo(r)
    k_val = 10.0 # Constante simple para la visualización
    V_r = np.zeros_like(r)
    
    if potencial_central == "Gravitatorio/Coulomb Atractivo ($V(r) = -k/r$)":
        V_r = -k_val / r
        nombre_potencial = "Potencial Gravitatorio/Coulomb"
    elif potencial_central == "Oscilador Armónico ($V(r) = \\frac{1}{2}kr^2$)":
        V_r = 0.5 * k_val * r**2
        nombre_potencial = "Potencial Oscilador Armónico"
    
    V_efectivo = V_r + V_centrifugo

    # Gráfica
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(r, V_efectivo, label='$V_{eff}(r)$ (Potencial Efectivo)', color='blue')
    ax.plot(r, V_r, '--', label='$V(r)$ (' + nombre_potencial + ')', color='green', alpha=0.7)
    ax.plot(r, V_centrifugo, ':', label='$V_{centr}(r)$', color='red', alpha=0.7)
    
    ax.set_ylim(min(V_efectivo.min(), V_r.min(), -1) - 2, V_efectivo.max() + 2)
    ax.set_xlabel("Distancia Radial ($r$)")
    ax.set_ylabel("Energía (Unidades Arbitrarias)")
    ax.set_title(f"Potencial Efectivo con $l={L}, \\mu={mu}$")
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)
    
    st.subheader("Análisis del Potencial Efectivo")
    st.write("La forma de $V_{eff}(r)$ determina la órbita. Un mínimo en la curva indica una órbita circular estable.")
    if potencial_central == "Gravitatorio/Coulomb Atractivo ($V(r) = -k/r$)":
        st.info("Para $V(r) = -k/r$, el mínimo en $V_{eff}$ permite **órbitas elípticas, parabólicas e hiperbólicas** (problema de Kepler).")
    
# --- Funciones Trigonométricas Hiperbólicas (para Matemáticas/Física) ---
def visualizacion_trigonometricas_hiperbolicas():
    """Muestra las funciones sinh, cosh y tanh."""
    st.header("Funciones Trigonométricas Hiperbólicas $\\text{sinh}(x)$, $\\text{cosh}(x)$ 📐")
    st.write("Las funciones hiperbólicas se definen a partir de la exponencial: $\\text{cosh}(x) = \\frac{e^x + e^{-x}}{2}$ y $\\text{sinh}(x) = \\frac{e^x - e^{-x}}{2}$. Son fundamentales en el estudio de catenarias, relatividad y soluciones de ecuaciones diferenciales.")

    # Parámetros de entrada
    x_max = st.slider("Rango de $x$ ($\\pm x_{max}$)", 1.0, 5.0, 3.0, 0.1)

    # Cálculo
    x = np.linspace(-x_max, x_max, 200)
    sinh_x = np.sinh(x)
    cosh_x = np.cosh(x)
    tanh_x = np.tanh(x)

    # Gráfica
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, sinh_x, label='$\\text{sinh}(x)$', color='blue')
    ax.plot(x, cosh_x, label='$\\text{cosh}(x)$', color='red')
    ax.plot(x, tanh_x, label='$\\text{tanh}(x)$', color='green', linestyle='--')
    
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    
    ax.set_ylim(-3, max(5, cosh_x.max() * 1.1))
    ax.set_xlabel("$x$")
    ax.set_ylabel("Valor de la Función")
    ax.set_title("Funciones Hiperbólicas")
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)
    
    st.subheader("Propiedades Clave")
    st.markdown("""
    * $\\text{cosh}(x)$ es **par** y similar a una parábola, pero crece exponencialmente.
    * $\\text{sinh}(x)$ es **impar** y similar a $x^3$.
    * $\\text{cosh}^2(x) - \\text{sinh}^2(x) = 1$ (análogo a $\\cos^2\\theta + \\sin^2\\theta = 1$).
    * La forma de la **catenaria** (cuerda colgante) es una $\\text{cosh}(x)$.
    """)


# --- Lógica Principal de la App ---
if opcion == "Campo Eléctrico":
    visualizacion_campo_electrico()
    
# ¡NUEVOS LLAMADOS A FUNCIONES AQUÍ!
elif opcion == "Ecuaciones de Euler-Lagrange":
    visualizacion_euler_lagrange()

elif opcion == "Potenciales Centrales":
    visualizacion_potenciales_centrales()

elif opcion == "Funciones Trigonométricas Hiperbólicas":
    visualizacion_trigonometricas_hiperbolicas()

st.markdown("---")
st.caption("Hecho con ❤️ para la enseñanza de la Física.")