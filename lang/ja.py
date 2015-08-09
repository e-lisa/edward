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
    'success_decrypt' : "こんにちは！ 私はGnuPGボットのEdwardです。あなたから送られたメールの暗号を解きました。確認のため、内容を返信します：",
    'public_key_received' : 'あなたの公開鍵を受けとりました。',
    'failed_decrypt' : "あなたからのメッセージを解読できなくて、すみません。そちらでは暗号化のとき、私の公開鍵を使ってくださったでしょうか？",
    'no_public_key' : "ごめんなさい、あなたの公開鍵が見つからないのです。公開鍵を添付したメールを前に送ってくださいましたか？",
    'sig_failure' : 'あなたの署名を認証できませんでした。',
    'sig_success' : ' あなたの署名を確認できました。',
    'signature' : '- GnuPGボットのEdward\n\nFree Software Foundationが私を制作しました。 Free Software Foundationに寄付しませんか。| https://www.fsf.org/donate'
}


