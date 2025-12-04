titel: Seite 3

{% include nav.html %}



die Größe des Delta nach dem Commiten anhand von

<pre>git show --stat
<font color="#CDCD00">commit 30eb1ce53382c1544853145e0cad30ef0263abbe (</font><font color="#00FFFF"><b>HEAD</b></font><font color="#CDCD00"> -&gt; </font><font color="#00FF00"><b>main</b></font><font color="#CDCD00">, </font><font color="#FF0000"><b>origin/main</b></font><font color="#CDCD00">, </font><font color="#FF0000"><b>origin/HEAD</b></font><font color="#CDCD00">)</font>
Date:   Mon Jan 20 22:21:50 2025 +0100

    feat(Factory Method)
    
    - add ConsoleService and ConsoleNotification
    - complement test

 bsp/src/main/java/task01/ConsoleNotification.java     | 18 <font color="#00CD00">++++++++++++++++++</font>
 bsp/src/main/java/task01/ConsoleService.java          |  9 <font color="#00CD00">+++++++++</font>
 bsp/src/main/java/task01/SystemTrayNotification.java  |  2 <font color="#CD0000">--</font>
 bsp/src/test/java/task01/NotificationServiceTest.java | 33 <font color="#00CD00">++++++++++++++++++++++++++++++</font><font color="#CD0000">---</font>
 4 files changed, 57 insertions(+), 5 deletions(-)
</pre>


die entstandenen Änderungen sind durch die neue Klasse minimal, da in diese nur die nötige Struktur (sprich Implementierung der abstrakten Methode) hinzugefügt werden musste. Die meisten Zeilen wurden in die Test-Klasse hinzugefügt worden.

[home](index.md)
