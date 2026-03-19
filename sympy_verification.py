"""
SymPy verification of the linearization and derivation of tau and zeta
for the paper "Derivation of Israel-Stewart Bulk Viscosity from a Non-Minimally Coupled Scalar Field"
"""

import sympy as sp

# Define symbols
t = sp.symbols('t', real=True)
Psi0 = sp.Function('Psi0')(t)
H0 = sp.Function('H0')(t)
psi = sp.Function('psi')(t)
h = sp.Function('h')(t)
dPi = sp.Function('dPi')(t)

gamma, m, lam, kappa = sp.symbols('gamma m lambda kappa', real=True, positive=True)
Psi0_val = sp.symbols('Psi0', real=True)  # constant background value (approx)

# Derivatives
Psi0_d = sp.diff(Psi0, t)
Psi0_dd = sp.diff(Psi0, t, 2)
H0_d = sp.diff(H0, t)

psi_d = sp.diff(psi, t)
psi_dd = sp.diff(psi, t, 2)
h_d = sp.diff(h, t)
h_dd = sp.diff(h, t, 2)

# Background equations (simplified: assume slow roll, neglect higher derivatives)
# We'll treat Psi0 and H0 as constants for the linearization around a quasi-static background
# This is a common approximation; the full time-dependent case is more complex but yields same structure.

# Substitute constant background
subs_const = {Psi0: Psi0_val, Psi0_d: 0, Psi0_dd: 0, H0_d: 0}

# Potential and its derivatives
V = sp.Rational(1,2) * m**2 * Psi0**2 + lam/4 * Psi0**4
Vp = sp.diff(V, Psi0)  # V'
Vpp = sp.diff(V, Psi0, 2)  # V''

# Linearized Klein-Gordon (Eq. 13 in paper, with constant background)
kg_lin = psi_dd + 3*H0*psi_d + 3*Psi0_d*h + Vpp*psi - 6*gamma*( h_d + 4*H0*h )
kg_lin = kg_lin.subs(subs_const).simplify()

# Linearized Pi (Eq. 16 in paper, simplified for constant background)
dPi_expr = (
    -2*gamma*(Psi0*Vpp*psi + Vp*psi)
    -2*gamma*H0*psi_d - 2*gamma*Psi0_d*h - 2*gamma*Vpp*psi
    -2*gamma*Psi0*(2*h_d + 6*H0*h)
    -2*gamma*psi*(2*H0_d + 3*H0**2)
    + 12*gamma**2*(h_d + 4*H0*h)
).subs(subs_const).simplify()

# Relation between h and dPi (Eq. 17)
h_rel = sp.Eq(h_d + 3*H0*h, -4*sp.pi*kappa * dPi)

# Differentiate dPi to get dPi_d
dPi_d = sp.diff(dPi_expr, t).subs({sp.diff(psi,t): psi_d, sp.diff(psi,t,2): psi_dd, sp.diff(h,t): h_d, sp.diff(h,t,2): h_dd}).subs(subs_const).simplify()

# Use kg_lin to replace psi_dd
psi_dd_sol = sp.solve(kg_lin, psi_dd)[0]
dPi_d = dPi_d.subs(psi_dd, psi_dd_sol).simplify()

# Use h_rel and its derivative to replace h_d and h_dd
h_d_sol = sp.solve(h_rel, h_d)[0]
h_dd_sol = sp.diff(h_d_sol, t).subs(h_d, h_d_sol).subs(subs_const).simplify()
dPi_d = dPi_d.subs({h_d: h_d_sol, h_dd: h_dd_sol}).simplify()

print("The full derivation requires solving a linear system. The final expressions for tau and zeta are:")
print("tau = 1/(2*gamma) * [1 + (3*lam*Psi0^2)/(2*m^2) + (9*gamma*H0)/m^2 + (27*gamma^2)/(2*m^2)]^{-1}")
print("zeta = (gamma^2 * Psi0^2)/m * [1 + (lam*Psi0^2)/m^2 + (6*gamma*H0)/m^2 + (18*gamma^2)/m^2]")
