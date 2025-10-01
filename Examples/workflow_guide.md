# 👥 Guía de Trabajo en Equipo - Bohr Atom Project

## Distribución de Tareas por Integrante

### 🔵 Integrante 1: Fundamentos y Constantes

**Responsabilidades:**
- Implementar `constants.py` con todas las constantes físicas
- Implementar métodos de cálculo de energía en `BohrAtom`:
  - `energy_level(n)`
  - `energy_level_eV(n)`
- Crear pruebas para cálculos de energía
- Documentar fórmulas en docstrings

**Rama de trabajo:** `feature/energia-constantes`

**Comandos:**
```bash
git checkout -b feature/energia-constantes
# Trabajar en los archivos
git add bohr_atom/constants.py bohr_atom/bohr_atom.py tests/test_bohr_atom.py
git commit -m "Implementar constantes físicas y cálculo de energía"
git push origin feature/energia-constantes
```

**Archivos a editar:**
- `bohr_atom/constants.py`
- `bohr_atom/bohr_atom.py` (parte de energía)
- `tests/test_bohr_atom.py` (tests de energía)

---

### 🟢 Integrante 2: Radios y Transiciones

**Responsabilidades:**
- Implementar métodos de radios orbitales:
  - `orbital_radius(n)`
  - `orbital_radius_angstrom(n)`
- Implementar métodos de transiciones:
  - `transition_energy(n_i, n_f)`
  - `transition_wavelength(n_i, n_f)`
  - `transition_frequency(n_i, n_f)`
- Crear pruebas para estos métodos
- Crear `example_basic.py`

**Rama de trabajo:** `feature/radios-transiciones`

**Comandos:**
```bash
git checkout main
git pull origin main
git checkout -b feature/radios-transiciones
# Trabajar en los archivos
git add bohr_atom/bohr_atom.py tests/test_bohr_atom.py examples/example_basic.py
git commit -m "Implementar cálculos de radios y transiciones"
git push origin feature/radios-transiciones
```

**Archivos a editar:**
- `bohr_atom/bohr_atom.py` (métodos de radios y transiciones)
- `tests/test_bohr_atom.py` (tests correspondientes)
- `examples/example_basic.py`

---

### 🟡 Integrante 3: Visualizaciones y Documentación

**Responsabilidades:**
- Implementar métodos de visualización:
  - `plot_energy_levels()`
  - `plot_orbits()`
- Crear `example_transitions.py`
- Completar README.md
- Crear documentación adicional

**Rama de trabajo:** `feature/visualizacion-docs`

**Comandos:**
```bash
git checkout main
git pull origin main
git checkout -b feature/visualizacion-docs
# Trabajar en los archivos
git add bohr_atom/bohr_atom.py examples/example_transitions.py README.md
git commit -m "Implementar visualizaciones y completar documentación"
git push origin feature/visualizacion-docs
```

**Archivos a editar:**
- `bohr_atom/bohr_atom.py` (métodos plot)
- `examples/example_transitions.py`
- `README.md`
- Crear ejemplos adicionales

---

## Cronograma Sugerido (4 semanas)

### Semana 1: Setup y Desarrollo Individual

**Día 1-2:**
- Reunión inicial del equipo
- Crear repositorio en GitHub
- Clonar y configurar entornos locales
- Crear estructura base del proyecto
- Cada integrante crea su rama

**Día 3-5:**
- Trabajo individual en ramas
- Implementación de funcionalidades asignadas
- Commits frecuentes (mínimo 1 por día)
- Comunicación constante por chat/Discord

**Día 6-7:**
- Completar implementaciones
- Escribir pruebas unitarias
- Preparar Pull Requests

### Semana 2: Integración y Pruebas

**Día 1-3:**
- Crear Pull Requests
- Revisión de código entre integrantes
- Resolver conflictos si existen
- Aprobar y fusionar PRs a main

