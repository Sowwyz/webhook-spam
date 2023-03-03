from discordwebhook import Discord
#you'r webhook
discord = Discord(url="WEBHOOK LINK")
discord.post(
    embeds=[
        {
            "author": {
              #Your Embad name
                "name": "Big Chungus",
              #your name url
                "url": "https://cdn.discordapp.com/attachments/1081107055659716691/1081107602219479140/s-ea2354f44c46765219d3328543bfdddd74061a29.png",
              #your icon url
                "icon_url": "https://cdn.discordapp.com/attachments/1081107055659716691/1081107602219479140/s-ea2354f44c46765219d3328543bfdddd74061a29.png",
            },
          #your title name
            "title": "Sowwyz#1337",
          #your Embad description , Field name
            "description": "GG!! https://discord.gg/Sowwyz",
            "fields": [
                {"name": "Big Chungus ", "value": "https://discord.gg/Sowwyz ", "inline": True},
                {"name": "Discord :  ", "value": "Sowwyz#1337 ", "inline": True},
                
            ],
          #your tumbnail , image url , footer name and icon url
            "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1081107055659716691/1081107602219479140/s-ea2354f44c46765219d3328543bfdddd74061a29.png"},
            "image": {"url": "https://cdn.discordapp.com/attachments/1081107055659716691/1081107602219479140/s-ea2354f44c46765219d3328543bfdddd74061a29.png"},
            "footer": {
                "text": "Developer by: Sowwyz#1337",
                "icon_url": "https://cdn.discordapp.com/attachments/1081107055659716691/1081107602219479140/s-ea2354f44c46765219d3328543bfdddd74061a29.png",
            },
        }
    ],
)
#by hermione
