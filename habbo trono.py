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




####
#Programado Por Jose89fcb
#Twitter: twitter.com/jose89fcb
####
@bot.command()
async def trono(ctx, *, keko): #Comando "trono"
    await ctx.message.delete() #Borramos el comando para no dejar sucio el chat xD
    await ctx.send("Generando Trono...", delete_after=0)
    time.sleep(3) #Añadimos un tiempo para que sea borrado
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
   
    
    habbo = response.json()['figureString']
   

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&action=sit&action=sit&direction=4&head_direction=4&gesture=std&size=m"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko
    
    


    
    


    

   

    

    
    
    



    img2 = img1.copy()
    
    
    almo = Image.open(r"imagenes/silla-parte.png").convert("RGBA") #imagen de la trozo
    img1 = almo.resize((80,200), Image.Resampling.LANCZOS)#tamaño de la silla

 



    
    

    
    


    img1.paste(img2,(10,30), mask = img2) #Posicion del keko 1
   
    ###
    

   

    img2 = img1.copy()
    pata = Image.open(r"imagenes/pata-parte.png").convert("RGBA") #imagen de la pata
    img1 = pata.resize((80,200), Image.Resampling.LANCZOS)#tamaño de la pata

    img1.paste(img2,(0,0), mask = img2) #Posicion del keko
    img1.paste(pata,(0,0), mask = pata) #Posicion del trozo de silla
    

    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)
       
        
        await ctx.send(file=discord.File(fp=image_binary, filename=f'keko_{keko}.png'))

        
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   
