$x = Import-Csv DRGEF.txt -Delimiter "`t" -Encoding Default
$x | foreach {
$_.�މ@�N���� = $_.�މ@�N����.replace("00000000","infinity")
}
$x | Export-Csv outputE.txt -notype -Encoding UTF8 -Delimiter "`t"