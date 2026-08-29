from datetime import datetime
from zoneinfo import ZoneInfo

Hora_Filipinas = datetime.now(ZoneInfo("Asia/Manila"))
Hora_Brasil = datetime.now(ZoneInfo("America/Sao_Paulo"))

print(Hora_Filipinas.strftime("%d/%m/%Y %H:%M:%S"))
print(Hora_Brasil.strftime("%d/%m/%Y %H:%M:%S"))
