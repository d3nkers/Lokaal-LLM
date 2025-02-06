```md
# Lokaal LLM Dashboard - AI Modellen op Ubuntu

## 🔹 Over dit project
Dit project draait **lokale Large Language Models (LLM’s)** via **Ollama** en **Flask**, met een webinterface waar je eenvoudig kunt wisselen tussen AI-modellen zoals LLaMA3 en Mistral.

Ik begon dit project op Windows, maar liep tegen verschillende beperkingen aan:
- **RAM-gebruik**: Windows kon de modellen niet efficiënt laden zonder vast te lopen.
- **Prestatieproblemen**: Het laden en genereren van tekst was traag.
- **Systeembronnen**: Zelfs kleinere modellen hadden moeite met draaien.

Om dit op te lossen, ben ik overgestapt naar Ubuntu, met geoptimaliseerde instellingen en een betere verdeling van systeembronnen.

```

## 🔹 Huidige status
⚠️ Dit project is nog in ontwikkeling ⚠️ 

**✅ Wat werkt nu?**
- LLaMA3 en Mistral draaien lokaal
- Webinterface gebouwd met Flask
- Dynamisch wisselen tussen modellen
- Streaming van AI-antwoorden voor snellere reacties
- Systeem draait stabiel op **Ubuntu 22.04**

**🔄 Wat wordt nog verbeterd?**
- Contextbeheer optimaliseren voor langere gesprekken
- Meer modellen testen (bijv. DeepSeek, Gemma)
- GPU-acceleratie inschakelen voor betere prestaties



## 🔹 Installatie

### **Stap 1: Installeer Ollama**
Ollama is nodig om de AI-modellen lokaal te draaien.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Stap 2: Zet een Python-omgeving op
```bash
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors requests
```

Stap 3: Haal de modellen op
```bash
ollama pull llama3
ollama pull mistral
```

Stap 4: Start de webserver
```bash
python3 server.py
De webinterface is nu bereikbaar via:
http://127.0.0.1:5004/
```

**🔹 Webinterface en werking**

  De webinterface is gebouwd met HTML, CSS en JavaScript en biedt de volgende functies:


- Chatten met AI

- Dynamisch wisselen tussen modellen

- Streaming-reacties (geen lange wachttijd)


🔹 **Problemen en oplossingen**


**Probleem:** De afbeelding pindahoofd.png werd niet geladen.

Oplossing: De afbeelding verplaatsen naar de juiste map:

```bash
mkdir assets
mv pindahoofd.png assets/pindahoofd_avatar.png
```
En in chat_interface.html de juiste verwijzing gebruiken:


```html
<img src="assets/pindahoofd_avatar.png">
```

LLM reageert traag

**Probleem:** Het duurt lang voordat er een antwoord komt.

Oplossing: Streaming inschakelen in de Flask-backend:

```python
payload = {"model": selected_model, "prompt": user_message, "stream": True}
```


🔹 GPU-versnelling (optioneel)

Dit project kan GPU-versnelling gebruiken als je een NVIDIA-kaart hebt met CUDA-ondersteuning.

⚠️ **Let op**: Dit is niet getest, omdat mijn huidige hardware geen GPU-versnelling ondersteunt.

Als je een geschikte GPU hebt, kun je Ollama starten met CUDA-ondersteuning:

```bash
ollama run --device cuda llama3
```

Wil je controleren of je GPU wordt herkend?

```bash
nvidia-smi
```
Heb je geen GPU? Geen probleem! Het werkt nog steeds op CPU, maar AI-reacties zullen trager zijn.

🔹 Conclusie
Dit project toont aan hoe je lokale LLM-modellen kunt draaien en besturen via een webinterface.
De overstap van Windows naar Ubuntu heeft de prestaties en stabiliteit flink verbeterd.
