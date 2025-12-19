# Omega-Strong

**Omega-Strong** is a classical effective strong-field regime of gravity
based on **geometric saturation of curvature**.
It provides a proof-of-concept mechanism by which spacetime singularities
can be avoided without invoking exotic matter or quantum gravity.

This repository contains **Omega-Strong v1**, a closed and self-consistent
implementation including the theoretical framework and numerical solutions.

---

## Motivation

In General Relativity, strong gravitational collapse generically leads
to curvature singularities, signaling a breakdown of the classical theory.
Omega-Strong explores the possibility that gravity may dynamically
self-regulate at high curvature through a purely geometric mechanism.

The guiding idea is that the same scalar degree of freedom responsible
for controlled deviations from GR in weak-field regimes
may also regulate the strong-field regime.

---

## Core Idea

Omega-Strong introduces a curvature scale \( R_\star \) such that:

- **For \( R \gg R_\star \)**  
  The system enters a *saturated regime* where scalar dynamics are
  dynamically suppressed and curvature remains finite.

- **For \( R \lesssim R_\star \)**  
  The theory smoothly transitions back to a GR-like regime with
  standard scalar dynamics.

Importantly, the transition scale is **geometrically controlled** and
does not depend on fine-tuning of the scalar potential.

---

## Main Results

- Existence of a **regular strong-field core** with finite curvature.
- Explicit realization of **geometric saturation** through an effective action.
- Dynamical suppression of scalar gradients in high-curvature regions.
- Non-trivial scalar profiles activated only beyond a curvature threshold.
- Numerical confirmation that the transition radius is controlled by \( R_\star \),
  not by the scalar mass.

A representative scalar profile is shown below:

![Scalar profile](figures/omega_profile_v1.png)

---

## Repository Structure

- `code/`
  - `omega_strong_core.py`  
    Canonical implementation of the Omega-Strong field equations.
  - `omega_strong_m2_scan.py`  
    Parameter scan demonstrating robustness with respect to the scalar mass.

- `figures/`  
  Representative plots generated from the code.

- `paper/`  
  (Optional) LaTeX source for the Omega-Strong manuscript.

---

## Scope and Limitations

Omega-Strong is a **classical effective model**.

It does **not**:
- claim to describe quantum gravity,
- provide direct observational predictions,
- assert uniqueness or completeness.

It is intended as a **proof of existence** for a regular strong-field regime.

---

## Relation to the Omega Program

Omega-Strong is part of the broader **Omega Program**, which includes:

- **Omega-CDM**: late-time cosmological phenomenology (completed)
- **Omega-Strong**: strong-field classical regime (this repository)
- **Omega-UV / Omega-Dark**: ongoing and future extensions

---

## Status

This repository corresponds to **Omega-Strong v1**.
The model is considered closed at this stage.
Further refinements and extensions are left for future work.

---

## License

MIT License.
