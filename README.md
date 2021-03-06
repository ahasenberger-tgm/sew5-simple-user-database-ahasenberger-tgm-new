# "Restful User-Service"

## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## Implementierung
Zuerst wurde eine Flask-Rest Schnittstelle implementiert. Dies wurde mithilfe eines Tutorials [1] gelöst. Getestet wurden die Funktionen der Schnittstelle mittels PyTest. Dazu wurde [2] als hilfestellung genommen. Gespeichert werden die Daten in einer SQLite Datenbank. Dort gibt es genau eine Tabelle, in welcher die Daten gespeichert werden. Lauffähig ist das gesamte mit Tox. Dazu wurde für Tox ein Requirements File geschrieben, welches die benötigten Dinge enthält.

Das Travis File führt 2 Jobs aus, zum einen das Tox und zum anderen die Cypress Testcases. Dafür musste zuerst der Server und das Frontend gestartet werden. 

Anschließend wurde eine GUI für diese Applikation erstellt. Dies wurde mit Vue.js durchgeführt. Dort wurde zur Anzeige der Daten aus der Datenbank eine dynamische Liste erstellt. Zusätzlich befinden sich dort Eingabefelder, welche zur Erstellung, zur Änderung und zur Löschung eines Schülers. Damit die richtige Seite aufgerufen wird, musste die Route in der Vue.js konfiguration geändert werden. Zur initialisierung von Vue.js wurde ein Tutorial [3] zur hilfe genommen. Getestet wurde das Frontend mit Cypress. Dazu wurde die Dokumentatiom von Cypress [4] als hilfestellung genommen, um diese Aufgabe zu lösen.

## Ausführen
### Frontend und Server
Um den Vue Client ausführen zu können, müssen folgende Befehle ausgeführt werden:
```console
cd src/main/python/client/frontend
npm run dev
```
Die Vue.js Applikation läuft dann auf Port ```8080```.
Jedoch muss beachtet werden, dass vor der Verwendung der Vue.js Applikation der Rest-Server gestartet wird. Dieser kann mit folgenden Befehlen gestartet werden:
```console
cd src/main/python/server
python rest.py
``` 
Wenn dieser in der Konsole ausgeführt werden soll, dann muss auch beachtet werden, dass alle Dependencies installiert werden. Die andere Möglichkeit wäre, den Rest-Server direkt in PyCharm zu starten. Der Rest-Server läuft auf Port ```5000```.
### Tox
Um sowohl die Frontend Tests und auch die PyTests auszuführen, muss Tox gestartet werden. Dies geht indem man sich im Projektordner befindet und folgendes ausführt:
```console
tox
```
### Testreport
Nachdem Tox ausgeführt wurde, kann man in der Konsole einen Testreport sehen, welcher zeigt ob die Testcases erfolgreich waren. Zusätzlich ist dort die Test-Coverage zu sehen. 
Außerdem wird der Testreport als HTML-File generiert.

Dieser wird im Root-Verzeichnis des Projekts gespeichert. Dort sind die Ergebnisse der einzelnen Testcases einzusehen. Die Coverage wird in einem HTML-File dokumentiert, welches sich im Ordner /cov_html/ befindet. In diesem Ordner muss das File index.html geöffnet werden.

Damit der Coverage Report funktioniert, mussten folgende Parameter in das tox.ini in die Zeile des PyTests hinzugefügt werden: ```--cov-report html:cov_html```
## Quellen
[1][Flask Tutorial](https://pythonspot.com/flask-web-app-with-python/)

[2][PyTest mit Flask](http://flask.pocoo.org/docs/1.0/testing/)

[3][Initialising Vue.js Tutorial](https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532)

[4][Cypress Documentation](https://docs.cypress.io/guides/getting-started/writing-your-first-test.html)