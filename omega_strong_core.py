import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# =========================
# Parámetros del modelo
# =========================
G = 1.0
alpha = 1.0
R_star = 1.0

# Potencial escalar
m2 = 0.05
V0 = 0.1

def V(Omega):
    return V0 + 0.5 * m2 * Omega**2

def dV_dOmega(Omega):
    return m2 * Omega


# =========================
# Sistema Omega-Strong
# =========================
def omega_strong_eq(r, y):
    Omega, Psi, Lambda, Phi = y

    if r < 1e-6:
        r = 1e-6

    A = np.exp(-2.0 * Lambda)

    # Curvatura escalar efectiva
    R = 2.0 * (1.0 - A) / r**2

    # Saturación geométrica
    F = alpha / (1.0 + R / R_star)

    # Densidad y presión radial
    rho = 0.5 * F * A * Psi**2 + V(Omega)
    p_r = 0.5 * F * A * Psi**2 - V(Omega)

    # Ecuaciones de Einstein
    dLambda = (1.0 - A) / (2.0 * r * A) + 4.0 * np.pi * G * r * rho
    dPhi = (A - 1.0) / (2.0 * r * A) + 4.0 * np.pi * G * r * p_r

    # Campo escalar
    dOmega = Psi
    dPsi = -(dPhi - dLambda + 2.0 / r) * Psi \
           + np.exp(2.0 * Lambda) * dV_dOmega(Omega) / F

    return [dOmega, dPsi, dLambda, dPhi]


# =========================
# Condiciones iniciales
# =========================
r0 = 1e-4
r_max = 20.0

Omega0 = 0.8
Psi0 = 0.0
Lambda0 = 0.0
Phi0 = 0.0

y0 = [Omega0, Psi0, Lambda0, Phi0]


# =========================
# Integración
# =========================
sol = solve_ivp(
    omega_strong_eq,
    (r0, r_max),
    y0,
    rtol=1e-6,
    atol=1e-9
)

r = sol.t
Omega, Psi, Lambda, Phi = sol.y

A = np.exp(-2.0 * Lambda)
R = 2.0 * (1.0 - A) / r**2


# =========================
# Escala de transición
# =========================
mask = r > 1e-3
idx = np.argmin(np.abs(R[mask] - R_star))
r_star = r[mask][idx]

print("r_star ≈", r_star)
print("R(r_star) ≈", R[mask][idx])


# =========================
# Gráficas
# =========================
plt.figure()
plt.plot(r, Omega)
plt.xlabel("r")
plt.ylabel("Omega(r)")
plt.title("Perfil escalar Omega(r) — Omega-Strong v1")
plt.show()

plt.figure()
plt.plot(r, R, label="R(r)")
plt.axhline(R_star, linestyle="--", label="R_star")
plt.axvline(r_star, linestyle=":", label="r_star")
plt.yscale("log")
plt.xlabel("r")
plt.ylabel("R(r)")
plt.legend()
plt.title("Escala geométrica de transición")
plt.show()

plt.figure()
plt.plot(r, A)
plt.xlabel("r")
plt.ylabel(r"$e^{-2\Lambda}$")
plt.title("Transición al régimen GR exterior")
plt.show()
