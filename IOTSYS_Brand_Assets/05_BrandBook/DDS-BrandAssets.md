# DOCUMENT DESIGN SYSTEM (DDS)
## DDS-BrandAssets-001: IOTSYS Brand Assets Architecture v1.0
**Estado:** OFICIAL / BLOQUEADO (FREEZE)  
**Custodio de Marca:** Fredy Custodio  
**Fecha de Emisión:** Agosto 2026  
**Organización:** IOTSYS Sistemas Inteligentes  

---

## 1. OBJETIVO DEL SISTEMA
El presente documento constituye la especificación canónica y vinculante que gobierna la arquitectura, construcción vectorial, exportación, jerarquía, paletas cromáticas y custodia técnica del paquete corporativo **IOTSYS Brand Assets v1.0**.

Este sistema garantiza:
1. **Consistencia Absoluta:** Rendimiento idéntico en micro-formatos (favicons 16px, serigrafía en PCBs de microcontroladores) y macro-formatos (cartelería industrial, rotulación vehicular, señalética arquitectónica).
2. **Inmutabilidad y Gobierno:** Protección legal y técnica de los activos vectoriales primarios contra modificaciones no autorizadas.
3. **Compatibilidad Multiplataforma:** Interoperabilidad nativa con herramientas de diseño (Adobe Illustrator, Inkscape, Figma, CorelDraw) y motores web/móvil (SVG puro, CSS Variables, Apple Touch Icon, Android Chrome PWA).

---

## 2. ESTRUCTURA DEL PAQUETE DISTRIBUIDO

```
IOTSYS_Brand_Assets/
├── 01_Master/
│   ├── Logo_Principal.svg          # Master vectorial con nodos optimizados
│   ├── Logo_Principal.ai           # Archivo Adobe Illustrator CC nativo
│   ├── Logo_Principal.eps          # Encapsulated PostScript 3.0 para imprenta
│   └── Logo_Principal.pdf          # Vector PDF de alta precisión (DPI infinito)
├── 02_Logos/
│   ├── Logo_Horizontal.svg         # Variante apaisada para headers y web
│   ├── Logo_Vertical.svg           # Variante vertical / estandarte
│   ├── Logo_Isotipo.svg            # Isotipo independiente (3 cintas Cyan, 2 Navy)
│   ├── Logo_Blanco.svg             # Versión monocromática negativa (#FFFFFF)
│   ├── Logo_Negro.svg              # Versión monocromática negra (#000000)
│   └── Logo_Monocromatico.svg      # Versión monocromática Azul Profundo (#01325D)
├── 03_PNG/
│   ├── 2048/                       # Ultra-High Resolution (4K Displays, gigantografías)
│   ├── 1024/                       # High Resolution (Presentaciones, docks)
│   ├── 512/                        # Medium Resolution (Avatares, tarjetas)
│   ├── 256/                        # Standard Resolution (Miniaturas UI)
│   └── 128/                        # Low Resolution (Iconos de lista)
├── 04_Web/
│   ├── favicon.ico                 # Multi-layer ICO (16, 32, 48, 64, 128, 256 px)
│   ├── favicon.svg                 # Vector SVG Favicon moderno
│   ├── apple-touch-icon.png        # Icono iOS Web Clip (180x180 px)
│   ├── android-chrome-192.png      # PWA Icon Standard (192x192 px)
│   └── android-chrome-512.png      # PWA Splash Icon (512x512 px)
├── 05_BrandBook/
│   ├── BrandBook.pdf               # Manual de Identidad Corporativa Maestro (25-40 pp)
│   └── DDS-BrandAssets.md          # Especificación DDS y Custodia (Este documento)
└── 06_ColorPalette/
    ├── palette.css                 # CSS Custom Properties (:root design tokens)
    ├── palette.gpl                 # Paleta GIMP / Inkscape
    ├── palette.ase                 # Adobe Swatch Exchange binario
    └── palette.json                # Estructura JSON para pipelines frontend
```

---

## 3. ESPECIFICACIÓN GEOMÉTRICA Y VECTORIAL

