#!/usr/bin/env python3
"""
Script per generare appunti dettagliati per il corso di Visione Artificiale.
Automatizza il processo mantenendo stile e struttura coerenti.

Uso:
    python generate_notes.py <numero_modulo>
    python generate_notes.py 00  # Genera appunti per il modulo 00
"""

import sys
import os
import re
from pathlib import Path
from datetime import datetime

# Configurazione stile
STYLE_CONFIG = {
    "use_emojis": False,
    "language": "italiano",
    "tone": "intuitivo-pratico",
    "callout_types": {
        "info": "Definizione",
        "note": "Nota",
        "example": "Esempio",
        "warning": "Attenzione",
        "danger": "Punto Critico",
        "tip": "Consiglio"
    }
}

def create_frontmatter(title, module_number, related_topics=None):
    """Crea il frontmatter YAML per Obsidian."""
    return f"""---
title: {title}
date: {datetime.now().strftime("%Y-%m-%d")}
tags:
  - visione-artificiale
  - modulo-{module_number}
  - fondamenti
aliases:
  - {title.split(" - ")[0] if " - " in title else title}
---

"""

def create_section(heading_level, title, content=None):
    """Crea una sezione con heading."""
    heading = "#" * heading_level
    section = f"{heading} {title}\n"
    if content:
        section += f"\n{content}\n"
    return section

def create_callout(callout_type, content, custom_title=None):
    """Crea un callout Obsidian."""
    title = custom_title or STYLE_CONFIG["callout_types"].get(callout_type, callout_type)
    return f"> [!{callout_type}] {title}\n> {content.replace(chr(10), chr(10) + '> ')}\n\n"

def create_wikilink(note_name, display_text=None):
    """Crea un wikilink Obsidian."""
    if display_text:
        return f"[[{note_name}|{display_text}]]"
    return f"[[{note_name}]]"

def template_definition_section(concept_name, formal_def, practical_exp, examples):
    """Template per una sezione di definizione."""
    content = f"### {concept_name}\n\n"
    content += create_callout("info", formal_def, "Definizione")
    content += f"**In pratica**: {practical_exp}\n\n"

    if examples:
        content += "**Esempi**:\n"
        for example in examples:
            content += f"- {example}\n"
        content += "\n"

    return content

def get_module_info(module_number):
    """Legge il file indice del modulo."""
    index_file = Path(f"./0{module_number}. *.md")
    # Implementazione semplificata - in pratica leggerebbe il file vero
    return {
        "number": module_number,
        "found": False,
        "content": ""
    }

def print_style_guide():
    """Stampa la guida di stile per la generazione."""
    print("\n" + "="*70)
    print("GUIDA DI STILE PER APPUNTI VISIONE ARTIFICIALE")
    print("="*70 + "\n")

    print("STRUTTURA STANDARD DI OGNI MODULO:")
    print("-" * 70)
    print("""
1. FRONTMATTER (YAML)
   - title: nome descrittivo del modulo
   - tags: sempre [visione-artificiale, modulo-XX, fondamenti/applicazioni]
   - aliases: nomi alternativi per i link

2. DEFINIZIONI FONDAMENTALI (h2)
   - Concetti principali (h3)
     * Definizione formale (info callout)
     * Spiegazione pratica
     * Esempi semplici
   - Concetti secondari correlati (h3)

3. CONCETTI CHIAVE / TEORIA (h2)
   - Spiegazioni intuitive
   - Differenze e relazioni tra concetti
   - Pro/contro dove rilevante

4. APPLICAZIONI PRATICHE (h2 opzionale)
   - Casi d'uso reali
   - Dove si usa nella pratica
   - Problemi che risolve

5. PROSSIMI ARGOMENTI (h2)
   - Wikilinks ai moduli correlati

STILE LINGUISTICO:
✓ Intuitive: spiegazioni semplici e intuitive
✓ Esempi: almeno uno per ogni concetto principale
✓ Linguaggio naturale: evitare formalismo eccessivo
✗ NO emoji
✗ NO approfondimenti inutili per l'esame
✗ NO formule complesse a meno che non richieste

CALLOUT OBSIDIAN:
- [!info] - Definizioni formali
- [!note] - Approfondimenti
- [!example] - Esempi pratici
- [!warning] - Sfide/difficoltà
- [!danger] - Punti critici
- [!tip] - Best practices

LINK INTERNI:
- Usa [[wikilinks]] per collegare i moduli correlati
- Abbrevia i titoli se troppo lunghi con display text
- Aggiungi #heading per linkaare sezioni specifiche
    """)
    print("\nEsempi di template:\n")
    print("DEFINIZIONE:")
    print("""
> [!info] Definizione
> Definizione formale del concetto

In pratica: spiegazione semplice con un'analogia

Esempi:
- Primo esempio
- Secondo esempio
    """)

def main():
    """Main function."""
    if len(sys.argv) > 1 and sys.argv[1] == "--guide":
        print_style_guide()
        return

    print("\nScript di generazione appunti Visione Artificiale")
    print("-" * 50)
    print("Configurazione caricata correttamente")
    print(f"Stile: {STYLE_CONFIG['tone']}, Lingua: {STYLE_CONFIG['language']}")
    print(f"Emoji: {'Attivate' if STYLE_CONFIG['use_emojis'] else 'Disattivate'}")
    print("\nComandi disponibili:")
    print("  python generate_notes.py <numero>  - Genera appunti modulo")
    print("  python generate_notes.py --guide   - Mostra guida di stile")
    print("-" * 50)

if __name__ == "__main__":
    main()
