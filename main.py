import discord
from discord.ext import commands
import os, random, requests, asyncio
description = 'Bot de concientizacion sobre el cambio climatico'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def hola(ctx):
    """Say hi."""
    await ctx.send(">>> *Mucho gusto*, soy un bot encargado de concientizar a los usuarios de discord sobre el cambio climatico y que reduzcan su huella de carbono. para ver lo que puedo hacer a detalle escribe `?ayuda`.")

@bot.command()
async def ayuda(ctx):
    """Give all comands details and examples"""
    await ctx.send(""">>> ## ***Los comandos del bot son:***
﻿
﻿
- `?manualidad` *= Te da una manualidad para reducir y reciclar*
- `?memr` = *Te da un meme sobre reciclaje*
- `?consejos` + las iniciales del país = *Te da informacion de los efetos del cambio climatico de las iniciales del paIs que pongas*
- `?pregunta` = Lanza una pregunta de trivia relacionada con el cambio climático. Después de que respondas, te dirá si tu respuesta fue correcta o incorrecta y te proporcionará la respuesta correcta y una explicación.
- `?mito` = Te presenta un mito relacionado con el cambio climático y te pide que determines si es verdadero o falso. Luego, te informará si tu respuesta fue correcta y te dará una explicación.
- `?sugerencia` = Comando que de diferentes sugerencias prácticas y hábitos diarios que las personas pueden adoptar para reducir su huella de carbono""")