### 3.1 Anatomía del Isotipo
El isotipo está conformado por exactamente **5 cintas vectoriales estilizadas** que forman un bucle helicoidal dinámico en forma de "S" tecnológica:
- **3 Cintas Superiores / Frontales:** Acabado en *Cyan Tecnológico* (`#04C1CF`), simbolizando innovación continua, conectividad en tiempo real y flujo de datos IoT.
- **2 Cintas Inferiores / Estructurales:** Acabado en *Azul Profundo* (`#01325D`), simbolizando la base sólida de ingeniería, infraestructura perimetral, firmware e inteligencia distribuida.
- **Topología de Curvas:** Construido exclusivamente mediante curvas de Bézier cúbicas con puntos de control tangenciales limpios. Sin nodos redundantes, sin micro-segmentos rotos.

### 3.2 Tipografía Corporativa Oficial
- **Logotipo Primario (`IOTSYS`):** *Noto Sans / Montserrat Ultra-Bold*. Caracteres monolíticos con proporción geométrica y peso visual balanceado.
- **Subtítulo Descriptivo (`SISTEMAS INTELIGENTES`):** *Noto Sans Semi-Bold / Medium* en caja alta con tracking expandido (+350 milésimas de em) para asegurar legibilidad en tamaños reducidos.

---

## 4. SISTEMA CROMÁTICO OFICIAL

| Denominación | HEX | RGB | CMYK | Pantone | Rol de Marca |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Azul Profundo** | `#01325D` | `1, 50, 93` | `99, 46, 0, 64` | Pantone 2955 C | Corporativo Primario |
| **Cyan Tecnológico** | `#04C1CF` | `4, 193, 207` | `98, 7, 0, 19` | Pantone 3115 C | Acento Tecnológico / IoT |
| **Celeste Medio** | `#66B6C0` | `102, 182, 192` | `47, 5, 0, 25` | Pantone 549 C | Soporte y Gráficos UI |
| **Acento Claro** | `#C1F2F6` | `193, 242, 246` | `22, 2, 0, 4` | Pantone 635 C | Fondos y Contenedores Suaves |
| **Blanco Puro** | `#FFFFFF` | `255, 255, 255` | `0, 0, 0, 0` | Opaque White | Fondos y Aplicaciones Invertidas |
| **Gris Grafito** | `#334155` | `51, 65, 85` | `40, 24, 0, 67` | Pantone 432 C | Texto Secundario y Bordes |

---

## 5. REGLAS DE GOBIERNO DE IDENTIDAD CORPORATIVA

> ### POLÍTICA OFICIAL VINCULANTE:
> *"El isotipo y logotipo oficial de IOTSYS constituye un activo estratégico de la organización.*
> 
> *No podrá modificarse su geometría, proporciones, composición, colores o tipografía sin autorización expresa del Arquitecto Corporativo y Custodio de Marca.*
> 
> *Toda modificación deberá generar una nueva versión controlada y documentada de los Brand Assets dentro del sistema DDS."*

### Restricciones Inmutables (Prohibiciones):
- ❌ **Prohibido distorsionar:** No estirar, comprimir ni sesgar la relación de aspecto bajo ninguna circunstancia.
- ❌ **Prohibido aplicar gradientes no oficiales:** No sustituir los colores planos por gradientes, brillos, sombras paralelas o biselados 3D.
- ❌ **Prohibido recolorear arbitrariamente:** No utilizar colores fuera de la paleta oficial (HEX `#01325D`, `#04C1CF`, `#66B6C0`, `#C1F2F6`, `#FFFFFF`, `#000000`).
- ❌ **Prohibido rotar elementos aislados:** No inclinar el isotipo con respecto al texto ni alterar el ángulo intrínseco de las cintas.
- ❌ **Prohibido sustituir tipografías:** No reescribir `IOTSYS` con fuentes serif, manuscritas o de fantasía.

---

## 6. CONTROL DE VERSIONES Y AUDITORÍA

| Versión | Fecha | Autor / Custodio | Descripción del Cambio | Estado |
| :--- | :--- | :--- | :--- | :--- |
| **v0.1** | 2026-08-10 | Fredy Custodio | Evaluación de imagotipo preliminar "IS". | Obsoleto |
| **v0.9** | 2026-08-12 | Fredy Custodio | Vectorización matemática preliminar y congelamiento conceptual. | Aprobado |
| **v1.0** | 2026-08-17 | Fredy Custodio | **Entrega Maestra Oficial.** Paquete completo de Brand Assets, Master SVGs, PNGs multirresolución, Web Icons, Paletas ASE/GPL/CSS y Brand Book PDF. | **OFICIAL / CONGELADO** |
