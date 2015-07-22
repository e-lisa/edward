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
    'success_decrypt' : "Bună ziua, eu sunt Edward, robotul GnuPG cel prietenos. Am primit mesajul dumneavoastră și l-am decriptat. Iată o copie a mesajului dumneavoastră:\n\n",
    'public_key_received' : 'Am primit cheia dumneavoastră publică. Mulțumesc.',
    'failed_decrypt' : "Îmi pare rău, dar nu am putut decripta mesajul dumneavoastră. Sunteți sigur(ă) că l-ați criptat cu cheia mea publică?",
    'no_public_key' : "Îmi pare rău, dar nu am putut găsi cheia dumneavoastră publică. V-ați amintit să o atașați?",
    'sig_failure' : 'Semnătura dumneavoastră nu a putut fi verificată.',
    'sig_success' : 'Semnătura dumneavoastră a fost verificată.',
    'signature' : '- Edward, robotul GnuPG cel prietenos.\n\nFundația pentru Software Liber m-a creat. Puteți dona ca să le susțineți munca? | https://www.fsf.org/donate'
}


