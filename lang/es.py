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
    'greeting' : "Hola, soy Edward, el simpático robot GnuPG.",
    'success_decrypt' : "He recibido tu mensaje y lo he descifrado.",
    'quote_follows' : " Aquí tienes una copia de tu mensaje:",
    'public_key_received' : 'He recibido tu clave pública. Gracias.',
    'failed_decrypt' : "Lo siento, no he podido descifrar tu mensaje. ¿Estás seguro de haberlo cifrado con mi clave pública?",
    'no_public_key' : "Lo siento, no he podido encontrar tu clave pública. ¿Te acordaste de adjuntarla?",
    'sig_failure' : 'No he podido verificar tu firma criptográfica.',
    'sig_success' : 'He verificado con éxito tu firma criptográfica.',
    'signature' : '- Edward, el simpático robot GnuPG\n\nMe creó la Free Software Foundation. ¿Puedes hacer una donación para apoyar su trabajo? | https://www.fsf.org/donate',
    'space' : " "
}

