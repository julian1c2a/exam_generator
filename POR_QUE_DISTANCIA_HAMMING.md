# 🔍 ¿Por Qué Hamming Se Llama "Distancia"?

**Una justificación matemática rigurosa**

---

## La Respuesta Corta

La función de Hamming $d_H(a,b)$ = "número de posiciones donde a y b difieren" **NO es solo un nombre conveniente**.

Es una **verdadera métrica matemática** — lo que significa que satisface los 3 axiomas formales que definen una distancia en matemáticas.

---

## Los 3 Axiomas (Demostración)

### 1️⃣ No-negatividad y Separabilidad

**Enunciado formal:**
$$d_H(a, b) \geq 0 \text{ para todo par } (a,b)$$
$$d_H(a, b) = 0 \iff a = b$$

**Por qué cumple:**

- $d_H$ *cuenta* el número de posiciones donde a[i] ≠ b[i]
- Contar siempre da un número ≥ 0 ✓
- Si a = b, entonces 0 posiciones difieren, luego $d_H = 0$ ✓
- Si a ≠ b, al menos 1 posición difiere, luego $d_H > 0$ ✓

**Ejemplo:**

```
a = 10110
b = 10110  →  d_H(a,b) = 0  (a = b) ✓

a = 10110
b = 10111  →  d_H(a,b) = 1  (a ≠ b) ✓
```

---

### 2️⃣ Simetría

**Enunciado formal:**
$$d_H(a, b) = d_H(b, a)$$

**Por qué cumple:**

- Si la posición i tiene $a[i] \neq b[i]$, entonces también $b[i] \neq a[i]$
- El *conjunto* de posiciones diferentes es idéntico en ambas direcciones
- Por tanto, el *conteo* es el mismo
- Conmutatividad de la comparación ✓

**Ejemplo:**

```
a = 10110
b = 11110

d_H(a,b): posición 2 difiere (1≠1 NO), posición 1 difiere (0≠1 SÍ) → d=1
d_H(b,a): posición 1 difiere (1≠0 SÍ) → d=1

d_H(a,b) = d_H(b,a) = 1 ✓
```

---

### 3️⃣ Desigualdad Triangular

**Enunciado formal:**
$$d_H(a, c) \leq d_H(a, b) + d_H(b, c)$$

**Interpretación**: "El camino directo nunca es más largo que cualquier camino indirecto"

**Por qué cumple:**

Analicemos cada posición i donde a[i], b[i], c[i] son símbolos.

*Casos posibles en posición i:*

| a[i] | b[i] | c[i] | a[i]=c[i]? | a[i]=b[i]? | b[i]=c[i]? | d_H contribuye |
|------|------|------|-----------|-----------|-----------|---|
| 0 | 0 | 0 | ✓ | ✓ | ✓ | (a,c):0, (a,b):0, (b,c):0 |
| 0 | 0 | 1 | ✗ | ✓ | ✗ | (a,c):1, (a,b):0, (b,c):1 → 1≤0+1 ✓ |
| 0 | 1 | 0 | ✓ | ✗ | ✗ | (a,c):0, (a,b):1, (b,c):1 → 0≤1+1 ✓ |
| 0 | 1 | 1 | ✗ | ✗ | ✓ | (a,c):1, (a,b):1, (b,c):0 → 1≤1+0 ✓ |
| 1 | 0 | 0 | ✗ | ✗ | ✓ | (a,c):1, (a,b):1, (b,c):0 → 1≤1+0 ✓ |
| 1 | 0 | 1 | ✓ | ✗ | ✗ | (a,c):0, (a,b):1, (b,c):1 → 0≤1+1 ✓ |
| 1 | 1 | 0 | ✗ | ✓ | ✗ | (a,c):1, (a,b):0, (b,c):1 → 1≤0+1 ✓ |
| 1 | 1 | 1 | ✓ | ✓ | ✓ | (a,c):0, (a,b):0, (b,c):0 |

**Conclusión**: En cada posición, la contribución a $d_H(a,c)$ nunca excede la suma de contribuciones a $d_H(a,b)$ y $d_H(b,c)$.

Sumando sobre todas las posiciones: ✓ Desigualdad triangular cumplida.

**Ejemplo numérico:**

```
a = 10110
b = 10101
c = 11111

d_H(a,b) = 2 (posiciones 3,5 difieren)
d_H(b,c) = 2 (posiciones 1,3 difieren)
d_H(a,c) = 3 (posiciones 1,3,5 difieren)

Verificar: d_H(a,c) = 3 ≤ 2 + 2 = 4 ✓
```

---

## Consecuencias Teóricas

Al satisfacer estos 3 axiomas, la función de Hamming define un **ESPACIO MÉTRICO**.

Esto habilita:

### 1. **Topología Matemática**

- Concepto de "bola abierta": $B_r(p) = \{w : d_H(w, p) < r\}$
- Concepto de "vecindario": ¿Qué códigos están "cerca"?
- Convergencia y límites en secuencias de palabras

### 2. **Análisis Geométrico**

- Tratamos palabras-código como puntos en un espacio
- La distancia Hamming es la métrica natural de ese espacio
- "Distancia mínima" de un código = radio mínimo de la bola más pequeña alrededor de un código

### 3. **Teoría de Códigos Correctores**

- **Capacidad correctora**: Un código con $d_{min} = 2t+1$ puede corregir $t$ errores
- **Capacidad detectora**: Puede detectar $d_{min}-1$ errores
- **Hamming bound**: Cota teórica máxima de eficiencia

### 4. **Algoritmos de Optimización**

- Búsqueda de códigos óptimos usa conceptos de "distancia mínima"
- Programación dinámica y algoritmos greedy se basan en métrica
- Análisis de complejidad depende de propiedades métricas

---

## Comparación: Hamming vs Medidas Ad-Hoc

| Aspecto | Medida Ad-Hoc | Distancia Hamming |
|--------|---------------|------------------|
| ¿Axiomas verificados? | Tal vez, quizás | ✅ SÍ (3/3) |
| ¿Teoría disponible? | Limitada | ✅ Teoría de métricas |
| ¿Garantías matemáticas? | Ninguna | ✅ Propiedades formales |
| ¿Análisis riguroso posible? | Difícil | ✅ Sí |
| ¿Nombre justificado? | "Parecería" | ✅ Probado |

---

## Reflexión Final

**¿Por qué importa que sea una "distancia"?**

Si fuera solo una medida arbitraria (sin cumplir axiomas), tendríamos un número, pero **no la seguridad de que los análisis basados en ese número sean válidos**.

Al ser una verdadera métrica:

- Podemos usar teoremas topológicos
- Podemos confiar en cotas teóricas
- Podemos construir algoritmos con garantías matemáticas
- Podemos justificar por qué un código es "óptimo"

**Eso es lo que significa llamarla "distancia" Hamming de verdad.**

---

## Lectura Adicional

Ver en el código:

- [core/sistemas_numeracion_basicos.py](core/sistemas_numeracion_basicos.py#L1) - Implementación de `distancia_hamming()`
- [tests/test_hamming_lenguaje.py](tests/test_hamming_lenguaje.py) - Tests de las 3 propiedades

Ver en documentación:

- [CONTENIDOS_FE.md § 2.1.1.6.1.8](../CONTENIDOS_FE.md#2.1.1.6) - Teoría completa
- [ROADMAP_Y_CATALOGO.md](ROADMAP_Y_CATALOGO.md#L50) - Justificación ampliada
