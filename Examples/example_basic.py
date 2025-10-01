"""
Ejemplo básico de uso de la librería Bohr Atom.

Este script demuestra los cálculos fundamentales del modelo de Bohr
para el átomo de hidrógeno.
"""

from bohr_atom import BohrAtom


def main():
    print("=" * 60)
    print("EJEMPLO BÁSICO: ÁTOMO DE HIDRÓGENO")
    print("=" * 60)
    
    # Crear átomo de hidrógeno
    hydrogen = BohrAtom(Z=1)
    print(f"\nÁtomo creado: {hydrogen}")
    
    # 1. NIVELES DE ENERGÍA
    print("\n" + "-" * 60)
    print("1. NIVELES DE ENERGÍA")
    print("-" * 60)
    
    for n in range(1, 6):
        E_J = hydrogen.energy_level(n)
        E_eV = hydrogen.energy_level_eV(n)
        print(f"n={n}: E = {E_J:.4e} J = {E_eV:.3f} eV")
    
    # 2. RADIOS ORBITALES
    print("\n" + "-" * 60)
    print("2. RADIOS ORBITALES")
    print("-" * 60)
    
    for n in range(1, 6):
        r_m = hydrogen.orbital_radius(n)
        r_A = hydrogen.orbital_radius_angstrom(n)
        print(f"n={n}: r = {r_m:.4e} m = {r_A:.3f} Å")
    
    # 3. TRANSICIONES ELECTRÓNICAS
    print("\n" + "-" * 60)
    print("3. TRANSICIONES ELECTRÓNICAS - SERIE DE BALMER")
    print("-" * 60)
    print("(Transiciones hacia n=2, luz visible)")
    
    n_final = 2
    for n_initial in range(3, 7):
        delta_E = hydrogen.transition_energy(n_initial, n_final)
        wavelength_nm = hydrogen.transition_wavelength_nm(n_initial, n_final)
        frequency = hydrogen.transition_frequency(n_initial, n_final)
        
        print(f"\nn={n_initial} → n={n_final}:")
        print(f"  ΔE = {abs(delta_E):.4e} J")
        print(f"  λ = {wavelength_nm:.1f} nm")
        print(f"  ν = {frequency:.4e} Hz")
        
        # Clasificar por color
        if wavelength_nm < 450:
            color = "Violeta"
        elif wavelength_nm < 495:
            color = "Azul"
        elif wavelength_nm < 570:
            color = "Verde"
        elif wavelength_nm < 590:
            color = "Amarillo"
        elif wavelength_nm < 620:
            color = "Naranja"
        else:
            color = "Rojo"
        
        print(f"  Color: {color}")
    
    # 4. COMPARACIÓN CON HELIO IONIZADO
    print("\n" + "-" * 60)
    print("4. COMPARACIÓN: H vs He⁺")
    print("-" * 60)
    
    helium_ion = BohrAtom(Z=2)
    
    n = 1
    E_H = hydrogen.energy_level_eV(n)
    E_He = helium_ion.energy_level_eV(n)
    r_H = hydrogen.orbital_radius_angstrom(n)
    r_He = helium_ion.orbital_radius_angstrom(n)
    
    print(f"\nNivel fundamental (n=1):")
    print(f"  H:   E₁ = {E_H:.2f} eV,  r₁ = {r_H:.3f} Å")
    print(f"  He⁺: E₁ = {E_He:.2f} eV,  r₁ = {r_He:.3f} Å")
    print(f"\nRelación de energías: E(He⁺)/E(H) = {E_He/E_H:.2f}")
    print(f"Relación de radios: r(He⁺)/r(H) = {r_He/r_H:.2f}")
    
    # 5. ENERGÍA DE IONIZACIÓN
    print("\n" + "-" * 60)
    print("5. ENERGÍA DE IONIZACIÓN")
    print("-" * 60)
    
    E_ionization = abs(hydrogen.energy_level_eV(1))
    print(f"\nEnergía necesaria para ionizar H desde n=1:")
    print(f"  E_ionización = {E_ionization:.2f} eV")
    print(f"  Equivalente a {E_ionization * 96.485:.1f} kJ/mol")
    
    print("\n" + "=" * 60)
    print("FIN DEL EJEMPLO")
    print("=" * 60)


if __name__ == "__main__":
    main()
