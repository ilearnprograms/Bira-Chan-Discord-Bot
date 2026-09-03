import discord
import os
from discord.ext import commands
import re
import random

class Prefixless(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Define triggers and responses
        responses = {

            ("sigara", "sigara içiyorum", "sigara iciyorum", "cigara"): [
                "Ver bakeem bir dal.🚬",
                "Cigara mı? Sonunda mantıklı birisi.",
                "Çakmağı ver len.",
                "Bir dal yakam da kendime gelem.🚬",
                "Hmph. Sigara içmeden nasıl yaşıyorsunuz siz abi ya?🚬",
                "Ben zaten yeterince içiyorum, bir de sana mı yetişeceğim amk",
            ],

            ("dal", "bir dal", "dal var mı", "dal varmi"): [
                "Var. Ama vermek istemiyorum bu sonuncu.",
                "Son dalımdı... artık senin. Deftere yazarsın.",
                "Bir dal mı? Çakmağı da ister misin aq?",
                "Al. Ama borçlusun he unutma nyan.",
                "Cebimde varsa senindir. Muhtemelen yok ama sjsjsjs.",
            ],

            ("çakmak", "cakmak", "çakmağın var mı", "cakmagin var mi"): [
                "Var. Ama geri vereceksin yoksa belanı...",
                "Çakmak mı? Az önce kim aldı onu sikerim ha?",
                "Bir saniye... cebimde olması lazım.",
                "Çakmağımı kaybettim. Ananı sikeyim.",
                "Al, ama kaybedersen seni gebertirim. 😤",
            ],

            ("sigaram bitti", "sigara bitti", "sigaram yok", "sigara yok"): [
                "NE?! Acil durum ilan ediyorum.",
                "Bu bir felaket. CIMER nerde",
                "Bir dal veririm ama sonuncuydu...",
                "Markete git. Hemen.",
                "Sigarasız mı kaldın? Geçmiş olsun kral.🚬",
            ],

            ("marlboro",): [
                "Kırmızı mı, Gold mu?",
                "Marlboro mu? Olsada içsem.🚬",
                "Bir Marlboro uzat.",
                "Marlboro görünce cüzdanım ağlıyor.",
            ],

            ("parliament",): [
                "Parliament mı? Beyaz paketli aristokrat.",
                "Parliament içenlerin cebinde kesin çakmak vardır.",
                "Bir tane ver de konuşalım.🚬",
            ],

            ("camel",): [
                "Deve mi? Yoksa sigara mı?",
                "Camel görünce çöl susuzluğu geliyor.😤",
                "Bir Camel yakılır şimdi.🚬",
            ],

            ("winston",): [
                "Winston mı? Fena değil.",
                "Winston içen adamın acelesi yoktur.",
                "Bir Winston ver.🚬",
            ],

            ("kent",): [
                "Kent. Sessiz ama tehlikeli.",
                "Kent mi? Hmph.😤",
                "Bir tane yakalım.🚬",
            ],

            ("balkondan", "talon", "balkon"): [
                "https://media.discordapp.net/attachments/1358927968944259285/1401962206047899759/image.gif?ex=6a867fcd&is=6a852e4d&hm=aea05a39d9de614a1dea3cebd4289becab6044ef738068c40e677c7de194aa2f&=",       
            ],

            ("bira ver", "bir bira", "bana bira", "bira lazım", "bira lazim", "bi bira", ): [
                "Al. Buz gibi.🍺",
                "Bir tane mi? Komik olma.",
                "Dolapta var. Git kendin al.",
                "Sana bira vereceğim de... önce hak et.",
            ],

            ("bira", "bira içiyorum", "bira iciyorum", "beer",): [
                "Buz gibi bira nerede?🍺",
                "Bir bira aç da kendime geleyim.",
                "Sigaranın yanına bira lazım.😤",
                "Bira mı? Şimdi konuşmaya başladık.🍺",
                "Soğuk olsun. Ilık bira içmem.🍺",
            ],

            ("efes pilsen",): [
                "Efes Pilsen. Klasik.🍺",
                "Buzdolabında varsa getir.",
                "Efes Pilsen açıldıysa ben hazırım.",
            ],

            ("efes",): [
                "Efes mi? Türkiye'nin final boss'u.🍺",
                "Bir Efes açılır şimdi.",
                "Efes + sigara = klasik.",
                "Soğuk Efes'e hayır demem.",
            ],


            ("tuborg", "tuborg gold"): [
                "Tuborg Gold mu? Şimdi ciddi konuşuyoruz.🍺",
                "Bir Tuborg aç da ortam düzelsin.",
                "Tuborg görünce sigara yakasım geliyor.😤",
            ],

            ("bomonti",): [
                "Bomonti mi? Havalı takılmaya başladık.🍺",
                "Bomonti + balkon + sigara.",
                "Bir Bomonti açılır şimdi.",
            ],

            ("corona",): [
                "Corona mı? Bira olanından bahsediyorsun umarım.",
                "Corona + limon? Hmph.",
                "Buz gibi Corona fena gitmez.🍺",
            ],

            ("heineken",): [
                "Heineken mi? Hollandalılar yine iş başında haa.",
                "Bir Heineken aç da yudumlayak moruk.",
                "Heineken + sigara. Fena kombinasyon moruk ya.",
            ],

            ("guinness",): [
                "Guinness mi? Ağırdan alıyorsun kral.",
                "O siyah bira nerede? Offf...",
                "Guinness içip hayatı sorgulama vakti. Bir de sigara tabii..",
            ],
            ("kedi", "cat", "miyav", "meow", "kedisi",): [
                "Miyav. Sigaramı ver.",
                "Kedi değilim. Ben profesyonelim.",
                "Miyav mı? Bira getir.",
                "Hmph. Miyav.",
                "Ne var? Sigara uzat.🚬",
                "Biri bana mı seslendi?",
            ]
            
        }

        # Remember the last response used for each response list.
        # This prevents the exact same response from being selected twice in a row.
        self.last_responses = {}

        # Compile regex patterns once
        self.patterns = []

        for triggers, resp_list in responses.items():
            for t in triggers:
                pattern = re.compile(
                    r"\b" + re.escape(t.lower()) + r"\b"
                )

                self.patterns.append((pattern, resp_list))


    @commands.Cog.listener()
    async def on_message(self, message):

        # Ignore our own messages, but listen to other bots
        if message.author.id == self.bot.user.id:
            return

        if message.author.bot:
            return

        msg = message.content.lower()

        for pattern, resp_list in self.patterns:
            if pattern.search(msg):

                # If there's only one possible response
                if len(resp_list) == 1:
                    response = resp_list[0]

                else:
                    # Get the previous response used for this list
                    last_response = self.last_responses.get(
                        id(resp_list)
                    )

                    # Don't repeat the same response twice in a row
                    possible_responses = [
                        resp for resp in resp_list
                        if resp != last_response
                    ]

                    response = random.choice(possible_responses)

                    # Remember it
                    self.last_responses[id(resp_list)] = response

                await message.channel.send(response)
                break


async def setup(bot):
    await bot.add_cog(Prefixless(bot))
