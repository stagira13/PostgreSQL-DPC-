$x = Import-Csv DRGEF.txt -Delimiter "`t" -Encoding Default
$x | foreach {
$_.‘Þ‰@”NŒŽ“ú = $_.‘Þ‰@”NŒŽ“ú.replace("00000000","infinity")
}
$x | Export-Csv outputE.txt -notype -Encoding UTF8 -Delimiter "`t"