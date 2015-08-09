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
    'success_decrypt' : "Γειά σου, είμαι ο Edward, το φιλικό ρομπότ του GnuPG. Έλαβα το μήνυμα σου και το αποκρυπτογράφησα. Δες ένα αντίγραφο του μηνύματος σου:",
    'public_key_received' : 'Έλαβα το δημόσιο κλειδί σου. Ευχαριστώ.',
    'failed_decrypt' : "Λυπάμαι, δε μπόρεσα να αποκρυπτογραφήσω το μήνυμα σου. Είσαι σίγουρος/η ότι το κρυπτογράφησες με το δημόσιο κλειδί μου;",
    'no_public_key' : "Δυστυχώς δε μπόρεσα να βρώ το δημόσιο κλειδί σου. Μήπως ξέχασες να το επισυνάψεις;",
    'sig_failure' : 'Δε μπόρεσα να επαληθεύσω την υπογραφή σου.',
    'sig_success' : 'nΕπαλήθευσα την υπογραφή σου.',
    'signature' : '- Edward, το φιλικό ρομπότ του GnuPG\n\nΜε δημιούργησε η Free Software Foundation. Μπορείς να υποστηρίξεις το έργο τους με μια δωρεά; | https://www.fsf.org/donate'
}


