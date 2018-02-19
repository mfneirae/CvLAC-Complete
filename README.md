<!--

#############################################################################
        Copyright (c) 2018 by Manuel Embus. All Rights Reserved.

            This work is licensed under a Creative Commons
      Attribution - NonCommercial - ShareAlike 4.0
      International License.

      For more information write me to jai@mfneirae.com
      Or visit my webpage at https://mfneirae.com/
#############################################################################

 -->
# CvLAC to Excel - UAPA - UNAL

This project corresponds to an open source tool to webscraping CvLAC - Colciencias Page with self-assessment and accreditation purpuses.

The entire project is associated to the
[Unidad de Apoyo a Procesos de Autoevaluación y Acreditación](http://ingenieria.unal.edu.co/dependencias/vicedecanatura-academica/autoevaluacion) of the [Universidad Nacional de Colombia](http://unal.edu.co/).


## Instructions
1. Requirements:
  * Windows 8 or higher / Ubuntu 14 or higher.
  * Python 3.6.
  * Internet Access.
  * Any Text Editor (I used Atom 3).
2. Install:
  * Copy this repository to your machine.
  * install bs4
  ```
    pip install bs4
  ```  
  * install openpyxl
  ```
    pip install openpyxl
  ```  
3. Usage:
  * Locate the CvLAC that you want to use.
  * Copy the URL.
  * Open main.py on your text editor.
  * replace "my_url" with the URL that you want to use.
  * Open a Terminal (CMD, bash, Git... does not matters).
  * Run:
  ```
    python main.py
  ```  
  * That is all, you sould see your data stored in the Resultados folder.
