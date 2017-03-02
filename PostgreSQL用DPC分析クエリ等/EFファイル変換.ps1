$x = Import-Csv DRGEF.txt -Delimiter "`t" -Encoding Default
$x | foreach {
$_.退院年月日 = $_.退院年月日.replace("00000000","infinity")
}
$x | Export-Csv outputE.txt -notype -Encoding UTF8 -Delimiter "`t"