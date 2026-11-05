# Sincroniza la oficina con GitHub: baja lo del otro socio y sube lo tuyo.
# Uso: powershell -ExecutionPolicy Bypass -File .\sincronizar.ps1 "que hiciste"
param([string]$Mensaje = "Avance")

Set-Location $PSScriptRoot
$socio = git config user.name
if (-not $socio) {
    Write-Host "Falta tu nombre en git. Corre una vez: git config --global user.name ""TuNombre""" -ForegroundColor Red
    exit 1
}

# 1. Guardar lo tuyo
git add -A
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -q -m "$Mensaje ($socio)"
    Write-Host "Guardado: $Mensaje" -ForegroundColor Green
}

# 2. Bajar lo del otro socio
git pull --rebase -q
if ($LASTEXITCODE -ne 0) {
    git rebase --abort 2>$null
    Write-Host "CHOQUE: tu y el otro socio cambiaron lo mismo. No se subio nada. Pidele a Claude que lo resuelva." -ForegroundColor Red
    exit 1
}

# 3. Subir
git push -q
if ($LASTEXITCODE -ne 0) {
    Write-Host "No se pudo subir a GitHub. Revisa tu internet o tu sesion de GitHub." -ForegroundColor Red
    exit 1
}
Write-Host "Listo: la oficina quedo al dia." -ForegroundColor Green
git log -3 --format="  %h  %an  %s"
