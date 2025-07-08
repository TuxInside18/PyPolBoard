# PyPolBoard  

**Dashboard minimalista per l'organizzazione politica locale**  
Strumento open-source in Python per gestire eventi, contatti e task all'interno di circoli e sezioni di partito.  

## Funzionalità  
- **Gestione eventi**: Creazione, modifica, esportazione in CSV/JSON  
- **Rubrica contatti**: Tagging automatico  
- **Task manager**: Note con sistema di priorità e ricerca full-text  
- **Backup cifrato**: AES-256 + sincronizzazione cloud opzionale  

## Tecnologie usate 
- **Linguaggio**: Python 3.11+  
- **CLI**: Typer  
- **Database**: mySQL  
- **Frontend**: Rich (terminal) / Flask (future web version)  

## Perché usarlo  
1. **Sostituisce Excel/Google Sheet** con strumento dedicato  
2. **Automatizza** il tracciamento delle relazioni politiche  
3. **Open-source** e modificabile per esigenze specifiche  

## Licenza  
GNU Affero GPL v3 - [Dettagli](https://www.gnu.org/licenses/agpl-3.0.html)  

## Stato progetto  
🛠️ Pre-alpha (in sviluppo)  
🗺️ Roadmap: Vedi [Issues](https://github.com/TuxInside18/PyPolBoard/issues)  

```bash
git clone https://github.com/TuxInside18/PyPolBoard.git  
cd PyPolBoard  
pip install -r requirements.txt  
python -m PyPolBoard
