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
    'greeting' : "Hallo, Ich bin Edward, der freundliche GnuPG Roboter.",
    'success_decrypt' : "Ich deine E-Mail empfangen und entschlüsselt.",
    'quote_follows' : "Hier ist eine Kopie deiner Nachricht:",
    'public_key_received' : 'Ich habe deinen öffentlicher Schlüssel erhalten. Danke.',
    'failed_decrypt' : "Tut mir leid, ich konnte deine Nachricht nicht entschlüsseln. Bist du dir sicher, dass du sie mit meinem öffentlichen Schlüssel verschlüsselt hast?",
    'no_public_key' : "Tut mir leid, Ich konnte deinen öffentlicher Schlüssel nicht finden. Hast du daran gedacht ihn an die E-Mail anzuhängen?",
    'sig_failure' : 'Deine Signatur konnte nicht verifiziert werden.',
    'sig_success' : 'Deine Signatur wurde erfolgreich verifiziert.',
    'signature' : '- Edward, der freundliche GnuPG Roboter\nnDie Free Software Foundation hat mich erstellt. Kannst du etwas spenden, um ihre Arbeit zu unterstützung? | https://www.fsf.org/donate',
    'space' : " "
}