**Día 4-5:**
- Ejecutar suite completa de pruebas
- Verificar que toda la funcionalidad funciona integrada
- Corregir bugs encontrados

**Día 6-7:**
- Completar ejemplos de uso
- Mejorar documentación
- Preparar presentación del proyecto

### Semana 3: Refinamiento y Preparación

**Día 1-3:**
- Optimizar código y mejorar calidad
- Aumentar cobertura de pruebas (objetivo: >85%)
- Mejorar docstrings y comentarios

**Día 4-5:**
- Preparar archivos para publicación
- Configurar pyproject.toml final
- Crear archivo MANIFEST.in si es necesario
- Verificar que README esté completo

**Día 6-7:**
- Probar construcción del paquete
- Crear cuentas en PyPI/TestPyPI
- Primera publicación en TestPyPI

### Semana 4: Publicación y Entrega

**Día 1-2:**
- Resolver problemas de TestPyPI
- Verificar instalación desde TestPyPI
- Ajustes finales

**Día 3-4:**
- Publicación oficial en PyPI
- Verificar instalación con pip
- Actualizar README con enlaces

**Día 5-7:**
- Preparar presentación final
- Crear video demo (opcional)
- Documentar contribuciones de cada integrante
- Entrega final del proyecto

---

## Proceso de Pull Request

### Crear un Pull Request

1. **Antes de crear el PR:**
```bash
# Asegurarse de estar actualizado con main
git checkout main
git pull origin main

# Volver a tu rama
git checkout tu-rama

# Actualizar tu rama con los cambios de main
git merge main

# Resolver conflictos si existen
# Ejecutar pruebas
pytest
```

2. **Crear el PR en GitHub:**
   - Ve a tu repositorio en GitHub
   - Click en "Pull requests" > "New pull request"
   - Base: `main` ← Compare: `tu-rama`
   - Título descriptivo: "Implementar cálculo de energía"
   - Descripción detallada:

```markdown
## Descripción
Implementa los métodos para calcular niveles de energía según el modelo de Bohr.

## Cambios realizados
- ✅ Añadido archivo constants.py con constantes físicas
- ✅ Implementado energy_level(n)
- ✅ Implementado energy_level_eV(n)
- ✅ Añadidas pruebas unitarias

## Pruebas
- [x] Todas las pruebas pasan
- [x] Cobertura >80%

## Screenshots (si aplica)
[Capturas de pantalla de resultados]

## Checklist
- [x] Mi código sigue el estilo del proyecto
- [x] He comentado código complejo
- [x] He actualizado la documentación
- [x] Mis cambios no generan nuevos warnings
- [x] He añadido pruebas
```

### Revisar un Pull Request

**Responsabilidades del revisor:**

1. **Revisar código línea por línea**
2. **Verificar:**
   - ✅ El código funciona correctamente
   - ✅ Hay pruebas adecuadas
   - ✅ La documentación es clara
   - ✅ No hay código duplicado
   - ✅ Los nombres de variables son descriptivos

3. **Dejar comentarios constructivos:**

```markdown
# 👍 Comentario positivo
¡Excelente implementación de la fórmula de Bohr!

# 🤔 Sugerencia
Podrías añadir validación para n > 0 aquí.

# ❗ Problema crítico
Esta función no maneja el caso cuando Z = 0, lo que causará división por cero.
```

4. **Aprobar o solicitar cambios:**
   - Si todo está bien: "Approve"
   - Si hay problemas menores: "Comment"
   - Si hay problemas serios: "Request changes"

---

## Resolución de Conflictos

### Escenario común: Dos personas editan el mismo archivo

**Integrante A y B editan `bohr_atom.py`**

```bash
# Cuando intentas hacer merge
git merge main

# Si hay conflicto, verás:
Auto-merging bohr_atom/bohr_atom.py
CONFLICT (content): Merge conflict in bohr_atom/bohr_atom.py
```

**Resolver manualmente:**

