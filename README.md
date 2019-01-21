# "Restful User-Service"

## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## Implementierung
Zuerst wurde eine Flask-Rest Schnittstelle implementiert. Dies wurde mithilfe eines Tutorials [1] gelöst. Getestet wurden die Funktionen der Schnittstelle mittels PyTest. Dazu wurde [2] als hilfestellung genommen. Gespeichert werden die Daten in einer SQLite Datenbank.  Lauffähig ist das gesamte mit Tox. Dazu wurde für Tox ein Requirements File geschrieben, welches die benötigten Dinge enthält.

Das Travis File führt 2 Jobs aus, zum einen das Tox und zum anderen die Cypress Testcases. Dafür musste zuerst der Server und das Frontend gestartet werden. 

Anschließend wurde eine GUI für diese Applikation erstellt. Dies wurde mit Vue.js durchgeführt. Zur initialisierung von Vue.js wurde ein Tutorial [3] zur hilfe genommen. Getestet wurde das Frontend mit Cypress. Dazu wurde die Dokumentatiom von Cypress [4] als hilfestellung genommen, um diese Aufgabe zu lösen.
## Quellen
[1][Flask Tutorial](https://pythonspot.com/flask-web-app-with-python/)

[2][PyTest mit Flask](http://flask.pocoo.org/docs/1.0/testing/)

[3][Initialising Vue.js Tutorial](https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532)

[4][Cypress Documentation](https://docs.cypress.io/guides/getting-started/writing-your-first-test.html)