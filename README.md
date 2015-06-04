# IpFinder
IpFinder is a simple command line tool for discovering the IP addresses of sub-domains.
It is intended for discovering the IP address of a server behind a proxy or CDN by locating a
sub domain that connects directly to the IP address of the server, for example, to give SSH 
access to a server behind Cloud Flare.

A second legally questionable use is to identify the IP address of a website that is hateful, 
abusive, or harassing.  You should discuss such use with a lawyer prior to use because establishing
connections for this purpose could be illegal.  Use of this tool for this purpose is not supported
by anyone and you are advised to determine whether it will be legal.

Use
---------

The IpFinder tool is run from the command line as a single command to support shell scripting.

The simplest option is to run the command with the domain that you want to test subdomains of.
`python ipFinder.py google.com`

There are a few options that you can use to change the behavior of the script.
`-sM` will not record domains that have previously discovered IP addresses.  You should use this
if the domain has a DNS wildcard record.
`-cS` followed by a number will select the character set to use when enumerating sub domains.  You
can view the help screen `-h` or `--help` for a list of character sets.

IP addresses will be recorded in the ip.log file.
