' test, whether the host is CScript.exe
If (Instr(UCase(WScript.FullName), "CSCRIPT") = 0) Then
 Set WshShell = WScript.CreateObject("WScript.Shell")
 WshShell.Run "Cscript.exe " & Chr(34) & WScript.ScriptFullName & Chr(34)
 WScript.Quit            ' terminate script
End If

set stdout = wscript.StdOut


' *** Connect to file system
Set fs = CreateObject("Scripting.FileSystemObject")
Set myFile = fs.OpenTextFile("ocr.txt")
count = 0
done = 0

Do While (myFile.AtEndOfLine <> True) and (done = 0)
 mySTring = myFile.ReadLine()
 mystring2 = ""
 count = count + 1

 for i = 1 to len(mystring)

  curchar = UCase(mid(mystring,i,1))

  if curchar >= "A" and curchar <= "Z" then
   mystring2 = mystring2 & curchar
  End If
 Next

 stdout.WriteLine(count & ": " & mystring2)
Loop

myFile.Close
