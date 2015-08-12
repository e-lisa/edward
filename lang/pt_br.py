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
    'greeting' : "Olá, sou Edward, o amigo robô de GnuPG.",
    'success_decrypt' : "Recebi e decifrei sua mensagem.",
    'quote_follows' : "Aqui vai uma cópia da sua mensagem:",
    'public_key_received' : 'Recebi sua chave pública. Muito agradecido.',
    'failed_decrypt' : "Perdão, não consegui decifrar sua mensagem. Você tem certeza que a cifrou usando minha chave pública?",
    'no_public_key' : "Perdão, não consegui encontrar sua chave pública. Você se lembrou de anexá-la?",
    'sig_failure' : 'Sua assinatura não pôde ser verificada.',
    'sig_success' : 'Sua assinatura foi verificada.',
    'signature' : '- Edward, o amigo robô de GnuPG\n\nA Free Software Foundation me criou. Você pode fazer uma doação para apoiar o trabalho dela? | https://www.fsf.org/donate',
    'space' : " "
}


