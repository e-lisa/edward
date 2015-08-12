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
    'greeting' : "Merhaba, Ben Edward, arkadaş canlısı GnuPG botu.",
    'success_decrypt' : "Mesajınızı aldım ve şifresini çözerek düz metine çevirdim.",
    'quote_follows' : "Mesajınızın düz metin kopyası şudur:",
    'public_key_received' : 'Açık anahtarınızı aldım. Teşekkürler.',
    'failed_decrypt' : "Özür dilerim, mesajınızı çözmeyi ve düz metine çevirmeyi başaramadım. Benim açık anahtarımla şifrelediğinize emin misiniz?",
    'no_public_key' : "Özür dilerim, açık anahtarınızı bulamadım. E-postaya eklemeyi unutmadınız, değil mi?",
    'sig_failure' : 'İmzanız doğrulanamadı.',
    'sig_success' : 'İmzanız doğrulandı.',
    'signature' : '- Edward, arkadaş canlısı GnuPG botu\n\nÖzgür Yazılım Vakfı tarafından yaratıldım. Çalışmalarını desteklemek için bağışta bulunur musunuz? | https://www.fsf.org/donate',
    'space' : " "
}


