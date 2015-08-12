#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""*********************************************************************
* This file is part of Edward the GPG Bot.                             *
*                                                                      *
* Edward is free software: you can redistribute it and/or modify       *
* it under the terms of the GNU Affero Public License as published by  *
* the Free Software Foundation, either version 3 of the License, or    *
* (at your option) any later version.                                  *
*                                                                      *
* Edward is distributed in the hope that it will be useful,            *
* but WITHOUT ANY WARRANTY; without even the implied warranty of       *
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        *
* GNU Affero Public License for more details.                          *
*                                                                      *
* You should have received a copy of the GNU Affero Public License     *
* along with Edward.  If not, see <http://www.gnu.org/licenses/>.      *
*                                                                      *
* Josh Drake, Copyright (c) 2014                                       *
* Lisa Marie Maginnis, Copyright (c) 2014                              *
*********************************************************************"""

replies = {
    'greeting' : "Ciao, io sono Edward, l'amichevole bot GnuPG.",
    'success_decrypt' : "Ho ricevuto il tuo messaggio e l'ho decriptato.",
    'quote_follows' : "Questa è una copia del tuo messaggio:",
    'public_key_received' : 'Ho ricevuto la tua chiave pubblica. Grazie.',
    'failed_decrypt' : "Mi dispiace, non sono stato in grado di decifrare il tuo messaggio. Sei sicuro di averlo criptato con la mia chiave pubblica?",
    'no_public_key' : "Mi dispiace, non ho trovato la tua chiave pubblica. Ti sei ricordato di allegarla?",
    'sig_failure' : 'La tua firma non può essere verificata.',
    'sig_success' : 'La tua firma è stata verificata.',
    'signature' : "- Edward, l'amichevole bot GnuPG\n\nLa Free Software Foundation mi ha creato. Potresti fare una donazione per supportare il loro lavoro? | https://www.fsf.org/donate",
    'space' : " "
}

