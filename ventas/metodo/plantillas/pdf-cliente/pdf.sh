#!/bin/bash
# Uso: bash pdf.sh <carpeta_pdf> <nombre_sin_extension> <numero_de_paginas>
# Genera <nombre>.pdf (A4, sin encabezados) y una hoja de miniaturas <nombre>-hoja.png para revisar cada página.
EDGE="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
D="$(cygpath -m "$1")"; n="$2"; pages="$3"; PERFIL="$(cygpath -m "$TEMP")/edge-pdf-cliente"
URL="file:///$(cygpath -m "$D/$n.html")"
"$EDGE" --headless=new --disable-gpu --user-data-dir="$PERFIL" --no-pdf-header-footer --virtual-time-budget=8000 \
  --print-to-pdf="$(cygpath -w "$D/$n.pdf")" "$URL" 2>/dev/null
"$EDGE" --headless=new --disable-gpu --hide-scrollbars --user-data-dir="$PERFIL" --window-size=794,$((1123*pages)) \
  --virtual-time-budget=8000 --screenshot="$(cygpath -w "$D/_$n-largo.png")" "$URL" 2>/dev/null
python -I -c "
from PIL import Image
im=Image.open(r'$D/_$n-largo.png');p=$pages
s=Image.new('RGB',(4*407,((p+3)//4)*571),'gray')
for i in range(p): s.paste(im.crop((0,i*1123,794,(i+1)*1123)).resize((397,561)),((i%4)*407+5,(i//4)*571+5))
s.save(r'$D/$n-hoja.png')
"
rm -f "$D/_$n-largo.png"; ls -la "$D/$n.pdf"
