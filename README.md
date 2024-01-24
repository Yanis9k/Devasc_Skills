# Devasc_Skills

Task name => name of the task
Task preparation => what preparation is necessary to perform the task? (short)
Task implementation => what is the way you have implemented this? 
Task troubleshooting => what were the problems encountered?
Task verification => proof of the quality of the result

Task 1 
Dus, ik heb een nieuwe repository op GitHub aangemaakt. Daarna heb ik een map met een specifieke naam gemaakt en deze geopend in Visual Studio Code. In de terminal heb ik een reeks Git-commando's ingevoerd.

Eerst heb ik de map geïnitialiseerd als een Git-repository met het commando `git init`. Daarna heb ik de GitHub-repository naar mijn lokale machine gekloond met `git clone` en de link van het repository.

Om wijzigingen toe te voegen, heb ik eerst iets in de map aangepast, bijvoorbeeld door een Python-bestand aan te maken, er iets in te typen en het op te slaan. Vervolgens heb ik de wijzigingen toegevoegd aan de "staging area" met `git add .`.

Daarna heb ik de wijzigingen gecommit met `git commit -m` en een beschrijvend bericht toegevoegd over wat ik heb gedaan. Ik heb ook de standaard branchnaam gewijzigd van "master" naar "main" met `git branch -M main`.

Om de GitHub-repository als externe locatie toe te voegen, heb ik `git remote add origin` gebruikt. Ten slotte heb ik de lokale commits naar GitHub gepusht met `git push -u origin main`.

Uiteindelijk heb ik gecontroleerd of de wijzigingen op GitHub waren doorgevoerd door naar de repository te kijken. En dat is in feite de reeks stappen die ik heb genomen om mijn repository op te zetten en wijzigingen toe te voegen.

Mijn code in de terminal: 
git init
        git clone https://github.com/Yanis9k/Devasc_Skills.git
        git add .     

        git commit -m "push1"
        git branch -M main
        git remote add origin https://github.com/Yanis9k/Devasc_Skills.git
        git push -u origin main



Task 2 

Niet mogenlijk wegens switch connectie probleem



Task 3

1. **Navigatiefout bij het wisselen van map:**
   Er was een typefout bij het veranderen van de mapnaam van "Dockerdile" naar "Dockerfile".

   ```
   devasc@labvm:~/Docker$ cd Dockerfile
   ```

2. **Syntaxfouten in Docker-opdrachten:**
   Er waren syntaxfouten in de `docker image build`- en `docker run`-opdrachten, met ongebalanceerde haakjes. Het is belangrijk om de plaatshoudernaam te vervangen door echte namen.

   ```
   devasc@labvm:~/Docker$ docker image build -t mijn_image .
   devasc@labvm:~/Docker$ docker run -d -p 8080:80 --name mijn_container mijn_image
   ```

3. **Fout bij het gebruik van curl:**
   De `curl`-opdracht mislukte omdat de container mogelijk niet was gestart of er een probleem was met de poort. Zorg ervoor dat de container actief is voordat je de curl-opdracht uitvoert.

   ```
   devasc@labvm:~/Docker$ curl http://localhost:8080/
   ```

4. **Build-fout met ontbrekende bestanden:**
   Er was een probleem bij het bouwen van de Docker-image omdat de bestanden `index.html` en `datescript.js` niet werden gevonden in de beoogde map `templates`.

   ```
   devasc@labvm:~/Docker$ docker image build -t image1 .
   ```

5. **Succesvolle uitvoering van Docker-opdrachten:**
   Na het corrigeren van de problemen werd de Docker-container met succes gebouwd en uitgevoerd. Opmerking: er was eerder een fout omdat het Docker-image nog niet was gemaakt.

   ```
   devasc@labvm:~/Docker$ docker ps
   ```

Taak 5 

Niet mogenlijk wegens switch connectie probleem

Taak 6

Dit Python-script maakt gebruik van de Webex Teams API om een ruimte te creëren, leden uit te nodigen en berichten in die ruimte te verzenden. Hier is een stapsgewijze uitleg van het script:

1. **Importeren van modules:**
   De modules `requests` en `json` worden geïmporteerd om HTTP-verzoeken uit te voeren en JSON-gegevens te manipuleren.

   ```python
   import requests
   import json
   ```

2. **Webex Teams API-instellingen:**
   De variabelen `api_url` en `api_token` bevatten respectievelijk de basis-URL van de Webex Teams API en de vereiste API-token voor autorisatie.

   ```python
   api_url = "https://api.ciscospark.com/v1"
   api_token = "jouw_webex_teams_api_token"
   ```

3. **E-mailadressen van leden:**
   De e-mailadressen van de leden worden opgeslagen in de variabelen `your_email` en `yvan_email`.

   ```python
   your_email = "jouw_email@example.com"
   yvan_email = "email_yvan@example.com"
   ```

4. **Naam van Webex Teams-ruimte:**
   De naam van de Webex Teams-ruimte wordt opgeslagen in de variabele `space_name`.

   ```python
   space_name = "devasc_skills_YanisSebagh"
   ```