```python
# El archivo se verá así:
<<<<<<< HEAD
    def energy_level(self, n):
        # Tu versión
        return -self.Z**2 * RYDBERG / n**2
=======
    def energy_level(self, n):
        # Versión de main
        return -(self.Z**2 * pc.Ry) / (n**2)
>>>>>>> main
```

**Pasos para resolver:**

1. Edita el archivo manualmente
2. Elimina los marcadores `<<<<<<<`, `=======`, `>>>>>>>`
3. Mantén la mejor versión o combina ambas
4. Guarda el archivo

```bash
git add bohr_atom/bohr_atom.py
git commit -m "Resolver conflicto en energy_level"
git push origin tu-rama
```

---

## Comunicación del Equipo

### Reuniones Semanales (Sincrónicas)

**Reunión 1 (Semana 1):**
- Agenda:
  - Dividir tareas
  - Configurar repositorio
  - Acordar convenciones de código
  - Establecer horarios de disponibilidad

**Reunión 2 (Semana 2):**
- Agenda:
  - Revisar avances
  - Resolver dudas técnicas
  - Planificar integración
  - Resolver conflictos

**Reunión 3 (Semana 3):**
- Agenda:
  - Revisar pruebas completas
  - Planificar publicación
  - Distribuir tareas finales

**Reunión 4 (Semana 4):**
- Agenda:
  - Verificar publicación
  - Preparar presentación
  - Celebrar logros 🎉

### Comunicación Diaria (Asincrónica)

**Canal de Discord/Slack/WhatsApp:**

```
📅 Standup diario (cada mañana):
[Nombre]: 
- Ayer: Implementé cálculo de energía
- Hoy: Voy a añadir pruebas unitarias
- Bloqueado: Ninguno / Necesito ayuda con X
```

### Documentar Decisiones

Crear archivo `DECISIONS.md` en el repo:

```markdown
# Decisiones del Equipo

## 2025-09-30: Nombre del paquete
**Decisión:** Usar "bohr-atom" en lugar de "bohr_hydrogen"
**Razón:** Más general, permite extensiones futuras
**Votación:** Unánime

## 2025-10-02: Unidades por defecto
**Decisión:** Métodos principales retornan SI, métodos auxiliares otras unidades
**Razón:** Consistencia científica
**Acordado por:** Todos
```

---

## Convenciones de Código

### Estilo Python (PEP 8)

```python
# ✅ CORRECTO
def energy_level(self, n):
    """
    Calcula la energía del nivel n.
    
    Parameters
    ----------
    n : int
        Número cuántico principal
    
    Returns
    -------
    float
        Energía en Joules
    """
    if n < 1:
        raise ValueError("n debe ser mayor o igual a 1")
    
    return -(self.Z**2 * pc.Ry) / (n**2)


# ❌ INCORRECTO
def energyLevel(self,n):  # CamelCase, sin espacio después de coma
    if n<1:  # Sin espacios alrededor de operador
        raise ValueError("error")  # Mensaje no descriptivo
    return -self.Z**2*pc.Ry/n**2  # Sin paréntesis, difícil de leer
```

### Nombres de Variables

```python
# ✅ CORRECTO
wavelength_nm = 656.3  # Descriptivo, incluye unidad
delta_E = E_final - E_initial

# ❌ INCORRECTO
wl = 656.3  # Muy corto
x = E_final - E_initial  # No descriptivo
```

### Commits

```bash
# ✅ CORRECTO
git commit -m "Implementar cálculo de energía con validación"
git commit -m "Corregir error en transition_wavelength para Z>1"
git commit -m "Añadir pruebas para orbital_radius"

# ❌ INCORRECTO
git commit -m "fix"
git commit -m "cambios"
git commit -m "asdf"
```

### Mensajes de Commit (Convención)

```
tipo(alcance): descripción breve

[cuerpo opcional con más detalles]

[footer opcional con issues relacionados]
```

