from decouple import config
from pypresence import Presence
import time
import psutil

client_id = config("CLIENT_ID")
RPC = Presence(client_id)

time.sleep(30) # Delay to make sure Discord is running

RPC.connect()

vs_start_time = None

try:
    while True:
        cpu_per = round(psutil.cpu_percent(), 1)
        mem = psutil.virtual_memory()
        
        # Check is Visual Studio is running
        vs_running = any("devenv" in p.name().lower() for p in psutil.process_iter(attrs=['pid', 'name']))
        
        if vs_running:
            if vs_start_time is None:
                vs_start_time = time.time()
            else:
                elapsed_time = int(time.time() - vs_start_time)
                RPC.update(
                    details="Working on a project",
                    state="CPU: {}% | RAM: {}%".format(cpu_per, mem.percent),
                    large_image="vslogo",
                    large_text="Visual Studio",
                    start=vs_start_time, # Set the start time to when VS was opened
                    buttons=[{"label": "GitHub", "url": "https://github.com/FoRoKo1o"},
                             {"label": "YouTube", "url": "https://youtube.com/@foroko"}]
                )
        else:
            vs_start_time = None  # Zresetowanie czasu początkowego
            RPC.update(
                state="CPU: {}% | RAM: {}%".format(cpu_per, mem.percent),
                buttons=[{"label": "GitHub", "url": "https://github.com/FoRoKo1o"},
                         {"label": "YouTube", "url": "https://youtube.com/@foroko"}]
            )
            
        time.sleep(10)
except KeyboardInterrupt:
    pass
finally:
    RPC.close()
