from django.core.management.base import BaseCommand
from morfosintaxis.models import Leccion, Ejercicio

class Command(BaseCommand):
    help = 'Carga 20 lecciones de ejemplo con ejercicios'
    
    def handle(self, *args, **kwargs):
        lecciones_data = [
            # NIVEL BÁSICO
            {
                'numero': 1,
                'titulo': 'El Sustantivo',
                'nivel': 'basico',
                'descripcion': 'Introducción a los sustantivos y sus clasificaciones',
                'teoria': '''El sustantivo es la palabra que sirve para nombrar personas, animales, cosas, ideas o sentimientos.

Clasificación de sustantivos:
- Común: nombra de forma general (libro, perro, ciudad)
- Propio: nombra de forma particular (María, Madrid, Amazonas)
- Concreto: se puede percibir por los sentidos (mesa, árbol, agua)
- Abstracto: no se puede percibir por los sentidos (amor, libertad, tristeza)
- Individual: nombra un solo ser (soldado, oveja, alumno)
- Colectivo: nombra un conjunto (ejército, rebaño, alumnado)''',
                'ejemplos': '''1. El libro está sobre la mesa. (libro, mesa = sustantivos comunes concretos)
2. María vive en Barcelona. (María, Barcelona = sustantivos propios)
3. La felicidad es importante para todos. (felicidad = sustantivo abstracto)
4. El rebaño pasta en el campo. (rebaño = sustantivo colectivo)
5. Mi hermano estudia medicina. (hermano = sustantivo común individual)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica el sustantivo en: "El perro ladra fuerte"',
                        'opciones': ['El', 'perro', 'ladra', 'fuerte'],
                        'respuesta_correcta': 'perro',
                        'explicacion': '¡Correcto! "Perro" es un sustantivo común que nombra un animal.',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿Qué tipo de sustantivo es "ejército"?',
                        'opciones': ['Individual', 'Colectivo', 'Propio', 'Abstracto'],
                        'respuesta_correcta': 'Colectivo',
                        'explicacion': '¡Exacto! "Ejército" es un sustantivo colectivo porque nombra un conjunto de soldados.',
                        'puntos': 1
                    },
                    {
                        'numero': 3,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Señala el sustantivo abstracto:',
                        'opciones': ['Mesa', 'Amor', 'Perro', 'Madrid'],
                        'respuesta_correcta': 'Amor',
                        'explicacion': 'Correcto. "Amor" es abstracto porque no se puede percibir con los sentidos.',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 2,
                'titulo': 'El Artículo',
                'nivel': 'basico',
                'descripcion': 'Los artículos determinados e indeterminados',
                'teoria': '''El artículo es una palabra que acompaña al sustantivo y concuerda con él en género y número.

Artículos determinados: Se refieren a algo conocido o específico
- Masculino singular: el
- Femenino singular: la
- Masculino plural: los
- Femenino plural: las

Artículos indeterminados: Se refieren a algo desconocido o no específico
- Masculino singular: un
- Femenino singular: una
- Masculino plural: unos
- Femenino plural: unas

Artículo neutro: lo (se usa con adjetivos sustantivados)''',
                'ejemplos': '''1. El libro está en la mesa. (artículos determinados: el, la)
2. Vi un perro en el parque. (un = indeterminado, el = determinado)
3. Las niñas juegan con los niños. (artículos determinados plurales)
4. Unos amigos llegaron ayer. (artículo indeterminado plural)
5. Lo importante es participar. (artículo neutro)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿Qué tipo de artículo es "un" en: "Vi un gato"?',
                        'opciones': ['Determinado', 'Indeterminado', 'Neutro', 'No hay artículo'],
                        'respuesta_correcta': 'Indeterminado',
                        'explicacion': '¡Correcto! "Un" es un artículo indeterminado que se refiere a un gato no específico.',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Completa: "___ flores son hermosas"',
                        'opciones': ['El', 'La', 'Las', 'Los'],
                        'respuesta_correcta': 'Las',
                        'explicacion': 'Perfecto. "Las" es el artículo determinado femenino plural que concuerda con "flores".',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 3,
                'titulo': 'El Adjetivo Calificativo',
                'nivel': 'basico',
                'descripcion': 'Palabras que califican o determinan al sustantivo',
                'teoria': '''El adjetivo calificativo es la palabra que acompaña al sustantivo para expresar una cualidad o característica.

Características:
- Concuerda en género y número con el sustantivo
- Puede ir antes o después del sustantivo
- Tiene grados: positivo, comparativo, superlativo

Grados del adjetivo:
- Positivo: expresa la cualidad (alto)
- Comparativo: compara dos elementos (más alto que, menos alto que, tan alto como)
- Superlativo: expresa el grado máximo (altísimo, el más alto)''',
                'ejemplos': '''1. La casa grande está vacía. (grande = adjetivo calificativo)
2. Tiene ojos azules. (azules = adjetivo calificativo)
3. Pedro es más alto que Juan. (comparativo)
4. Esta es la película más interesante. (superlativo)
5. Es un excelente profesor. (excelente = adjetivo antepuesto)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica el adjetivo: "El coche rojo es rápido"',
                        'opciones': ['coche', 'rojo', 'es', 'El'],
                        'respuesta_correcta': 'rojo',
                        'explicacion': '¡Bien! "Rojo" califica al sustantivo "coche". "Rápido" también es adjetivo.',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿En qué grado está "altísimo"?',
                        'opciones': ['Positivo', 'Comparativo', 'Superlativo', 'Ninguno'],
                        'respuesta_correcta': 'Superlativo',
                        'explicacion': 'Correcto. "Altísimo" es el grado superlativo de "alto".',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 4,
                'titulo': 'Los Pronombres Personales',
                'nivel': 'basico',
                'descripcion': 'Palabras que sustituyen al nombre',
                'teoria': '''Los pronombres personales son palabras que sustituyen al sustantivo y designan a las personas gramaticales.

Pronombres personales sujeto:
- 1ª persona: yo (singular), nosotros/nosotras (plural)
- 2ª persona: tú, usted (singular), vosotros/vosotras, ustedes (plural)
- 3ª persona: él, ella (singular), ellos, ellas (plural)

Pronombres átonos (sin acento):
- me, te, se, lo, la, le, nos, os, los, las, les

Pronombres tónicos (con preposición):
- mí, ti, sí, conmigo, contigo, consigo''',
                'ejemplos': '''1. Yo estudio español. (yo = pronombre de 1ª persona)
2. Ella me llamó ayer. (ella = 3ª persona, me = átono)
3. ¿Vienes tú conmigo? (tú = 2ª persona, conmigo = tónico)
4. Nosotros lo vimos. (nosotros = 1ª plural, lo = átono)
5. Se lo dije a ellos. (se, lo = átonos, ellos = tónico)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica el pronombre: "Ella estudia mucho"',
                        'opciones': ['Ella', 'estudia', 'mucho', 'No hay pronombre'],
                        'respuesta_correcta': 'Ella',
                        'explicacion': '¡Correcto! "Ella" es un pronombre personal de 3ª persona singular.',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿Qué tipo de pronombre es "me" en "Me gusta"?',
                        'opciones': ['Sujeto', 'Átono', 'Tónico', 'Demostrativo'],
                        'respuesta_correcta': 'Átono',
                        'explicacion': 'Perfecto. "Me" es un pronombre átono (sin acento propio).',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 5,
                'titulo': 'El Verbo: Presente de Indicativo',
                'nivel': 'basico',
                'descripcion': 'Conjugación del tiempo presente',
                'teoria': '''El verbo es la palabra que expresa acción, estado o proceso. El presente de indicativo indica acciones que ocurren en el momento actual o de forma habitual.

Conjugación regular:
- Verbos en -ar: cant-o, cant-as, cant-a, cant-amos, cant-áis, cant-an
- Verbos en -er: com-o, com-es, com-e, com-emos, com-éis, com-en
- Verbos en -ir: viv-o, viv-es, viv-e, viv-imos, viv-ís, viv-en

Usos del presente:
- Acción actual: Ahora como una manzana
- Acción habitual: Todos los días estudio
- Verdad universal: El sol sale por el este''',
                'ejemplos': '''1. Yo canto en el coro. (verbo cantar, 1ª persona)
2. Tú comes muy rápido. (verbo comer, 2ª persona)
3. Ella vive en Madrid. (verbo vivir, 3ª persona)
4. Nosotros estudiamos juntos. (verbo estudiar, 1ª plural)
5. El agua hierve a 100 grados. (verdad universal)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Conjuga "hablar" en 1ª persona singular:',
                        'opciones': ['hablo', 'hablas', 'habla', 'hablamos'],
                        'respuesta_correcta': 'hablo',
                        'explicacion': '¡Exacto! "Hablo" es la conjugación correcta de "hablar" en presente, 1ª persona.',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 6,
                'titulo': 'El Verbo: Pretérito Perfecto Simple',
                'nivel': 'basico',
                'descripcion': 'El pasado simple del español',
                'teoria': '''El pretérito perfecto simple (o pretérito indefinido) expresa acciones pasadas completamente terminadas.

Conjugación regular:
- Verbos en -ar: cant-é, cant-aste, cant-ó, cant-amos, cant-asteis, cant-aron
- Verbos en -er/-ir: com-í/viv-í, com-iste/viv-iste, com-ió/viv-ió, com-imos/viv-imos, com-isteis/viv-isteis, com-ieron/viv-ieron

Marcadores temporales:
- ayer, anoche, la semana pasada, el año pasado, hace dos días''',
                'ejemplos': '''1. Ayer comí pizza. (acción terminada en el pasado)
2. El año pasado viajé a España. (acción puntual pasada)
3. ¿Estudiaste para el examen? (pregunta sobre acción pasada)
4. Ellos llegaron tarde. (acción completada)
5. La película empezó a las 8. (acción específica del pasado)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Completa: "Ayer yo ___ al cine"',
                        'opciones': ['voy', 'fui', 'iré', 'iba'],
                        'respuesta_correcta': 'fui',
                        'explicacion': 'Correcto. "Fui" es el pretérito perfecto simple de "ir".',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 7,
                'titulo': 'El Verbo: Futuro Simple',
                'nivel': 'basico',
                'descripcion': 'Expresar acciones futuras',
                'teoria': '''El futuro simple expresa acciones que ocurrirán después del momento presente.

Conjugación regular (se añade al infinitivo):
- cant-aré, cant-arás, cant-ará, cant-aremos, cant-aréis, cant-arán
- com-eré, com-erás, com-erá, com-eremos, com-eréis, com-erán
- viv-iré, viv-irás, viv-irá, viv-iremos, viv-iréis, viv-irán

Usos:
- Acción futura: Mañana estudiaré
- Probabilidad en presente: Serán las tres (probablemente son las tres)
- Mandato: No matarás''',
                'ejemplos': '''1. Mañana viajaré a Barcelona.
2. El próximo año terminaré la universidad.
3. ¿Vendrás a mi fiesta?
4. Serán las cinco de la tarde. (probabilidad)
5. Algún día comprenderás. (futuro lejano)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Conjuga "estudiar" en futuro, 1ª persona:',
                        'opciones': ['estudio', 'estudiaba', 'estudiaré', 'he estudiado'],
                        'respuesta_correcta': 'estudiaré',
                        'explicacion': '¡Perfecto! "Estudiaré" es el futuro simple de "estudiar".',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 8,
                'titulo': 'Las Preposiciones',
                'nivel': 'basico',
                'descripcion': 'Palabras que relacionan elementos',
                'teoria': '''Las preposiciones son palabras invariables que relacionan palabras o grupos de palabras.

Preposiciones simples:
a, ante, bajo, cabe, con, contra, de, desde, durante, en, entre, hacia, hasta, mediante, para, por, según, sin, so, sobre, tras, versus, vía

Preposiciones más comunes:
- a: dirección, tiempo (Voy a casa)
- de: procedencia, materia (Vengo de Madrid, mesa de madera)
- en: lugar, tiempo (Estoy en casa, en verano)
- con: compañía, instrumento (Voy con María, escribo con lápiz)
- para: finalidad, destinatario (Estudio para aprender)
- por: causa, medio (Lo hago por ti, hablo por teléfono)''',
                'ejemplos': '''1. Voy a la escuela. (dirección)
2. El libro es de Juan. (posesión)
3. Estudio en la biblioteca. (lugar)
4. Salgo con mis amigos. (compañía)
5. Este regalo es para ti. (destinatario)
6. Lo hice por amor. (causa)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica la preposición: "Voy a casa"',
                        'opciones': ['Voy', 'a', 'casa', 'No hay preposición'],
                        'respuesta_correcta': 'a',
                        'explicacion': '¡Correcto! "A" es una preposición que indica dirección.',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 9,
                'titulo': 'Las Conjunciones',
                'nivel': 'basico',
                'descripcion': 'Palabras que unen oraciones o elementos',
                'teoria': '''Las conjunciones son palabras invariables que unen palabras, sintagmas u oraciones.

Tipos de conjunciones:
- Copulativas (suman): y, e, ni
- Disyuntivas (opción): o, u
- Adversativas (oposición): pero, mas, sino, aunque
- Causales (causa): porque, pues, ya que
- Consecutivas (consecuencia): luego, por lo tanto, así que
- Condicionales (condición): si
- Concesivas (concesión): aunque''',
                'ejemplos': '''1. Juan y María estudian. (copulativa)
2. ¿Vienes o te quedas? (disyuntiva)
3. Estudié pero no aprobé. (adversativa)
4. No vino porque estaba enfermo. (causal)
5. Llueve, así que lleva paraguas. (consecutiva)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿Qué tipo de conjunción es "pero"?',
                        'opciones': ['Copulativa', 'Disyuntiva', 'Adversativa', 'Causal'],
                        'respuesta_correcta': 'Adversativa',
                        'explicacion': 'Exacto. "Pero" es una conjunción adversativa que expresa oposición.',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 10,
                'titulo': 'La Oración Simple',
                'nivel': 'basico',
                'descripcion': 'Estructura básica: sujeto y predicado',
                'teoria': '''La oración simple tiene un solo verbo conjugado y se compone de:

SUJETO: Quién realiza la acción (puede estar omitido)
- Núcleo: sustantivo o pronombre
- Modificadores: artículos, adjetivos

PREDICADO: Lo que se dice del sujeto
- Núcleo: verbo
- Complementos: directos, indirectos, circunstanciales

Tipos de oraciones según el sujeto:
- Sujeto explícito: El niño corre
- Sujeto omitido: Corro (yo)
- Sujeto indeterminado: Llaman a la puerta

Tipos según la actitud del hablante:
- Enunciativas: afirman o niegan
- Interrogativas: preguntan
- Exclamativas: expresan emoción
- Imperativas: ordenan o piden''',
                'ejemplos': '''1. El perro ladra. (Sujeto: el perro / Predicado: ladra)
2. María estudia matemáticas. (Sujeto: María / Predicado: estudia matemáticas)
3. Los niños juegan en el parque. (Sujeto: los niños / Predicado: juegan en el parque)
4. Comí pizza. (Sujeto omitido: yo / Predicado: comí pizza)
5. Llueve mucho. (Oración impersonal, sin sujeto)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica el sujeto: "Los estudiantes leen libros"',
                        'opciones': ['Los', 'estudiantes', 'Los estudiantes', 'libros'],
                        'respuesta_correcta': 'Los estudiantes',
                        'explicacion': '¡Perfecto! "Los estudiantes" es el sujeto completo de la oración.',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': 'En "Corro rápido", el sujeto es:',
                        'opciones': ['Corro', 'rápido', 'yo (omitido)', 'No hay sujeto'],
                        'respuesta_correcta': 'yo (omitido)',
                        'explicacion': 'Correcto. El sujeto "yo" está omitido pero se entiende por la conjugación.',
                        'puntos': 1
                    }
                ]
            },
            
            # NIVEL INTERMEDIO
            {
                'numero': 11,
                'titulo': 'El Complemento Directo (CD)',
                'nivel': 'intermedio',
                'descripcion': 'Objeto que recibe directamente la acción del verbo',
                'teoria': '''El Complemento Directo (CD) es la función sintáctica que recibe directamente la acción del verbo.

Características:
- Responde a las preguntas: ¿qué? o ¿a quién?
- Se puede sustituir por los pronombres: lo, la, los, las
- Con verbos transitivos (necesitan CD para completar su significado)
- Cuando es persona, lleva la preposición "a"

Pruebas para identificarlo:
1. Pregunta: ¿Qué + verbo? o ¿A quién + verbo?
2. Sustitución: lo, la, los, las
3. Conversión a pasiva: el CD se convierte en sujeto paciente''',
                'ejemplos': '''1. Compré un libro. (¿Qué compré? → un libro = CD)
   → Lo compré. (sustitución por "lo")

2. Vi a María. (¿A quién vi? → a María = CD)
   → La vi. (sustitución por "la")

3. Los niños comen manzanas. (¿Qué comen? → manzanas = CD)
   → Los niños las comen.

4. Escribí una carta. (¿Qué escribí? → una carta = CD)
   → La escribí.

5. El profesor explicó la lección. (¿Qué explicó? → la lección = CD)
   → El profesor la explicó.''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica el CD: "Juan compró flores"',
                        'opciones': ['Juan', 'compró', 'flores', 'No hay CD'],
                        'respuesta_correcta': 'flores',
                        'explicacion': '¡Correcto! "Flores" es el CD (¿Qué compró Juan? → flores). Se puede sustituir: Juan las compró.',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Sustituye el CD por pronombre: "Leí el periódico"',
                        'opciones': ['Le leí', 'Lo leí', 'La leí', 'Los leí'],
                        'respuesta_correcta': 'Lo leí',
                        'explicacion': 'Perfecto. "El periódico" (masculino singular) se sustituye por "lo".',
                        'puntos': 1
                    },
                    {
                        'numero': 3,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿Cuál tiene CD?: ',
                        'opciones': ['Llueve mucho', 'Escribí una carta', 'Llegué tarde', 'Estoy cansado'],
                        'respuesta_correcta': 'Escribí una carta',
                        'explicacion': 'Exacto. "Una carta" es CD (¿Qué escribí?). Las demás son intransitivas o atributivas.',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 12,
                'titulo': 'El Complemento Indirecto (CI)',
                'nivel': 'intermedio',
                'descripcion': 'Destinatario o beneficiario de la acción',
                'teoria': '''El Complemento Indirecto (CI) indica el destinatario o beneficiario de la acción verbal.

Características:
- Responde a las preguntas: ¿a quién? o ¿para quién?
- Siempre lleva la preposición "a" o "para"
- Se puede sustituir por: le, les (singular/plural)
- Puede aparecer junto con el CD en la misma oración
- Compatible con verbos transitivos e intransitivos

Estructura típica:
Sujeto + Verbo + CD + CI
"Juan dio un regalo a María"''',
                'ejemplos': '''1. Di un libro a Pedro. (¿A quién di? → a Pedro = CI)
   → Le di un libro. (sustitución por "le")

2. Compré flores para mi madre. (¿Para quién? → para mi madre = CI)
   → Le compré flores.

3. Escribí una carta a mis padres. (¿A quién? → a mis padres = CI)
   → Les escribí una carta.

4. El profesor explicó la lección a los alumnos. (CI: a los alumnos)
   → El profesor les explicó la lección.

5. Traje regalos para todos. (CI: para todos)
   → Les traje regalos.''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica el CI: "Envié una carta a Juan"',
                        'opciones': ['Envié', 'una carta', 'a Juan', 'No hay CI'],
                        'respuesta_correcta': 'a Juan',
                        'explicacion': '¡Correcto! "A Juan" es el CI (¿A quién envié? → a Juan). "Una carta" es el CD.',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Sustituye el CI: "Compré un regalo a María"',
                        'opciones': ['La compré un regalo', 'Le compré un regalo', 'Lo compré a María', 'Les compré un regalo'],
                        'respuesta_correcta': 'Le compré un regalo',
                        'explicacion': 'Perfecto. "A María" (singular) se sustituye por "le".',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 13,
                'titulo': 'Los Complementos Circunstanciales',
                'nivel': 'intermedio',
                'descripcion': 'Expresan circunstancias de la acción verbal',
                'teoria': '''Los Complementos Circunstanciales (CC) expresan las circunstancias en que se realiza la acción verbal.

Tipos principales:
- CC de Lugar (CCL): ¿dónde? → en casa, aquí, allí
- CC de Tiempo (CCT): ¿cuándo? → ayer, ahora, mañana
- CC de Modo (CCM): ¿cómo? → bien, rápidamente, con cuidado
- CC de Cantidad (CCC): ¿cuánto? → mucho, poco, bastante
- CC de Causa (CCC): ¿por qué? → por enfermedad, debido a
- CC de Finalidad (CCF): ¿para qué? → para estudiar
- CC de Compañía (CCComp): ¿con quién? → con mis amigos
- CC de Instrumento (CCI): ¿con qué? → con un cuchillo''',
                'ejemplos': '''1. Estudio en la biblioteca. (CCL: en la biblioteca)
2. Llegué ayer. (CCT: ayer)
3. Habla despacio. (CCM: despacio)
4. Come mucho. (CCC: mucho)
5. No vine por la lluvia. (CCCausa: por la lluvia)
6. Estudio para aprobar. (CCF: para aprobar)
7. Voy con mi hermano. (CCComp: con mi hermano)
8. Corté el pan con un cuchillo. (CCI: con un cuchillo)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica el tipo de CC: "Llegó ayer"',
                        'opciones': ['Lugar', 'Tiempo', 'Modo', 'Cantidad'],
                        'respuesta_correcta': 'Tiempo',
                        'explicacion': '¡Correcto! "Ayer" es un CC de Tiempo (¿cuándo llegó?).',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿Qué CC es "en el parque"?: "Juegan en el parque"',
                        'opciones': ['Tiempo', 'Lugar', 'Modo', 'Compañía'],
                        'respuesta_correcta': 'Lugar',
                        'explicacion': 'Perfecto. "En el parque" indica dónde juegan (CCL).',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 14,
                'titulo': 'Oraciones Coordinadas',
                'nivel': 'intermedio',
                'descripcion': 'Dos oraciones unidas en el mismo nivel sintáctico',
                'teoria': '''Las oraciones coordinadas son dos o más oraciones simples unidas por conjunciones coordinantes. Cada oración mantiene su independencia sintáctica.

Tipos:
1. Copulativas (suman): y, e, ni
   → Juan estudia y María trabaja.

2. Disyuntivas (opción): o, u
   → ¿Vienes o te quedas?

3. Adversativas (oposición): pero, mas, sino, aunque
   → Estudié pero no aprobé.

4. Distributivas (alternancia): ya...ya, bien...bien, ora...ora
   → Ya ríe, ya llora.

5. Explicativas (aclaración): es decir, o sea, esto es
   → Es tímido, es decir, no habla mucho.''',
                'ejemplos': '''1. Yo cocino y tú lavas. (copulativa)
2. ¿Estudias o trabajas? (disyuntiva)
3. Es inteligente pero vago. (adversativa)
4. Ya canta, ya baila. (distributiva)
5. Es arquitecto, o sea, diseña edificios. (explicativa)
6. No estudia ni trabaja. (copulativa negativa)
7. Llamé mas no contestó. (adversativa)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿Qué tipo es?: "Estudié pero no aprobé"',
                        'opciones': ['Copulativa', 'Disyuntiva', 'Adversativa', 'Explicativa'],
                        'respuesta_correcta': 'Adversativa',
                        'explicacion': '¡Correcto! "Pero" es una conjunción adversativa que expresa oposición.',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 15,
                'titulo': 'Subordinadas Sustantivas',
                'nivel': 'intermedio',
                'descripcion': 'Oraciones que funcionan como un sustantivo',
                'teoria': '''Las oraciones subordinadas sustantivas funcionan como un sustantivo dentro de la oración principal.

Introducidas por:
- "que": Quiero que vengas
- "si": No sé si vendrá
- Interrogativos: Pregunto cuándo llega, dónde vive, quién es
- Infinitivo: Me gusta bailar

Funciones que pueden desempeñar:
1. Sujeto: Me gusta que estudies
2. CD: Quiero que vengas
3. CI: Dio importancia a que llegaras
4. Atributo: La verdad es que no sé
5. CN: Tengo ganas de que llegue
6. CRég: Me acuerdo de que viniste''',
                'ejemplos': '''1. Quiero que vengas. (CD: "que vengas")
2. Me gusta estudiar. (Sujeto: "estudiar")
3. No sé si vendrá. (CD: "si vendrá")
4. Preguntó dónde vivías. (CD: "dónde vivías")
5. Es necesario que estudies. (Sujeto: "que estudies")
6. Tengo miedo de que llueva. (CN: "de que llueva")''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica la subordinada: "Quiero que estudies"',
                        'opciones': ['Quiero', 'que', 'que estudies', 'estudies'],
                        'respuesta_correcta': 'que estudies',
                        'explicacion': '¡Correcto! "Que estudies" es la oración subordinada sustantiva que funciona como CD.',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 16,
                'titulo': 'Subordinadas Adjetivas',
                'nivel': 'intermedio',
                'descripcion': 'Oraciones que funcionan como un adjetivo',
                'teoria': '''Las oraciones subordinadas adjetivas (o de relativo) funcionan como un adjetivo, modificando a un sustantivo (antecedente).

Introducidas por pronombres relativos:
- que: El libro que leí
- quien/quienes: La persona quien llamó
- cual/cuales: La razón por la cual vine
- cuyo/cuya/cuyos/cuyas: El autor cuyo libro leí
- donde: La casa donde vivo
- cuando: El día cuando nací
- como: La forma como lo hizo

Tipos:
1. Especificativas: seleccionan (sin comas)
   → Los alumnos que estudian aprueban
2. Explicativas: añaden información (con comas)
   → Los alumnos, que estudian, aprueban''',
                'ejemplos': '''1. El libro que leí es interesante. (especificativa)
2. María, que es mi hermana, vive en Madrid. (explicativa)
3. La casa donde vivo es grande. (con "donde")
4. El autor cuyo libro leí ganó un premio. (con "cuyo")
5. Las personas que trabajan duro triunfan. (especificativa)
6. Vi la película que me recomendaste. (especificativa)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica la subordinada: "El libro que compré"',
                        'opciones': ['El libro', 'que', 'que compré', 'compré'],
                        'respuesta_correcta': 'que compré',
                        'explicacion': '¡Correcto! "Que compré" es la subordinada adjetiva que modifica a "libro".',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 17,
                'titulo': 'Subordinadas Adverbiales',
                'nivel': 'intermedio',
                'descripcion': 'Oraciones que funcionan como un adverbio',
                'teoria': '''Las oraciones subordinadas adverbiales funcionan como un complemento circunstancial.

Tipos principales:
1. Lugar: donde
   → Vive donde nació

2. Tiempo: cuando, mientras, antes de que, después de que
   → Llegué cuando terminó

3. Modo: como, según
   → Hazlo como te dije

4. Comparativas: más...que, menos...que, tan...como
   → Es más alto que tú

5. Causales: porque, ya que, puesto que
   → No vine porque estaba enfermo

6. Consecutivas: tan...que, tanto...que
   → Llueve tanto que no salgo

7. Condicionales: si, como, cuando (+ subjuntivo)
   → Si estudias, aprobarás

8. Concesivas: aunque, a pesar de que
   → Aunque llueva, iré

9. Finales: para que, a fin de que
   → Estudio para que me aprueben''',
                'ejemplos': '''1. Voy donde tú vayas. (lugar)
2. Llegué cuando terminó. (tiempo)
3. Hazlo como puedas. (modo)
4. Es tan inteligente que todos lo admiran. (consecutiva)
5. No vine porque llovía. (causal)
6. Si estudias, aprobarás. (condicional)
7. Aunque esté cansado, iré. (concesiva)
8. Te llamo para que vengas. (final)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿Qué tipo es?: "No vine porque llovía"',
                        'opciones': ['Temporal', 'Causal', 'Condicional', 'Final'],
                        'respuesta_correcta': 'Causal',
                        'explicacion': '¡Correcto! "Porque llovía" expresa la causa de no venir.',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 18,
                'titulo': 'Voz Activa y Voz Pasiva',
                'nivel': 'intermedio',
                'descripcion': 'Dos formas de expresar la misma acción',
                'teoria': '''La voz indica si el sujeto realiza la acción (activa) o la recibe (pasiva).

VOZ ACTIVA:
Sujeto agente + verbo + CD
→ Juan escribió la carta

VOZ PASIVA:
Sujeto paciente + ser + participio + (por + agente)
→ La carta fue escrita (por Juan)

Formación de la pasiva:
1. El CD de la activa → Sujeto paciente
2. Verbo ser (conjugado) + participio (concordado)
3. El sujeto de la activa → Complemento agente (por...)

Pasiva refleja (con "se"):
Se venden casas = Las casas son vendidas''',
                'ejemplos': '''1. ACTIVA: El profesor explicó la lección
   PASIVA: La lección fue explicada por el profesor

2. ACTIVA: Los niños comen las manzanas
   PASIVA: Las manzanas son comidas por los niños

3. ACTIVA: Cervantes escribió Don Quijote
   PASIVA: Don Quijote fue escrito por Cervantes

4. PASIVA REFLEJA: Se venden pisos
   = Los pisos son vendidos

5. ACTIVA: María pintó el cuadro
   PASIVA: El cuadro fue pintado por María''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Convierte a pasiva: "Juan escribió el libro"',
                        'opciones': ['El libro escribió Juan', 'El libro fue escrito por Juan', 'Juan fue escrito por el libro', 'El libro es Juan'],
                        'respuesta_correcta': 'El libro fue escrito por Juan',
                        'explicacion': '¡Perfecto! En pasiva: sujeto paciente (el libro) + fue escrito + por Juan (agente).',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 19,
                'titulo': 'Perífrasis Verbales',
                'nivel': 'intermedio',
                'descripcion': 'Construcciones de dos o más verbos',
                'teoria': '''Las perífrasis verbales son construcciones de dos o más verbos que funcionan como uno solo.

Estructura: Verbo auxiliar + nexo (opcional) + verbo principal (infinitivo/gerundio/participio)

TIPOS:

1. Modales (actitud del hablante):
- Obligación: tener que, deber, haber de + infinitivo
  → Tengo que estudiar
- Posibilidad: poder + infinitivo
  → Puede llover

2. Aspectuales (desarrollo de la acción):
- Ingresivas (inicio): ir a, estar a punto de, ponerse a + infinitivo
  → Voy a salir
- Durativas (en proceso): estar, andar, venir + gerundio
  → Estoy estudiando
- Terminativas (fin): dejar de, acabar de + infinitivo
  → Acabo de llegar
- Reiterativas: volver a + infinitivo
  → Vuelvo a intentarlo
- Resultativas: tener, llevar + participio
  → Tengo hecho el trabajo''',
                'ejemplos': '''1. Tengo que estudiar. (obligación)
2. Voy a salir. (ingresiva, futuro inmediato)
3. Estoy leyendo. (durativa)
4. Acabo de llegar. (terminativa reciente)
5. Vuelvo a intentarlo. (reiterativa)
6. Llevo leídos tres libros. (resultativa)
7. Debe de ser tarde. (probabilidad)
8. Vengo trabajando desde las 8. (durativa)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Identifica la perífrasis: "Tengo que estudiar"',
                        'opciones': ['Tengo', 'que', 'Tengo que estudiar', 'estudiar'],
                        'respuesta_correcta': 'Tengo que estudiar',
                        'explicacion': '¡Correcto! "Tengo que estudiar" es una perífrasis modal de obligación.',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': '¿Qué expresa "Voy a salir"?',
                        'opciones': ['Obligación', 'Futuro próximo', 'Acción terminada', 'Posibilidad'],
                        'respuesta_correcta': 'Futuro próximo',
                        'explicacion': 'Perfecto. "Ir a + infinitivo" expresa futuro inmediato (perífrasis ingresiva).',
                        'puntos': 1
                    }
                ]
            },
            {
                'numero': 20,
                'titulo': 'Análisis Sintáctico Completo',
                'nivel': 'intermedio',
                'descripcion': 'Análisis completo de oraciones',
                'teoria': '''El análisis sintáctico completo identifica todas las funciones sintácticas de una oración.

PASOS:

1. Identificar el verbo (núcleo del predicado)
2. Buscar el sujeto (quién realiza la acción)
3. Identificar el tipo de predicado:
   - Verbal: verbo predicativo
   - Nominal: verbo copulativo + atributo

4. Analizar complementos del verbo:
   - CD: ¿qué?, sustituible por lo/la/los/las
   - CI: ¿a quién?, sustituible por le/les
   - CC: ¿dónde?, ¿cuándo?, ¿cómo?, etc.
   - CRég: preposición exigida por el verbo
   - Atributo: con ser, estar, parecer

5. Analizar la estructura de sintagmas:
   - SN (sintagma nominal): Det + N + Ady
   - SV (sintagma verbal): V + Complementos
   - SAdj: Cuant + Adj
   - SAdv: Cuant + Adv
   - SPrep: Prep + Término''',
                'ejemplos': '''EJEMPLO 1: "Los estudiantes leen libros en la biblioteca"
- Sujeto: Los estudiantes (SN: Det + N)
- Predicado: leen libros en la biblioteca (SV)
  - Núcleo: leen
  - CD: libros (SN)
  - CCL: en la biblioteca (SPrep)

EJEMPLO 2: "María dio un regalo a su hermano ayer"
- Sujeto: María (SN: N propio)
- Predicado: dio un regalo a su hermano ayer (SV)
  - Núcleo: dio
  - CD: un regalo (SN: Det + N)
  - CI: a su hermano (SPrep)
  - CCT: ayer (SAdv)

EJEMPLO 3: "El libro es interesante"
- Sujeto: El libro (SN: Det + N)
- Predicado nominal: es interesante
  - Cópula: es
  - Atributo: interesante (SAdj)''',
                'ejercicios': [
                    {
                        'numero': 1,
                        'tipo': 'multiple_choice',
                        'enunciado': 'En "Juan compró flores", el sujeto es:',
                        'opciones': ['Juan', 'compró', 'flores', 'Juan compró'],
                        'respuesta_correcta': 'Juan',
                        'explicacion': '¡Correcto! "Juan" es el sujeto (quién compró). "Flores" es el CD.',
                        'puntos': 1
                    },
                    {
                        'numero': 2,
                        'tipo': 'multiple_choice',
                        'enunciado': 'Tipo de predicado en "María es profesora":',
                        'opciones': ['Verbal', 'Nominal', 'Adverbial', 'No tiene predicado'],
                        'respuesta_correcta': 'Nominal',
                        'explicacion': 'Perfecto. Es predicado nominal porque tiene verbo copulativo (es) + atributo (profesora).',
                        'puntos': 1
                    }
                ]
            }
        ]
        
        # Crear las lecciones y ejercicios
        for leccion_data in lecciones_data:
            ejercicios_data = leccion_data.pop('ejercicios')
            
            # Crear o actualizar la lección
            leccion, created = Leccion.objects.update_or_create(
                numero=leccion_data['numero'],
                defaults=leccion_data
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Creada: Lección {leccion.numero} - {leccion.titulo}'))
            else:
                self.stdout.write(self.style.WARNING(f'↻ Actualizada: Lección {leccion.numero} - {leccion.titulo}'))
            
            # Crear ejercicios para esta lección
            for ej_data in ejercicios_data:
                ejercicio, ej_created = Ejercicio.objects.update_or_create(
                    leccion=leccion,
                    numero=ej_data['numero'],
                    defaults=ej_data
                )
                
                if ej_created:
                    self.stdout.write(f'  ✓ Ejercicio {ej_data["numero"]} creado')
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ ¡Proceso completado! Se cargaron {len(lecciones_data)} lecciones con sus ejercicios.'))
        self.stdout.write(self.style.SUCCESS('Accede al admin para verlas: http://IP:8000/admin'))
