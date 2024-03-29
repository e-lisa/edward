# About 'edward'

This is 'edward', a program that automatically responds to GPG encrypted and
signed email. It tests whether users' early attempts to use GPG encrypted and
signed email are successful.

At the time of writing, this program is used by the Free Software Foundation
as part of its campaign at https://emailselfdefense.org

Edward's Git repo is current hosted at:
<https://vcs.fsf.org/?p=edward.git;a=summary>

    $ git clone https://vcs.fsf.org/git/edward.git

## License

This program, its translation files, and its automated test cases are licensend
under AGPLv3.

The public and private GPG keys in tests/testgnupghome are licensed under CC0.

    * https://creativecommons.org/publicdomain/zero/1.0/

## Dependencies

    $ sudo apt-get install python3 python3-gpgme sendmail

## Usage

To run the test cases in the top level directory: (No emails are sent)

    $ ln -s edward_config.py.example edward_config.py
    $ ./run-tests

Edward expects the TO address of incoming emails and the FROM address of
outgoing emails to be "edward-en@domain" or "edward-es@domain", etc. For a list
of supported languages, look at the beginning of the edward source file, or
look in the lang/ directory.

To view edward's output email without sending it: (for debugging purposes)

    $ ./edward -p < input-email.eml

To automatically send the the replay email using sendmail: (For this to work,
you will need to properly setup your mail transfer agent (MTA).)

    $ ./edward < input-email.eml

No news (aside from execution duration) is good news.

To automatically pipe incoming messages to edward and send its replies: (Notice
the added dot.)

    $ cp edward_config.py.example edward_config.py
    $ nano edward_config.py

    $ cd ~ ; mv edward edward-src
    $ cp edward-src/procmailrc.example ~/.procmailrc
    $ nano .procmailrc

