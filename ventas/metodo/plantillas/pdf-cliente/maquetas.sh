#!/bin/bash
# Uso: bash maquetas.sh <carpeta_maquetas>
# Convierte cada .html de la carpeta en PNG (600x1000, o 1600x1040 si el nombre contiene "escritorio") a doble resolución.
EDGE="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
D="$(cygpath -m "$1")"; PERFIL="$(cygpath -m "$TEMP")/edge-pdf-cliente"
cd "$D" || exit 1
for f in *.html; do
  n="${f%.html}"; size="600,1000"; [[ "$n" == *escritorio* ]] && size="1600,1040"
  "$EDGE" --headless=new --disable-gpu --hide-scrollbars --user-data-dir="$PERFIL" --force-device-scale-factor=2 \
    --window-size=$size --virtual-time-budget=6000 --screenshot="$(cygpath -w "$D/$n.png")" "file:///$(cygpath -m "$D/$f")" 2>/dev/null
done
ls -la *.png
