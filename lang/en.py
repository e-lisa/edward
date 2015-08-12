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
    'greeting' : "Hello, I am Edward, the friendly GnuPG bot.",
    'success_decrypt' : "I received your message and decrypted it.",
    'quote_follows' : "Here's a copy of your message:",
    'public_key_received' : 'I received your public key. Thanks.',
    'failed_decrypt' : "I'm sorry, I was not able to decrypt your message. Are you sure you encrypted it with my public key?",
    'no_public_key' : "I'm sorry, I was not able to find your public key. Did you remember to attach it?",
    'sig_failure' : 'Your signature could not be verified.',
    'sig_success' : 'Your signature was verified.',
    'signature' : '- Edward, the friendly GnuPG bot\nThe Free Software Foundation created me.\n\nCan you donate to support their work?\nhttps://www.fsf.org/donate',
    'space' : " "
}