@bot.event
async def on_command_error(ctx, error):
    """Maneja comandos no reconocidos."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(">>> ***__Ese comando no existe.__ Usa `?ayuda` para ver la lista de comandos disponibles y para qué sirven.***")
    else:
        raise error
    
@bot.command()
async def memr(ctx):
    memr = random.choice(os.listdir("memr"))
    with open(f'memr/{memr}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def manualidad(ctx):
    manualidad = random.choice(os.listdir("manualidad"))
    with open(f'manualidad/{manualidad}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

consejos_por_pais = {
    "AR": "En Argentina, el cambio climático provoca el derretimiento de glaciares en los Andes, aumento de la temperatura promedio, y más inundaciones y sequías en diferentes regiones.",
    "BO": "En Bolivia, los consejos del cambio climático incluyen la reducción de la cobertura glaciar, sequías prolongadas, y cambios en los patrones de lluvias que afectan la agricultura.",
    "BR": "En Brasil, la deforestación del Amazonas contribuye al cambio climático, que se manifiesta en olas de calor más intensas, sequías severas, y pérdida de biodiversidad.",
    "CA": "En Canadá, el cambio climático se evidencia con el derretimiento del hielo ártico, incendios forestales más frecuentes y severos, y cambios en los ecosistemas boreales.",
    "CL": "En Chile, los consejos incluyen la disminución de las precipitaciones en el centro y sur del país, el retroceso de los glaciares, y la desertificación en algunas regiones.",
    "CO": "En Colombia, el cambio climático se manifiesta en la pérdida de glaciares, aumento en la frecuencia de deslizamientos de tierra, y alteraciones en los ecosistemas de páramo.",
    "CR": "En Costa Rica, los consejos incluyen el aumento en la intensidad de huracanes y tormentas, cambios en la biodiversidad, y amenazas a la producción agrícola.",
    "CU": "En Cuba, el cambio climático provoca el aumento del nivel del mar, afectando las zonas costeras, y también un incremento en la frecuencia e intensidad de huracanes.",
    "DO": "En República Dominicana, el cambio climático se manifiesta en huracanes más fuertes, aumento en el nivel del mar que afecta las costas, y cambios en la agricultura.",
    "EC": "En Ecuador, los consejos incluyen el retroceso de los glaciares, cambios en los patrones de lluvia, y el impacto en la biodiversidad, especialmente en las Islas Galápagos.",
    "SV": "En El Salvador, el cambio climático se evidencia en lluvias más intensas, sequías prolongadas, y un aumento en la vulnerabilidad a desastres naturales.",
    "GT": "En Guatemala, los consejos del cambio climático incluyen sequías prolongadas, aumento en la intensidad de tormentas, y una mayor inseguridad alimentaria debido a la variabilidad climática.",
    "HN": "En Honduras, los consejos incluyen huracanes más intensos, sequías prolongadas, y un impacto negativo en la agricultura y los recursos hídricos.",
    "MX": "En México, el cambio climático provoca sequías más frecuentes, aumento en la temperatura promedio, y huracanes más intensos en las costas.",
    "NI": "En Nicaragua, el cambio climático se manifiesta en huracanes más fuertes, sequías prolongadas, y la pérdida de biodiversidad en ecosistemas clave.",
    "PA": "En Panamá, los consejos incluyen el aumento en la frecuencia e intensidad de las lluvias, la subida del nivel del mar que amenaza las zonas costeras, y cambios en la biodiversidad.",
    "PY": "En Paraguay, el cambio climático se evidencia en sequías prolongadas, aumento en la temperatura promedio, y la alteración de los ciclos hidrológicos que afecta la agricultura.",
    "PE": "En Perú, los consejos del cambio climático incluyen el derretimiento de los glaciares, alteraciones en los patrones de lluvia que afectan la agricultura, y la intensificación de fenómenos como El Niño.",
    "PR": "En Puerto Rico, el cambio climático provoca huracanes más intensos, el aumento del nivel del mar que amenaza las zonas costeras, y cambios en los ecosistemas marinos.",
    "ES": "En España, los consejos incluyen olas de calor más frecuentes, aumento en la desertificación, incendios forestales más graves, y la pérdida de recursos hídricos.",
    "UY": "En Uruguay, el cambio climático se manifiesta en un aumento de las temperaturas promedio, mayor frecuencia de inundaciones, y cambios en los patrones de lluvias.",
    "VE": "En Venezuela, los consejos incluyen sequías más severas, reducción en la disponibilidad de agua, y cambios en la biodiversidad debido a la alteración de los ecosistemas."
}

@bot.command()
async def consejos(ctx, pais: str = None):
    if not pais:
        await ctx.send("Por favor, proporciona las iniciales del país luego del comando.")
        return
    
    pais = pais.upper()  
    if pais in consejos_por_pais:
        await ctx.send(consejos_por_pais[pais])
    else:
        await ctx.send("Lo siento, no tengo información sobre ese país. Por favor, asegúrate de usar las iniciales correctas o escribe `?ayuda`.")

trivia_preguntas = [
    {
        "preguntas": "¿Cuál es el gas de efecto invernadero más abundante en la atmósfera?",
        "opciones": ["A) Dióxido de carbono", "B) Metano", "C) Vapor de agua", "D) Óxido nitroso"],
        "respuesta": "C"
    },
    {
        "preguntas": "¿Qué porcentaje del planeta está cubierto por océanos?",
        "opciones": ["A) 50%", "B) 71%", "C) 80%", "D) 90%"],
        "respuesta": "B"
    },
    {
        "preguntas": "¿Cuál de las siguientes actividades humanas es la mayor fuente de emisiones de dióxido de carbono?",
        "opciones": ["A) Agricultura", "B) Deforestación", "C) Transporte", "D) Uso de combustibles fósiles"],
        "respuesta": "D"
    },
    {
        "preguntas": "¿Qué es el Protocolo de Kioto?",
        "opciones": ["A) Un acuerdo internacional para reducir las emisiones de gases de efecto invernadero", 
                    "B) Un tratado para proteger la biodiversidad", 
                    "C) Un plan para limpiar los océanos", 
                    "D) Un proyecto de energía renovable en Japón"],
        "respuesta": "A"
    },
    {
        "preguntas": "¿Qué país emite la mayor cantidad de gases de efecto invernadero por persona?",
        "opciones": ["A) Estados Unidos", "B) China", "C) Australia", "D) India"],
        "respuesta": "C"
    },
    {
        "preguntas": "¿Qué porcentaje de la electricidad mundial proviene de energías renovables?",
        "opciones": ["A) 10%", "B) 24%", "C) 36%", "D) 50%"],
        "respuesta": "B"
    },
    {
        "preguntas": "¿Cuál es el principal causante de la acidificación de los océanos?",
        "opciones": ["A) Plásticos", "B) Derrames de petróleo", "C) Dióxido de carbono", "D) Residuos nucleares"],
        "respuesta": "C"
    },
    {
        "preguntas": "¿Cuál es el país con mayor tasa de deforestación en la Amazonía?",
        "opciones": ["A) Perú", "B) Colombia", "C) Bolivia", "D) Brasil"],
        "respuesta": "D"
    }
]

@bot.command()
async def pregunta(ctx):
    preguntas = random.choice(trivia_preguntas)
    preguntas_text = f">>> **{preguntas['preguntas']}** Tienes 15 segundos\n" + "\n".join(preguntas['opciones'] )
    
    await ctx.send(preguntas_text)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        # Espera por la respuesta del usuario
        response = await bot.wait_for('message', check=check, timeout=15.0)
    except asyncio.TimeoutError:
        await ctx.send('>>> ⏰ ***¡Tiempo agotado!***  La respuesta correcta era: ' + preguntas['respuesta'])
    else:
        if response.content.upper() == preguntas['respuesta']:
            await ctx.send('>>> ✅ ***¡Correcto!*** 🎉')
        else:
            await ctx.send('>>> ❌ ***Incorrecto***.  La respuesta correcta era: ' + preguntas['respuesta'])

mitos_climaticos = [
    {
        "mitos": "El cambio climático es solo un fenómeno natural y no está influenciado por actividades humanas.",
        "es_verdadero": False,
        "explicacion": "Falso. Si bien la Tierra ha experimentado cambios climáticos naturales en el pasado, la evidencia científica muestra que el calentamiento global actual es principalmente causado por las actividades humanas, como la quema de combustibles fósiles y la deforestación."
    },
    {
        "mitos": "El cambio climático no es real porque hace frío en invierno.",
        "es_verdadero": False,
        "explicacion": "Falso. El cambio climático se refiere a patrones climáticos a largo plazo. El hecho de que haga frío en invierno no contradice la tendencia general de calentamiento global."
    },
    {
        "mitos": "La capa de ozono y el cambio climático son lo mismo.",
        "es_verdadero": False,
        "explicacion": "Falso. La capa de ozono y el cambio climático son problemas ambientales diferentes. La capa de ozono protege la Tierra de la radiación ultravioleta, mientras que el cambio climático se refiere al calentamiento global causado por el aumento de gases de efecto invernadero en la atmósfera."
    },
    {
        "mitos": "El dióxido de carbono es el único gas de efecto invernadero.",
        "es_verdadero": False,
        "explicacion": "Falso. Aunque el dióxido de carbono es uno de los principales gases de efecto invernadero, otros gases como el metano y el óxido nitroso también contribuyen al cambio climático."
    },
    {
        "mitos": "Los niveles del mar no están aumentando.",
        "es_verdadero": False,
        "explicacion": "Falso. Los niveles del mar están aumentando debido al derretimiento de los glaciares y el hielo polar, así como la expansión térmica del agua a medida que se calienta."
    },
    {
        "mitos": "El cambio climático no es un problema urgente; tenemos tiempo para solucionarlo más adelante.",
        "es_verdadero": False,
        "explicacion": "Falso. El cambio climático ya está afectando a muchas regiones del mundo y sus impactos se están intensificando. Las acciones para mitigar y adaptarse deben tomarse de inmediato para evitar consecuencias más graves en el futuro."
    },
    {
        "mitos": "Las energías renovables no son una solución efectiva contra el cambio climático.",
        "es_verdadero": False,
        "explicacion": "Falso. Las energías renovables, como la solar y la eólica, juegan un papel crucial en la reducción de las emisiones de gases de efecto invernadero y la transición hacia un sistema energético más sostenible."
    },
    {
        "mitos": "El cambio climático solo afecta a los países en desarrollo.",
        "es_verdadero": False,
        "explicacion": "Falso. Aunque los países en desarrollo a menudo sufren de manera más severa debido a su menor capacidad de adaptación, el cambio climático afecta a todos los países. Las naciones desarrolladas también enfrentan riesgos como eventos climáticos extremos, cambios en los ecosistemas y desafíos económicos."
    }
]

@bot.command()
async def mito(ctx):
    mito = random.choice(mitos_climaticos)
    es_verdadero = 'Verdadero' if mito['es_verdadero'] else 'Falso'
    mitos_text = f">>> **{mito['mitos']}**\n ¿Es verdadero o falso? Responde con 'Verdadero' o 'Falso', tienes 15 segundos."
    
    await ctx.send(mitos_text)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        response = await bot.wait_for('message', check=check, timeout=15.0)
    except asyncio.TimeoutError:
        await ctx.send(f'>>> ⏰ ***¡Tiempo agotado!***  La respuesta correcta era: {mito["explicacion"]}')
    else:
        if response.content.strip().lower() == es_verdadero.lower():
            await ctx.send('>>> ✅ ***¡Correcto!*** 🎉')
        else:
            await ctx.send(f'>>> ❌ ***Incorrecto***.  La respuesta correcta era: {mito["explicacion"]}')

@bot.command()
async def sugerencias(ctx):
    """Ofrece una sugerencia práctica aleatoria para reducir la huella de carbono"""
    sugerencias = [
        "Reduce el uso del automóvil: Opta por caminar, andar en bicicleta o usar el transporte público siempre que sea posible.",
        "Eficiencia energética en el hogar: Usa bombillas LED, apaga los aparatos eléctricos cuando no los estés usando y considera invertir en electrodomésticos de bajo consumo.",
        "Reduce, reutiliza y recicla: Evita los productos de un solo uso, reutiliza materiales cuando puedas y asegúrate de reciclar correctamente.",
        "Compra productos locales y de temporada para reducir la huella de carbono asociada al transporte de alimentos.",
        "Conserva el agua: Instala dispositivos de ahorro de agua y repara cualquier fuga para reducir el consumo.",
        "Adopta una dieta más sostenible: Reduce el consumo de carne y productos de origen animal, y elige opciones vegetales y de bajo impacto.",
        "Participa en programas de reforestación o planta árboles en tu comunidad para ayudar a absorber CO2.",
        "Utiliza equipos de bajo consumo y apaga las luces y computadoras cuando no estén en uso.",
        "Comparte información sobre el cambio climático y promueve prácticas sostenibles en tu comunidad.",
        "Apoya iniciativas y negocios que se comprometan a reducir su impacto ambiental y adoptar prácticas sostenibles."
    ]
    
    sugerencia = random.choice(sugerencias)
    await ctx.send(f">>> **Sugerencia para reducir tu huella de carbono:**\n{sugerencia}")
    
bot.run('token')