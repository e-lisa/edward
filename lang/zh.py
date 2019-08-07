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
    'greeting' : "你好，我是爱德华，一个友好的 GnuPG 机器人。",
    'success_decrypt' : "我收到你的消息并解密了它。",
    'quote_follows' : "以下是原始消息的副本：",
    'public_key_received' : '我收到了你的公钥。谢谢。',
    'failed_decrypt' : "抱歉，我无法解密你的消息。你确定加密消息时使用的是我的公钥吗？",
    'no_public_key' : "抱歉，我无法找到你的公钥。你忘记附件里发送公钥了吗？",
    'sig_failure' : '签名无法验证。',
    'sig_success' : '签名已验证。',
    'signature' : '- 爱德华，一个友好的 GnuPG 机器人\n自由软件基金会创造了我。\n\n你能捐款支持他们的工作吗？\nhttps://www.fsf.org/donate',
    'space' : " "
}



