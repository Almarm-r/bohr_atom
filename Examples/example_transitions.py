"""
Ejemplo de transiciones electrónicas y series espectrales.

Este script calcula y visualiza las series espectrales del hidrógeno:
- Serie de Lyman (UV)
- Serie de Balmer (visible)
- Serie de Paschen (IR)
"""

import matplotlib.pyplot as plt
from bohr_atom import BohrAtom


def analyze_series(atom, n_final, series_name, n_range):
    """
    Analiza una serie espectral completa.
    
    Parámetros
    ----------
    atom : BohrAtom
        El átomo a analizar
    n_final : int
        Nivel final de las transiciones
    series_name : str
        Nombre de la serie
    n_range : range
        Rango de niveles iniciales
    """
    print(f"\n{'=' * 70}")
    print(f"SERIE DE {series_name.upper()} (transiciones hacia n={n_final})")
    print(f"{'=' * 70}")
    
    wavelengths = []
    transitions = []
    
    for n_initial in n_range:
        wavelength_nm = atom.transition_wavelength_nm(n_initial, n_final)
        frequency = atom.transition_frequency(n_initial, n_final)
        energy_eV = abs(atom.transition_energy(n_initial, n_final)) / 1.602176634e-19
        
        wavelengths.append(wavelength_nm)
        transitions.append((n_initial, n_final))
        
        print(f"\nn={n_initial} → n={n_final}:")
        print(f"  λ = {wavelength_nm:.2f} nm")
        print(f"  ν = {frequency:.4e} Hz")
        print(f"  ΔE = {energy_eV:.3f} eV")
    
    return wavelengths, transitions


def main():
    print("=" * 70)
    print("ANÁLISIS DE SERIES ESPECTRALES DEL HIDRÓGENO")
    print("=" * 70)
    
    # Crear átomo de hidrógeno
    hydrogen = BohrAtom(Z=1)
    
    # 1. SERIE DE LYMAN (UV)
    wavelengths_lyman, trans_lyman = analyze_series(
        hydrogen, n_final=1, series_name="Lyman",
        n_range=range(2, 7)
    )
    
    # 2. SERIE DE BALMER (Visible)
    wavelengths_balmer, trans_balmer = analyze_series(
        hydrogen, n_final=2, series_name="Balmer",
        n_range=range(3, 8)
    )
    
    # 3. SERIE DE PASCHEN (IR)
    wavelengths_paschen, trans_paschen = analyze_series(
        hydrogen, n_final=3, series_name="Paschen",
        n_range=range(4, 9)
    )
    
    # VISUALIZACIÓN 1: Diagrama de niveles con todas las series
    print("\n" + "=" * 70)
    print("GENERANDO VISUALIZACIONES...")
    print("=" * 70)
    
    fig1 = hydrogen.plot_energy_levels(
        n_max=8,
        show_transitions=True,
        transitions=trans_lyman[:3] + trans_balmer[:3] + trans_paschen[:2]
    )
    fig1.suptitle("Series Espectrales del Hidrógeno", fontsize=16, y=0.98)
    
    # VISUALIZACIÓN 2: Espectro de longitudes de onda
    fig2, ax = plt.subplots(figsize=(12, 6))
    
    # Serie de Lyman
    for i, (wl, (ni, nf)) in enumerate(zip(wavelengths_lyman, trans_lyman)):
        ax.axvline(wl, color='purple', alpha=0.6, linewidth=2)
        ax.text(wl, 0.9 - i*0.05, f'{ni}→{nf}', rotation=90, 
               verticalalignment='top', fontsize=8, color='purple')
    
    # Serie de Balmer
    for i, (wl, (ni, nf)) in enumerate(zip(wavelengths_balmer, trans_balmer)):
        ax.axvline(wl, color='red', alpha=0.6, linewidth=2)
        ax.text(wl, 0.9 - i*0.05, f'{ni}→{nf}', rotation=90,
               verticalalignment='top', fontsize=8, color='red')
    
    # Serie de Paschen
    for i, (wl, (ni, nf)) in enumerate(zip(wavelengths_paschen[:3], trans_paschen[:3])):
        ax.axvline(wl, color='brown', alpha=0.6, linewidth=2)
        ax.text(wl, 0.9 - i*0.05, f'{ni}→{nf}', rotation=90,
               verticalalignment='top', fontsize=8, color='brown')
    
    # Regiones del espectro
    ax.axvspan(380, 450, alpha=0.1, color='violet', label='Visible')
    ax.axvspan(450, 495, alpha=0.1, color='blue')
    ax.axvspan(495, 570, alpha=0.1, color='green')
    ax.axvspan(570, 590, alpha=0.1, color='yellow')
    ax.axvspan(590, 620, alpha=0.1, color='orange')
    ax.axvspan(620, 750, alpha=0.1, color='red')
    ax.axvspan(10, 380, alpha=0.05, color='purple', label='UV')
    ax.axvspan(750, 2000, alpha=0.05, color='brown', label='IR')
    
    ax.set_xlabel('Longitud de onda (nm)', fontsize=12)
    ax.set_ylabel('Intensidad (arbitraria)', fontsize=12)
    ax.set_title('Espectro de Emisión del Hidrógeno - Series Espectrales', fontsize=14)
    ax.set_xlim(0, 2000)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    
    # VISUALIZACIÓN 3: Órbitas
    fig3 = hydrogen.plot_orbits(n_max=6)
    
    # RESUMEN FINAL
    print("\n" + "=" * 70)
    print("RESUMEN DE LONGITUDES DE ONDA")
    print("=" * 70)
    
    print(f"\nSerie de Lyman (UV):")
    print(f"  Rango: {min(wavelengths_lyman):.1f} - {max(wavelengths_lyman):.1f} nm")
    
    print(f"\nSerie de Balmer (Visible):")
    print(f"  Rango: {min(wavelengths_balmer):.1f} - {max(wavelengths_balmer):.1f} nm")
    print(f"  H-alpha (3→2): {wavelengths_balmer[0]:.1f} nm (rojo)")
    print(f"  H-beta  (4→2): {wavelengths_balmer[1]:.1f} nm (azul-verde)")
    print(f"  H-gamma (5→2): {wavelengths_balmer[2]:.1f} nm (azul)")
    print(f"  H-delta (6→2): {wavelengths_balmer[3]:.1f} nm (violeta)")
    
    print(f"\nSerie de Paschen (IR):")
    print(f"  Rango: {min(wavelengths_paschen):.1f} - {max(wavelengths_paschen):.1f} nm")
    
    print("\n" + "=" * 70)
    print("Mostrando gráficos...")
    print("=" * 70)
    
    plt.show()


if __name__ == "__main__":
    main()
