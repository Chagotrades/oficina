# Crea la carpeta de un cliente nuevo desde plantilla-cliente/.
# Uso: powershell -ExecutionPolicy Bypass -File .\nuevo-cliente.ps1 -Nombre "Campo Verde San Pedro"
param(
    [Parameter(Mandatory = $true)][string]$Nombre
)

$ErrorActionPreference = 'Stop'
$utf8 = New-Object System.Text.UTF8Encoding($false)
$raiz = $PSScriptRoot
$Nombre = $Nombre.Trim()

# Nombre de carpeta: minúsculas, sin tildes, palabras separadas por guiones.
$sinTildes = -join ($Nombre.Normalize([Text.NormalizationForm]::FormD).ToCharArray() |
    Where-Object { [Globalization.CharUnicodeInfo]::GetUnicodeCategory($_) -ne 'NonSpacingMark' })
$carpeta = ($sinTildes.ToLowerInvariant() -replace '[^a-z0-9]+', '-').Trim('-')
if (-not $carpeta) { throw "El nombre '$Nombre' no sirve para crear una carpeta." }

$destino = Join-Path $raiz "clientes\$carpeta"
if (Test-Path $destino) {
    Write-Error "Ya existe clientes\$carpeta. No se tocó nada."
    exit 1
}

$fecha = Get-Date -Format 'yyyy-MM-dd'
$nombreTabla = $Nombre -replace '\|', '/'

Copy-Item (Join-Path $raiz 'plantilla-cliente') $destino -Recurse
Get-ChildItem $destino -Filter *.md -Recurse | ForEach-Object {
    $texto = [IO.File]::ReadAllText($_.FullName, $utf8)
    $texto = $texto.Replace('{{CLIENTE}}', $Nombre).Replace('{{FECHA}}', $fecha)
    [IO.File]::WriteAllText($_.FullName, $texto, $utf8)
}

# Agrega una fila al final de la tabla de clientes del CLAUDE.md de la oficina (es la última sección).
$claude = Join-Path $raiz 'CLAUDE.md'
$texto = [IO.File]::ReadAllText($claude, $utf8).TrimEnd() + "`n| ``clientes/$carpeta/`` | $nombreTabla |`n"
[IO.File]::WriteAllText($claude, $texto, $utf8)

# Agrega el encargo de alta en ENCARGOS.md, justo debajo del encabezado de la tabla (lo más nuevo arriba).
$encargos = Join-Path $raiz 'ENCARGOS.md'
$lineas = [Collections.Generic.List[string]]([IO.File]::ReadAllText($encargos, $utf8).TrimEnd() -split "`r?`n")
$separador = $lineas.FindIndex([Predicate[string]] { param($l) $l -match '^\|(-+\|)+$' })
if ($separador -lt 0) { throw "No encontré la tabla en ENCARGOS.md. La carpeta del cliente sí quedó creada." }
$lineas.Insert($separador + 1, "| $fecha | $nombreTabla | Alta del cliente | Santiago | por hacer | Completar descripción y límites en clientes/$carpeta/CLAUDE.md |")
[IO.File]::WriteAllText($encargos, ($lineas -join "`n") + "`n", $utf8)

Write-Output "Listo: clientes\$carpeta"
