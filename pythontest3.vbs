' test, whether the host is CScript.exe
If (Instr(UCase(WScript.FullName), "CSCRIPT") = 0) Then
 Set WshShell = WScript.CreateObject("WScript.Shell")
 WshShell.Run "Cscript.exe " & Chr(34) & WScript.ScriptFullName & Chr(34)
 WScript.Quit            ' terminate script
End If

set stdout = wscript.StdOut

dim counter(256)

' *** Connect to file system
Set fs = CreateObject("Scripting.FileSystemObject")
Set myFile = fs.OpenTextFile("equality.txt")
count = 0
done = 0

Do While (myFile.AtEndOfLine <> True) and (done = 0)
 mySTring = myFile.ReadLine()
 mystring2 = ""
 count = count + 1
lastchar = 0

 for i = 1 to len(mystring)-5

  bigcount = 0
  littlecount = 0
  if (mid(mystring,i,1) <= "Z") Then bigcount = bigcount+1
  if (mid(mystring,i+1,1) <= "Z") Then bigcount = bigcount+1
  if (mid(mystring,i+2,1) <= "Z") Then bigcount = bigcount+1
  if (mid(mystring,i+3,1) >= "a") Then littlecount = 1
  if (mid(mystring,i+4,1) <= "Z") Then bigcount = bigcount+1
  if (mid(mystring,i+5,1) <= "Z") Then bigcount = bigcount+1
  if (mid(mystring,i+6,1) <= "Z") Then bigcount = bigcount+1

  if (bigcount = 6 and littlecount = 1) then
   stdout.WriteLine("Possible match " & Mid(mystring,i,7) & " in line " & count)
  End If


 Next

' stdout.WriteLine(count & ": " & mystring2)
Loop

'for i = 0 to 255
' if counter(i) > 0 Then
'  stdout.WriteLine(chr(i) & " = " & counter(i))
' End If
'Next

myFile.Close
