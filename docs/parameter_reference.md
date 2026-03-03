# Parameter Reference

## S_yield - Spin Quantum Yield
Photon-to-radical-pair conversion efficiency.
- Formula: Φ_RP = k_ET / (k_ET + k_rec)
- Weight: 22%
- Threshold: >0.85 for optimal function

## ΔE_zeeman - Zeeman Energy Splitting
Energy gap between spin states under Earth's field.
- Formula: ΔE = γₑ ℏ B₀ cosθ
- Weight: 18%
- Value at 50 µT: 5.6 × 10⁻²⁷ J (kT/780)

## Γ_coh - Quantum Coherence Lifetime
Duration of singlet-triplet quantum coherence.
- Formula: τ_coh = -1 / Re(λ_relax)
- Weight: 16%
- Required: >4.7 µs for <5° precision

## θ_inc - Magnetic Inclination Sensitivity
Angular resolution for geomagnetic inclination.
- Formula: θ_inc = arctan(Bz / √(Bx² + By²))
- Weight: 14%
- Precision: <5° demonstrated

## χ_para - Paramagnetic Susceptibility
Biogenic magnetite contribution.
- Formula: χ_para = M / H = N µ² / (3k_B T)
- Weight: 10%
- Magnetite moment: 1.4 × 10⁻¹⁷ J/T

## P_singlet - Singlet-Triplet Probability
Primary output variable encoding direction.
- Formula: P_S(t) = Tr[P̂_S ρ(t)]
- Weight: 9%
- Modulation: ΔΦ = 0.001-0.01

## Ω_dipole - Dipolar Coupling Tensor
Inter-radical dipole-dipole interaction.
- Formula: Ĥ_dipolar = Ŝₐ · D · Ŝᵦ
- Weight: 6%
- Distance: 19.5 Å in ErCry4a

## V_nav - Navigational Vector Precision
Final heading accuracy from population integration.
- Formula: V_nav = R · exp(iΘ_mean)
- Weight: 5%
- R > 0.85 for optimal navigation
