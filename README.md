# Sitio de clases María Cano 2026-02

Material de clase de la **Fundación Universitaria María Cano**, Facultad de Ingeniería, programa de
Ingeniería de Software, semestre 2026-02. Docente: Oscar Leonel Sánchez Conde.

Sitio publicado: <https://oscarleosanchez.github.io/sitio-maria-cano-2026-02/>

Cada estudiante recibe el enlace directo de su curso, no el de la portada:

- Telemática para IoT (TPI01):
  <https://oscarleosanchez.github.io/sitio-maria-cano-2026-02/telematica-iot/>

El sitio no tiene barra de navegación superior a propósito. Cada curso navega por su propia barra
lateral y ninguna página de curso enlaza a la portada.

## Cómo se construye

El sitio se genera con [Quarto](https://quarto.org). Los fuentes son los archivos `.qmd` y la
carpeta `docs/` guarda el HTML renderizado, que es lo que sirve GitHub Pages.

```powershell
quarto render          # regenera docs/
quarto preview         # servidor local con recarga automática
```

Cierra el preview antes de correr `quarto render`. Si lo dejas abierto, el render falla al intentar
recrear `docs/` porque el proceso mantiene la carpeta ocupada. Lo mismo pasa con una pestaña del
navegador apuntando a la copia local.

## Estructura

```
_quarto.yml                    Configuración del sitio: barras laterales, tema, formato
estilos/estilo.scss            Tema visual compartido por todas las guías
estilos/favicon.svg
index.qmd                      Portada con las tarjetas de los cursos
telematica-iot/index.qmd       Presentación, unidades y evaluación del curso
telematica-iot/semana-NN/      Una carpeta por semana: la guía y sus imágenes
docs/                          Salida renderizada. GitHub Pages publica desde aquí
```

Cada semana vive en su propia carpeta con las imágenes al lado de la guía que las usa.

## Agregar un curso nuevo

1. Crea `<curso>/index.qmd` con la presentación.
2. Agrega un bloque `sidebar` con `id: <curso>` en `_quarto.yml`.
3. Agrega la tarjeta del curso en `index.qmd`.

La portada usa una grilla que se reacomoda sola, así que no hay que tocar los estilos.

## Publicar una semana nueva

```powershell
quarto render
git add -A
git commit -m "Semana NN de Telemática"
git push
```

GitHub Pages actualiza el sitio en menos de un minuto.

## Diagramas

Los diagramas son **SVG escrito a mano dentro del propio `.qmd`**, envuelto en
`::: {.diagrama}`. Se editan como texto, no hay archivos de imagen que mantener y el resultado
imprime bien en el PDF.

La paleta sale de `estilos/estilo.scss`: relleno `#eef4fa` con borde `#c7d6e6` para las cajas
normales, `#e4f2f1` con borde `#8fc9c5` para la caja destacada de cada diagrama, texto `#12324f`
y secundario `#5b6876`, conectores `#8fb3d1`.

Reglas para que un diagrama nuevo encaje:

- Fija el tipo con `font-family` en el elemento `<svg>` y hereda tamaño y color desde grupos `<g>`.
  Nada de `<style>` dentro del SVG: en HTML esos estilos son globales y se filtran a toda la página.
- Los `id` de los `marker` deben ser únicos en toda la página, porque todos los SVG comparten el
  mismo DOM. La convención es `pf1`, `pf2` y así.
- El `viewBox` va sobre 760 unidades de ancho como máximo, con textos entre 11 y 17 unidades.
- `.diagrama` fija `min-width: 470px` y desplaza en horizontal en pantallas angostas, en vez de
  encoger el texto hasta que no se lee.

Mermaid se probó primero y se descartó: con este tema los `subgraph` salen con relleno azul oscuro
y el texto encima queda ilegible, y el control tipográfico es mucho menor.

## Convenciones de escritura

- Nombres de archivo sin tildes, sin eñes y sin espacios. El contenido sí lleva tildes.
- Nada de raya larga, punto medio, comillas tipográficas ni flechas. Solo ASCII, más las tildes y
  la eñe del español.
- Numeración de semanas a dos dígitos: `semana-01`, nunca `semana-1`.
- El encabezado YAML de cada guía es corto: `title`, `author`, `date` y `date-format`. El formato
  lo hereda del `_quarto.yml`.

## Qué no vive aquí

Este repositorio es público. Los planes de sesión, los enunciados, las rúbricas y las soluciones
quedan fuera de él, en el taller privado del docente, y se reparten por otra vía.

## Configuración de GitHub Pages

Settings, Pages, Source: **Deploy from a branch**, rama `main`, carpeta `/docs`.

El archivo `docs/.nojekyll` es necesario: sin él GitHub procesa el sitio con Jekyll y descarta las
carpetas que empiezan con guion bajo, que es donde Quarto pone estilos y scripts. Va declarado como
recurso en `_quarto.yml` porque cada render recrea `docs/` desde cero.