5. **Functie om een Webex Teams-ruimte te creëren:**
   De functie `create_space` neemt de API-URL, API-token en de ruimtanaam als parameters, creëert een ruimte en retourneert de ID van de aangemaakte ruimte.

   ```python
   def create_space(api_url, api_token, space_name):
       # ...
   ```

6. **Functie om leden uit te nodigen voor een Webex Teams-ruimte:**
   De functie `invite_members` neemt de API-URL, API-token, de ID van de ruimte en een lijst met e-mailadressen als parameters, en nodigt de leden uit om deel te nemen aan de ruimte.

   ```python
   def invite_members(api_url, api_token, space_id, email_list):
       # ...
   ```

7. **Functie om een bericht naar een Webex Teams-ruimte te sturen:**
   De functie `send_message` neemt de API-URL, API-token, de ID van de ruimte en een bericht als parameters, en stuurt dit bericht naar de ruimte.

   ```python
   def send_message(api_url, api_token, space_id, message):
       # ...
   ```

8. **Creatie van de Webex Teams-ruimte:**
   De variabele `space_id` wordt geïnitialiseerd met de ID van de aangemaakte ruimte door de functie `create_space`.

   ```python
   space_id = create_space(api_url, api_token, space_name)
   ```

9. **Uitnodiging van leden voor de ruimte:**
   De functie `invite_members` wordt opgeroepen om leden uit te nodigen om deel te nemen aan de ruimte.

   ```python
   invite_members(api_url, api_token, space_id, [your_email, yvan_email])
   ```

10. **Publicatie van de URL van het GitHub-repository in de ruimte:**
    De URL van het GitHub-repository wordt opgeslagen in `github_repo_url`, en vervolgens wordt de functie `send_message` gebruikt om deze URL in de ruimte te plaatsen.

    ```python
    github_repo_url = "https://github.com/Yanis9k/Devasc_Skills.git"
    send_message(api_url, api_token, space_id, f"Bekijk mijn GitHub-repository: {github_repo_url}")
    ```

11. **Verzenden van een bericht naar de ruimte:**
    Tot slot wordt een bericht naar de ruimte gestuurd.

    ```python
    send_message(api_url, api_token, space_id, "Hier zijn mijn schermafbeeldingen van het devasc skills-examen.")
    ```

Taak 7
Niet mogenlijk wegens switch probleem


Taak 10

Stap 1: In de eerste stap is een Python-script gemaakt in een map genaamd "Danc". Het script maakt gebruik van de requests-module om verbinding te maken met het Cisco DNA Center (DNAC) via de Web API. Het verkrijgt een token voor authenticatie en haalt vervolgens de informatie op van netwerkapparaten in het DNAC. De verkregen gegevens omvatten hostname, familie, MAC-adres, IP-adres, softwareversie en bereikbaarheidsstatus van de apparaten.

Stap 2: In de tweede stap is een nieuw programma gemaakt dat de tijd en apparaatinformatie afdrukt. Dit programma maakt ook gebruik van JSON en maakt verbinding met het web om vergelijkbare informatie op te halen als in stap 1. De uitvoer van dit programma is vergelijkbaar met wat wordt getoond in "output_task_10".

Stap 3: Om het Python-script uit te voeren, moet de opdracht `python3 (python_script_name.py)` worden ingevoerd in de bash-terminal. De vervangbare tekst "(python_script_name.py)" moet worden vervangen door de daadwerkelijke naam van het Python-scriptbestand. Het uitvoeren van deze opdracht start het script en geeft de resultaten weer zoals gespecificeerd in het script.

Dit proces biedt een gestructureerde manier om verbinding te maken met Cisco DNAC, apparaatgegevens op te halen en deze informatie op een overzichtelijke manier weer te geven. Het gebruik van JSON en de requests-module vergemakkelijkt de communicatie met de Web API van DNAC.
Dit is de code : 
import requests
import datetime
import json
requests.packages.urllib3.disable_warnings()

DNAC_scheme = 'https://'
DNAC_authority='sandboxdnac.cisco.com'
DNAC_port=':443'
DNAC_path_token='/dna/system/api/v1/auth/token'
DNAC_path='/dna/intent/api/v1/network-device'
DNAC_user = 'devnetuser'
DNAC_psw = 'Cisco123!'


print("Current date and time: ")
print(datetime.datetime.now())


token_req_url = DNAC_scheme + DNAC_authority + DNAC_path_token
auth = (DNAC_user, DNAC_psw)
req = requests.request('POST', token_req_url, auth=auth, verify=False)
token = req.json()['Token']
req_url = DNAC_scheme + DNAC_authority + DNAC_port + DNAC_path
headers = {'X-Auth-Token': token}
resp_devices = requests.request('GET', req_url, headers=headers, verify=False)
resp_devices_json = resp_devices.json()


for device in resp_devices_json['response']:
    if device['type'] is not None:
        print('===')
        print('Hostname: ' + device['hostname'])
        print('Family  : ' + device['family'])
        print('MAC: ' + device['macAddress'])
        print('IP: ' + device['managementIpAddress'])
        print('Software version: ' + device['softwareVersion'])
        print('Reachability: ' + device['reachabilityStatus'])
