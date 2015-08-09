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
    'success_decrypt' : "Привет, я Эдвард, дружелюбный GnuPG бот. Я получил ваше сообщение и расшифровал его. Вот копия вашего сообщения:",
    'public_key_received' : 'Я получил ваш открытый ключ. Спасибо.',
    'failed_decrypt' : "Прошу прощения, я не смог расшифровать ваше сообщение. Вы уверены, что зашифровали его при помощи моего открытого ключа?",
    'no_public_key' : "Прошу прощения, я не смог найти ваш открытый ключ. Вы не забыли вложить его в письмо?",
    'sig_failure' : 'Мне не удалось проверить вашу подпись.',
    'sig_success' : 'Ваша подпись была успешно проверена.',
    'signature' : '- Эдвард, дружелюбный GnuPG бот\nЯ был создан Фондом свободного программного обеспечения. Вы можете сделать пожертвование в поддержку их работы? | https://www.fsf.org/donate'
}


