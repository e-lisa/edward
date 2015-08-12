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
    'greeting' : "Bonjour, je suis Edward, le gentil robot de GnuPG.",
    'success_decrypt' : "J'ai bien reçu votre message et l'ai déchiffré.",
    'quote_follows' : "En voici une copie:",
    'public_key_received' : "J'ai bien reçu votre clef publique. Merci.",
    'failed_decrypt' : "Je n'ai pas été en mesure de déchiffrer votre message, désolé. L'avez-vous bien chiffré avec ma clef publique ?",
    'no_public_key' : "Je n'ai pas pu trouver votre clef publique, désolé. Avez-vous oublié de la joindre ?",
    'sig_failure' : "Votre signature n'a pas pu être vérifiée.",
    'sig_success' : 'Votre signature a été vérifiée.',
    'signature' : "- Edward, le gentil robot de GnuPGn\nLa Free Software Foundation m'a créé. Pourriez-vous faire un don pour soutenir leur travail ? | https://www.fsf.org/donate",
    'space' : " "
}


