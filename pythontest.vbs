' test, whether the host is CScript.exe
If (Instr(UCase(WScript.FullName), "CSCRIPT") = 0) Then
 Set WshShell = WScript.CreateObject("WScript.Shell")
 WshShell.Run "Cscript.exe " & Chr(34) & WScript.ScriptFullName & Chr(34)
 WScript.Quit            ' terminate script
End If

set stdout = wscript.StdOut

mystring = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
mystring2 = ""

for i = 1 to len(mystring)

 curchar = Asc(mid(mystring,i,1))

 if curchar > 95 then
  curchar = curchar + 2
  if curchar > 96+25 then
   curchar = curchar - 26
  End If
 End If

 mystring2 = mystring2 & chr(curchar)
Next

stdout.WriteLine(mystring2)
