# teafyi — Python Tea Encyclopedia Demo
Output demo.gif

Set FontSize 14
Set Width 920
Set Height 620
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 35ms
Set Padding 20

Type `curl -s 'https://teafyi.com/api/search/?q=green+tea' | jq '.results[:3][] | {name, type}'`
Enter
Sleep 3s

Type `curl -s 'https://teafyi.com/api/variety/matcha/' | jq '{name, category}'`
Enter
Sleep 3s

Type `curl -s 'https://teafyi.com/api/random/' | jq '{name, type}'`
Enter
Sleep 3s

Sleep 2s
