import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time


with open("configuracion.json") as f: #Creamos un archivo de configuracion para el bot
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Prefijo para el comando !trono
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def trono(ctx, *, keko): #Comando "trono"
    await ctx.message.delete() #Borramos el comando para no dejar sucio el chat xD
    await ctx.send("Generando Trono...", delete_after=0)
    time.sleep(3) #Añadimos un tiempo para que sea borrado
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
   


    habbo = response.json()['figureString']
   
   

   
    
    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&action=sit&action=sit&direction=4&head_direction=3&gesture=sml&size=m"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko
    
    
    
    

    

    



    img2 = img1.copy()
    
    
    almo = Image.open(r"imagenes/trono.png").convert("RGBA") #imagen de la trozo
    img1 = almo.resize((118,133), Image.ANTIALIAS)#tamaño de la silla

 


   

    
    


    img1.paste(img2,(10,10), mask = img2) #Posicion del keko 1
   
    ###
    

   

    img2 = img1.copy()
    pata = Image.open(r"imagenes/pata_trono.png").convert("RGBA") #imagen de la pata
    img1 = pata.resize((118,133), Image.ANTIALIAS)#tamaño de la pata

    img1.paste(img2,(0,0), mask = img2) #Posicion del keko
    img1.paste(pata,(0,0), mask = pata) #Posicion del trozo de silla
    

    




    
     ###
    img2 = img1.copy()
    globo = Image.open(r"imagenes/globo.png").convert("RGBA") #imagen de la pata
    img1 = globo.resize((118,133), Image.ANTIALIAS)#tamaño de la pata
    
    img1.paste(img2,(0,0), mask = img2) #Posicion del keko
    img1.paste(globo,(0,0), mask = globo) #Posicion del globo
    ###
    
    
    
    
   
    
    
       
      
     ###
    draw = ImageDraw.Draw(img1)
    font = ImageFont.truetype("fuentes/volter.ttf", 9) #Tamaño de la fuente (textos)

    draw.text((8, 10), f"¡Hey soy {keko}!", font=font, fill=(0,0,0))  #Texto y color
     ###
      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)
       
        
        await ctx.send(file=discord.File(fp=image_binary, filename=f'keko.png'))
      

        
         
        
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('El comando no existe 🤷🏼‍♂️🔍')
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   