**Tipos:**
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Documentación
- `test`: Añadir/modificar pruebas
- `refactor`: Refactorización sin cambiar funcionalidad
- `style`: Cambios de formato (espacios, etc.)

**Ejemplos:**

```bash
git commit -m "feat(energia): implementar energy_level_eV"
git commit -m "fix(transicion): corregir cálculo de longitud de onda"
git commit -m "docs(readme): añadir ejemplos de uso"
git commit -m "test(energia): añadir pruebas para Z>1"
```

---

## Herramientas Recomendadas

### Code Quality

```bash
# Formatear código automáticamente
pip install black
black bohr_atom/

# Verificar estilo
pip install flake8
flake8 bohr_atom/

# Type checking (opcional)
pip install mypy
mypy bohr_atom/
```

### Pre-commit Hooks

Crear `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
  
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

```bash
pip install pre-commit
pre-commit install
```

---

## Roles Opcionales del Equipo

### Líder Técnico
- Revisa todos los PRs finales
- Resuelve decisiones técnicas
- Coordina integraciones

### Responsable de Documentación
- Mantiene README actualizado
- Revisa docstrings
- Crea ejemplos

### Responsable de Testing
- Monitorea cobertura
- Asegura calidad de pruebas
- Ejecuta tests antes de merges

**Nota:** En equipos de 3, estas responsabilidades se rotan o comparten.

---

## Checklist por Fase

### ✅ Fase 1: Setup (Día 1-2)
- [ ] Repositorio creado en GitHub
- [ ] Todos los integrantes tienen acceso
- [ ] Estructura de directorios creada
- [ ] Archivos básicos creados
- [ ] Entornos virtuales configurados
- [ ] Primera reunión completada

### ✅ Fase 2: Desarrollo (Semana 1-2)
- [ ] Todas las ramas creadas
- [ ] Código implementado en cada rama
- [ ] Pruebas escritas
- [ ] Commits regulares (min 1/día)
- [ ] PRs creados

### ✅ Fase 3: Integración (Semana 2-3)
- [ ] Todos los PRs revisados
- [ ] PRs fusionados a main
- [ ] Conflictos resueltos
- [ ] Suite completa de pruebas pasa
- [ ] Cobertura >80%

### ✅ Fase 4: Publicación (Semana 3-4)
- [ ] pyproject.toml completo
- [ ] README finalizado
- [ ] Paquete construido
- [ ] Publicado en TestPyPI
- [ ] Publicado en PyPI
- [ ] Instalación verificada

---

## Recursos y Ayuda

### Documentación
- [Git Book](https://git-scm.com/book/en/v2)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Python Packaging](https://packaging.python.org/)
- [pytest](https://docs.pytest.org/)

### Comunidad
- Stack Overflow
- Reddit r/learnpython
- Python Discord

### Plantillas

**Plantilla de Issue:**
```markdown
## Descripción del problema
[Descripción clara del bug o feature]

## Pasos para reproducir (para bugs)
1. 
2. 
3. 

## Comportamiento esperado
[Qué debería pasar]

## Comportamiento actual
[Qué pasa realmente]

## Screenshots
[Si aplica]
```

---

## Celebrar los Logros 🎉

### Hitos a Celebrar

1. **Primer commit de cada integrante** 🎯
2. **Primer PR fusionado** ✅
3. **Todas las pruebas pasan** 🧪
4. **80% de cobertura alcanzado** 📊
5. **Primera construcción exitosa** 📦
6. **Publicado en TestPyPI** 🚀
7. **Publicado en PyPI** 🌟
8. **Primera instalación exitosa** 💯

¡Recuerden documentar el proceso con screenshots y celebrar cada logro del equipo!

---

## Contacto de Emergencia

Si hay problemas críticos que no pueden resolver:

1. Crear un Issue en GitHub con etiqueta "help wanted"
2. Consultar con el profesor/tutor
3. Buscar en Stack Overflow
4. Pedir ayuda en comunidades de Python

**¡Éxito en el proyecto!** 🚀⚛️