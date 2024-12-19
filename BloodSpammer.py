import os
import sys
import aiohttp
import asyncio
import time

class GradientPrinter:
    def __init__(self, start_color=(255, 0, 0), end_color=(255, 165, 0), steps=10):
        self.start_color = start_color
        self.end_color = end_color
        self.steps = steps
        self.colors = self._generate_gradient()

    def _generate_gradient(self):
        r_step = (self.end_color[0] - self.start_color[0]) / self.steps
        g_step = (self.end_color[1] - self.start_color[1]) / self.steps
        b_step = (self.end_color[2] - self.start_color[2]) / self.steps

        return [(
            int(self.start_color[0] + r_step * i),
            int(self.start_color[1] + g_step * i),
            int(self.start_color[2] + b_step * i)
        ) for i in range(self.steps)]

    def print(self, text):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            color = self.colors[min(i, len(self.colors) - 1)]
            print(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{line.center(os.get_terminal_size().columns)}\033[0m")

class WebhookSpammer:

    def __init__(self, webhook: str, msg: str, Threads: int):
        self.clear = lambda: os.system("cls" if os.name == "nt" else "clear")
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"}
        self.webhook = webhook
        self.payload = {"content": msg}
        self.Threads = Threads
        self.gradient_printer = GradientPrinter()

    def print_blood(self):
        blood = """
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██████╔╝██║     ██║   ██║██║   ██║██║  ██║███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                       """
        self.gradient_printer.print(blood)
        self.gradient_printer.print("< ADVANCED WEBHOOK SPAMMER >")
        self.gradient_printer.print("< Made by ! Sx_Flow™ >")
        self.gradient_printer.print("< Join = https://discord.gg/wsuDF37YP5 >")
        self.gradient_printer.print("< Used by BloodRaidersTeam >")
        print("\n")

    async def webhook_spammer(self, session, webhook, amount):
        while True:
            async with session.post(webhook, json=self.payload) as s:
                if s.status in (200, 201, 204):
                    sys.stdout.write(f"\033[38;2;255;165;0m [+] Sent webhook to channel with {amount} Threads in its payload.\n\n \033[0m")
                else:
                    json = await s.json()
                    sys.stdout.write(f"\033[38;2;255;0;0m [-] Error sending webhook with {amount} Threads in its payload.\n-> Message: {json['message']}\n-> Retry After: {json['retry_after']}\n\n \033[0m")

    async def start(self):
        self.clear()
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = []
            for amount in range(self.Threads):
                tasks.append(asyncio.create_task(self.webhook_spammer(session, self.webhook, amount)))
            await asyncio.gather(*tasks)

def change_terminal_title():
    if os.name == 'nt':
        os.system("title BloodSpammer")
    else:
        os.system("echo -e '\033]0;BloodSpammer\007'")

if __name__ == "__main__":
    change_terminal_title()

    os.system("cls" if os.name == "nt" else "clear")
    gradient_printer = GradientPrinter()
    blood = """
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██████╔╝██║     ██║   ██║██║   ██║██║  ██║███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                       """
    gradient_printer.print(blood)
    gradient_printer.print("< ADVANCED WEBHOOK SPAMMER >")
    gradient_printer.print("< Made by ! Sx_Flow™ >")
    gradient_printer.print("< Join = https://discord.gg/wsuDF37YP5 >")
    gradient_printer.print("< ☣︎ BloodRaidersTeam ☣︎ >")
    print("\n")

    try:
        print("")
        webhook_urls = input("\033[38;2;255;0;0m┌──(Blood@input) ~ (enter the webhook urls separated by space) ~ (if you want you can use only 1 webhook) \n└─$ \033[0m").split()
        print("")  
        msg = input("\033[38;2;255;0;0mWrite what message to send ~ \033[0m")
        print("")  
        Threads = int(input("\033[38;2;255;0;0mEnter how many Threads to send (it is recommended to put 10) ~ \033[0m"))  

        client = WebhookSpammer(webhook=webhook_urls, msg=msg, Threads=Threads)
        start_time = time.time()
        asyncio.get_event_loop().run_until_complete(client.start())
        finish_time = round((time.time() - start_time), 4)
        sys.stdout.write(f"\033[38;2;255;0;0m-> Finished executing webhook.\n-> Finished in {finish_time}s.")
    except Exception as error:
        sys.stdout.write(f"\033[38;2;255;0;0m-> Event loop has ended or you are being ratelimited or was given invalid roles.\n-> Exception: {error}.\n-> Press enter to exit.\n")
        input("-> ")
        os._exit(0)
