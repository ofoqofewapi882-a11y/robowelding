$outputFile = "c:\Users\User\OneDrive\Рабочий стол\Перманент\Роботы\robo\pptx_text.txt"
$slidesDir = "c:\Users\User\OneDrive\Рабочий стол\Перманент\Роботы\robo\tmp_pptx\ppt\slides"
Set-Content -Path $outputFile -Value "" -Encoding utf8

for ($i=1; $i -le 32; $i++) {
    $xmlPath = "$slidesDir\slide$i.xml"
    if (Test-Path $xmlPath) {
        Add-Content -Path $outputFile -Value "--- SLIDE $i ---" -Encoding utf8
        $xml = [xml](Get-Content $xmlPath -Raw -Encoding utf8)
        $namespaces = @{a='http://schemas.openxmlformats.org/drawingml/2006/main'}
        $texts = Select-Xml -Xml $xml -XPath "//a:t" -Namespace $namespaces | Select-Object -ExpandProperty Node | Select-Object -ExpandProperty '#text'
        if ($texts) {
            $textJoined = ($texts -join " ")
            Add-Content -Path $outputFile -Value $textJoined -Encoding utf8
        }
        Add-Content -Path $outputFile -Value "" -Encoding utf8
    }
}
